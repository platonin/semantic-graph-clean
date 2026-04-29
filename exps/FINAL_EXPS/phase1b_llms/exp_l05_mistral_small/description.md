# exp_l05_mistral_small

**Phase:** 1b — LLMs sweep
**Variable:** LLM = `mistralai/Mistral-Small-Instruct-2409` (~22B, local, cuda, **8-bit**)
**Fixed:** embedder=`BAAI/bge-m3` (placeholder), coref=off, norm=on, multi_method, llm_naming=off

**Hypothesis:** старший локальный без 32B, должен брать качеством. Весит ~22B → грузим в 8-bit, чтобы влез в 24GB+.
