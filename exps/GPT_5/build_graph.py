#!/usr/bin/env python3
"""Parse exps/GPT_5/graph.md and emit a ClusteredGraph-format JSON.

Run:
    python build_graph.py
"""
from __future__ import annotations

import json
import re
import sys
from collections import OrderedDict
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]  # clustering_1/
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from llm_v2.schemas.clustered_graph import (
    ClusteredEdge,
    ClusteredGraph,
    ClusteredGraphMeta,
    ClusteredNode,
)
from llm_v2.schemas.common import Mention


# `| `Exx` | label-cells... |`  — capture id + everything after the second pipe
ENTITY_ROW_RE = re.compile(r"^\|\s*`(E\d+)`\s*\|(.+)$")
# `<src> —[<relation>]→ <target>`
EDGE_LINE_RE = re.compile(r"^(.+?)\s+—\[(.+?)\]→\s+(.+?)\s*$")
# leading `Exx` token (target like `E09 находился по одну сторону от E14`)
ENTITY_PREFIX_RE = re.compile(r"^(E\d+)\b")


def parse_entity_row(line: str) -> tuple[str, str] | None:
    """Parse one entity row, reconstructing labels that contain pipes (LaTeX `||w||`)."""
    m = ENTITY_ROW_RE.match(line)
    if not m:
        return None
    eid, rest = m.group(1), m.group(2)
    cells = [c.strip() for c in rest.split("|")]
    while cells and cells[-1] == "":
        cells.pop()
    if not cells:
        return None
    label = "|".join(cells).strip()
    return eid, label


def parse_md(md_text: str) -> tuple[OrderedDict[str, str], list[tuple[str, str, str]]]:
    entities: OrderedDict[str, str] = OrderedDict()
    edges_raw: list[tuple[str, str, str]] = []

    for line in md_text.splitlines():
        s = line.rstrip()
        if not s:
            continue
        if s.lstrip().startswith("|"):
            parsed = parse_entity_row(s.lstrip())
            if parsed:
                entities[parsed[0]] = parsed[1]
            continue
        m = EDGE_LINE_RE.match(s)
        if m:
            edges_raw.append(
                (m.group(1).strip(), m.group(2).strip(), m.group(3).strip())
            )
    return entities, edges_raw


def build_graph(md_path: Path) -> ClusteredGraph:
    entities, edges_raw = parse_md(md_path.read_text(encoding="utf-8"))
    literals: OrderedDict[str, str] = OrderedDict()

    def resolve(text: str) -> str:
        """Map a raw endpoint string to a node id.

        - if it starts with a known `Exx`, return that entity id (drop trailing description)
        - otherwise create / reuse a synthetic literal node `lit_N`
        """
        m = ENTITY_PREFIX_RE.match(text)
        if m and m.group(1) in entities:
            return m.group(1)
        if text not in literals:
            literals[text] = f"lit_{len(literals)}"
        return literals[text]

    src_md = md_path.name

    # build edges
    edges: list[ClusteredEdge] = []
    for i, (src, rel, tgt) in enumerate(edges_raw):
        eid = f"R{i + 1}"
        edges.append(
            ClusteredEdge(
                id=eid,
                source=resolve(src),
                target=resolve(tgt),
                label=rel,
                members=[eid],
                size=1,
            )
        )

    # build nodes (entities first, then literals)
    nodes: list[ClusteredNode] = []
    for eid, label in entities.items():
        nodes.append(
            ClusteredNode(
                id=eid,
                label=label,
                members=[eid],
                size=1,
                mentions=[Mention(text=label, chunk_id=src_md)],
            )
        )
    for text, lit_id in literals.items():
        nodes.append(
            ClusteredNode(
                id=lit_id,
                label=text,
                members=[lit_id],
                size=1,
                mentions=[Mention(text=text, chunk_id=src_md)],
            )
        )

    meta = ClusteredGraphMeta(
        created_at=datetime.now(timezone.utc).isoformat(),
        source_text=src_md,
        config_summary={
            "source": "GPT-5 reference graph (manual)",
            "md_file": src_md,
            "entities": len(entities),
            "literals": len(literals),
        },
        stats={
            "nodes": len(nodes),
            "edges": len(edges),
            "entity_nodes": len(entities),
            "literal_nodes": len(literals),
        },
    )

    return ClusteredGraph(meta=meta, nodes=nodes, edges=edges)


def main() -> None:
    md_path = HERE / "graph.md"
    graph = build_graph(md_path)
    out = HERE / "clustered_graph.json"
    out.write_text(
        json.dumps(graph.model_dump(), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    n_ent = sum(1 for n in graph.nodes if n.id.startswith("E"))
    n_lit = sum(1 for n in graph.nodes if n.id.startswith("lit_"))
    print(f"Saved {out}")
    print(f"  Nodes: {len(graph.nodes)}  (entities={n_ent}, literals={n_lit})")
    print(f"  Edges: {len(graph.edges)}")


if __name__ == "__main__":
    main()
