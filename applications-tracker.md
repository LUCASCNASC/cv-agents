# 📋 Rastreador de Candidaturas (Application Tracker)

Este arquivo registra automaticamente todas as oportunidades processadas pelo comando `/new-opportunity`. Cada candidatura possui seu **Pacote Autônomo** armazenado dentro de `applications/<data>_<empresa>_<cargo>/`.

---

## Histórico de Oportunidades

| Data | Empresa | Cargo | Plataforma | Idioma | Score ATS | Pacote Completo & PDF | Status | Notas / Próximo Passo |
|---|---|---|---|---|---|---|---|---|
| 20/11/2026 | Global InsurTech | Senior QA Engineer | Greenhouse / Site | EN | 96/100 | [Ver Pasta & PDF](applications/2026-11_global-insurtech_senior-qa/Resume_Lucas_Camargo_Senior_QA.pdf) | Pronto para Envio | Perguntas salvas; foco em Playwright POM e MCPs |
| 20/11/2026 | Fintech Inovadora | QA Engineer Sênior | Gupy / Brasil | PT | 97/100 | [Ver Pasta & PDF](output/fintech-qa-senior-pt/Curriculo_Lucas_Camargo_QA_Senior.pdf) | Pronto para Envio | Foco em APIs governamentais, k6 e consignado CLT |

---

## 📂 O Que Contém na Pasta de Cada Candidatura (`applications/`)
- `job-description.md` — Texto integral e original da vaga.
- `company-context.md` — Contexto da empresa, nicho, modelo de negócio e notas enviadas.
- `screening-questions.md` — Perguntas do formulário e respostas personalizadas para aquela vaga.
- `resume.html` & `Curriculo_<Nome>.pdf` — Código semântico e PDF oficial A4.
- `ats-audit.md` — Auditoria de pontuação ATS e análise de gaps.
- `pitch-linkedin.md` — Mensagem pronta para abordagem ao Tech Recruiter ou Hiring Manager.

---

## 🏷️ Legenda de Status
- `Pronto para Envio`: Currículo, perguntas e pitch gerados.
- `Aplicado`: Candidatura submetida na plataforma.
- `Contato Feito`: Pitch enviado no LinkedIn para Tech Recruiter ou Hiring Manager.
- `Entrevista RH`: Primeira fase em andamento.
- `Entrevista Técnica`: Desafio prático ou conversa técnica agendada.
- `Oferta`: Proposta recebida.
- `Arquivado`: Processo finalizado.
