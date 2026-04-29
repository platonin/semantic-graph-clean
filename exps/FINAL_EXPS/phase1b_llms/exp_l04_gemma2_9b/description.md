# exp_l04_gemma2_9b

**Phase:** 1b — LLMs sweep
**Variable:** LLM = `google/gemma-2-9b-it` (local, cuda, bf16)
**Fixed:** embedder=`BAAI/bge-m3` (placeholder), coref=off, norm=on, multi_method, llm_naming=off

**Hypothesis:** сильный 9B, хорошо работает с инструкциями. Альтернатива Qwen-семейству на близком масштабе.
