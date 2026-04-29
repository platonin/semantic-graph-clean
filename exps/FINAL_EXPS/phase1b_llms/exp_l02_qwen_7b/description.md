# exp_l02_qwen_7b

**Phase:** 1b — LLMs sweep
**Variable:** LLM = `Qwen/Qwen2.5-7B-Instruct` (local, cuda, bf16)
**Fixed:** embedder=`BAAI/bge-m3` (placeholder), coref=off, norm=on, multi_method, llm_naming=off

**Hypothesis:** Qwen middle. Точка scaling-кривой между 3B и 14B.
