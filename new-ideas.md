# 💡 Backlog de Ideias & Evolução do Sistema

- [x] **Site institucional da empresa (CONCLUÍDO):**
  - Implementado na Fase 2 da skill `/new-opportunity`.
  - O agente busca produtos, missão, modelo de negócio (B2B, SaaS, Fintech, InsurTech) e bandeiras culturais da empresa contratante para permear o resumo e a carta/pitch de apresentação.

- [x] **Perfil no LinkedIn & Equipe (CONCLUÍDO):**
  - Implementado na Fase 2 da skill `/new-opportunity`.
  - O agente busca perfis e sinais de liderança técnica (Head of QA, Engineering Managers, Tech Leads) para identificar tom, ênfases metodológicas e stack preferida da equipe.

- [x] **Máximo de informações possíveis sobre a vaga e contexto (CONCLUÍDO):**
  - O fluxo agora cruza a descrição formal da vaga + dados institucionais da empresa + inteligência de liderança no LinkedIn, gerando um pacote completo de candidatura (Currículo A4 + Pitch para LinkedIn + Relatório de Auditoria ATS).

- [x] **Otimização para Triagem por IA & ATS (CONCLUÍDO):**
  - Criado o guia aprofundado [`docs/ai-ats-screening-guide.md`](docs/ai-ats-screening-guide.md) explicando como funcionam os parsers de ATS (Workday, Greenhouse, Lever, Gupy) e os agentes avaliadores por LLM (embeddings vetoriais, princípio STAR, verificação de métricas).
  - Desenvolvido o script de auditoria e cálculo de score ATS [`scripts/ats_scorer.py`](scripts/ats_scorer.py) para auditar automaticamente o currículo gerado contra a vaga.

- [x] **Padronização Universal do Agente (CONCLUÍDO):**
  - Informações de carreira extraídas **exclusivamente** do arquivo centralizado [`career-knowledge.md`](career-knowledge.md).
  - O agente e os templates são **100% universais**: funcionam para qualquer pessoa simplesmente alterando o arquivo `career-knowledge.md`.
