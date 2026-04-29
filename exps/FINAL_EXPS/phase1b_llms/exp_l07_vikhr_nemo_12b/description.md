# exp_l07_vikhr_nemo_12b

**Phase:** 1b — LLMs sweep
**Variable:** LLM = `Vikhrmodels/Vikhr-Nemo-12B-Instruct-R-21-09-24` (local, cuda, bf16)
**Fixed:** embedder=`BAAI/bge-m3` (placeholder), coref=off, norm=on, multi_method, llm_naming=off

**Hypothesis:** RU-fine-tuned Mistral-Nemo. Может выстрелить за счёт лучшей русской токенизации/инструкций.
