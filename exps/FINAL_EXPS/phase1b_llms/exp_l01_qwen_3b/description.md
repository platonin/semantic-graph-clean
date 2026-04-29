# exp_l01_qwen_3b

**Phase:** 1b — LLMs sweep
**Variable:** LLM = `Qwen/Qwen2.5-3B-Instruct` (local, cuda, bf16)
**Fixed:** embedder=`BAAI/bge-m3` (placeholder — заменить на E* после phase 1a), coref=off, norm=on, multi_method, llm_naming=off

**Hypothesis:** младший Qwen, нижняя граница качества. Скорее всего слабее извлечёт триплеты — отдельный edge-recall просядет.
