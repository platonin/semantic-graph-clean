# exp_e5_rosberta

**Phase:** 1a — embedders sweep
**Variable:** embedder = `ai-forever/ru-en-RoSBERTa`
**Fixed:** LLM=`deepseek-v32/latest` (API), coref=off, norm=on, multi_method clustering, llm_naming=off

**Hypothesis:** RU/EN bilingual fine-tune, должен лучше держать русскую морфологию и научную терминологию. Может выстрелить на специфичной лексике.
