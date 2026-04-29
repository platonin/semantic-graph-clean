# exp_e1_mpnet_en

**Phase:** 1a — embedders sweep
**Variable:** embedder = `sentence-transformers/all-mpnet-base-v2`
**Fixed:** LLM=`deepseek-v32/latest` (API), coref=off, norm=on, multi_method clustering, llm_naming=off

**Hypothesis:** EN-only baseline. Ожидаем просадку на русском тексте — служит нижней границей для остальных эмбеддеров.
