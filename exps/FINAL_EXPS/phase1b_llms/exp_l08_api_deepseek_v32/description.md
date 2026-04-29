# exp_l08_api_deepseek_v32

**Phase:** 1b — LLMs sweep
**Variable:** LLM = `deepseek-v32/latest` (Yandex Cloud API)
**Fixed:** embedder=`BAAI/bge-m3` (placeholder), coref=off, norm=on, multi_method, llm_naming=off

**Hypothesis:** ожидаемый чемпион. Дублирует phase 1a с E*=bge-m3 — если E* совпадёт, можно переиспользовать результат и не пересчитывать.
