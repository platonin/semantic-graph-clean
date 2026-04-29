# Phase 2 — toggles

Запускается **после** phase 1. По её результатам:

1. В `analysis.ipynb` смотрим лучший `(LLM, embedder, method, param)` по `graph_score` → setup A.
2. Берём второй (например, лучший локальный, если в setup A был API; или вообще другая метрика интересна) → setup B.
3. Для каждого setup'а делаем 4 подэксперимента:

| Папка | Изменение vs phase 1 baseline |
|---|---|
| `00_baseline` | без изменений (можно symlink на phase 1-результат, чтобы не пересчитывать) |
| `01_coref_on` | `coreference.enabled: true` |
| `02_norm_off` | `normalization.enabled: false` |
| `03_naming_on` | `clustering.multi_method: false`, `method: <best>`, фикс параметра + `llm_naming: true` |

Для `03_naming_on` важно отказаться от `multi_method`: иначе LLM-naming прогонится на 57 вариантах и съест всё время. Берём один лучший вариант кластеризации из phase 1 и только его именуем через LLM.

## Шаблон setup-folder

```
phase2_toggles/
  setup_A/
    description.md          # какое (LLM, embedder, method, param) и почему
    00_baseline/config.yaml
    01_coref_on/config.yaml
    02_norm_off/config.yaml
    03_naming_on/config.yaml
  setup_B/
    ... то же самое
```

## Шаблоны config.yaml

### `00_baseline` / `01_coref_on` / `02_norm_off`

`multi_method: true` сохраняем (получаем сразу свежий sweep после изменения toggle).

```yaml
llm:
  # ... (скопировать из phase1b/exp_l<N>/config.yaml)

embedding:
  model_name: "<E*>"   # лучший embedder из phase 1a
  device: "cuda"

coreference:
  enabled: false        # для 01_coref_on → true
  prompt_file: "prompts/coreference_ru.txt"
  context_sentences: 3
  window_sentences: 5

extraction:
  prompt_file: "prompts/extraction_ru.txt"
  chunk_size: 3
  overlap_size: 1

normalization:
  enabled: true         # для 02_norm_off → false
  language: "ru"

deduplication:
  enabled: true
  threshold: 0.92

clustering:
  multi_method: true
  cluster_relations: true
  include_embeddings: false
  threshold_min: 0.25
  threshold_max: 0.9
  threshold_steps: 10
  k_min: 10
  k_max: 60
  k_step: 15
  hdbscan_min_cluster_sizes: [3, 5, 10]
  hdbscan_min_samples: [1, 3, 5]
  cluster_naming_prompt: "prompts/cluster_naming_ru.txt"
  llm_naming: false

paths:
  input_text: "../benchmark/final_bench/formated_fragment2.md"
  output_dir: "output"
```

### `03_naming_on` (single-method, фиксируем лучший вариант)

```yaml
# ... llm/embedding/coreference/extraction/normalization/deduplication как в baseline

clustering:
  multi_method: false
  method: "agglomerative"          # ← из phase 1: best_method
  threshold: 0.55                  # ← из phase 1: best_param (если agglomerative)
  # n_clusters: 24                 # ← вместо threshold, если best_method=kmeans
  # min_cluster_size: 5            # ← если best_method=hdbscan
  # min_samples: 3                 # ← если best_method=hdbscan
  cluster_relations: true
  include_embeddings: false
  cluster_naming_prompt: "prompts/cluster_naming_ru.txt"
  llm_naming: true                 # ← главное отличие

paths:
  input_text: "../benchmark/final_bench/formated_fragment2.md"
  output_dir: "output"
```
