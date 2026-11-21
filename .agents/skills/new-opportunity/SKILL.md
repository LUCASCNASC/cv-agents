---
name: new-opportunity
description: Fluxo inteligente de candidatura completa. Aceita vagas de qualquer plataforma, contexto da empresa e perguntas de formulário. Cria pacote autônomo em applications/, adapta o currículo em PDF (padrão CV_English_Lucas_Camargo_QA.pdf), responde screening questions e indexa no questions-bank.md.
---

# Fluxo de Candidatura Completa: New Opportunity (`/new-opportunity`)

Este comando inicia o agente de candidaturas completas. O sistema opera de forma **100% universal e agnóstica ao candidato**, alimentando-se exclusivamente do arquivo [`career-knowledge.md`](../../../career-knowledge.md).

---

## 🎯 Arquitetura de Dados & Armazenamento

Para cada oportunidade processada, o agente cria automaticamente uma pasta dedicada:
`applications/<YYYY-MM>_<empresa>_<cargo>/`

Dentro dela, armazena o **Pacote Autônomo da Candidatura**:
1. `job-description.md` — Texto bruto da vaga, preservando o histórico integral.
2. `company-context.md` — Contexto da empresa (produtos, nicho, notas informadas pelo usuário ou coletadas de forma opcional/best-effort).
3. `screening-questions.md` — Perguntas do formulário de inscrição respondidas de forma personalizada no modelo STAR.
4. `resume.html` e `Curriculo_<Nome>.pdf` — Currículo oficial A4 fiel a `templates/CV_English_Lucas_Camargo_QA.pdf`.
5. `ats-audit.md` — Auditoria de score ATS e gap analysis.
6. `pitch-linkedin.md` — Mensagem de abordagem personalizada para o recrutador.

Além disso, o agente atualiza automaticamente os dois índices centrais:
- [`applications-tracker.md`](../../../applications-tracker.md) — Registra a candidatura na tabela geral.
- [`questions-bank.md`](../../../questions-bank.md) — Indexa novas respostas para aprendizado contínuo.

---

## 🚀 Fases de Execução Passo a Passo

### Fase 1: Recepção Universal de Dados
O usuário pode enviar em uma única mensagem ou em etapas:
- **Texto da Vaga:** De qualquer plataforma (LinkedIn, Gupy, Greenhouse, Lever, Workday, etc.).
- **Contexto da Empresa (Opcional):** Notas sobre produtos, cultura, notícias ou links.
- **Perguntas de Inscrição (Opcional):** Perguntas abertas do formulário (ex: *"Conte sobre um desafio técnico"*, *"Por que você quer trabalhar aqui?"*).

Se o usuário enviar apenas `/new-opportunity`, o agente solicita os dados disponíveis.

---

### Fase 2: Enriquecimento & Criação da Pasta
1. Cria a pasta `applications/<YYYY-MM>_<empresa>_<cargo>/`.
2. Salva o texto bruto em `job-description.md`.
3. Salva os detalhes institucionais em `company-context.md` (se o usuário informou notas ou se o agente encontrou dados públicos via pesquisa web rápida não bloqueante).

---

### Fase 3: Consulta Factual & Resposta às Perguntas de Inscrição
1. Consulta `career-knowledge.md` e `questions-bank.md`.
2. Se houver perguntas de formulário informadas:
   - Responde cada questão conectando o histórico factual do candidato às dores e ao negócio da empresa.
   - Salva em `screening-questions.md`.
   - Adiciona a melhor versão no `questions-bank.md` para reaproveitamento futuro.

---

### Fase 4: Adaptação Semântica do Currículo
- Título alinhado à vaga.
- Resumo cirúrgico conectando as maiores conquistas do candidato à dor da empresa.
- Reordenação de `TECHNICAL SKILLS` destacando as ferramentas obrigatórias.
- Bullets de experiência priorizados por relevância e métricas quantificadas (STAR).
- Fuso horário (`UTC-3 · Overlap with US EST/PST`) para posições internacionais.

---

### Fase 5: Compilação do PDF
Injeta no template correspondente (`resume-template-pt.html` ou `resume-template-en.html`) e executa:
```powershell
python scripts/generate_pdf.py "applications/<pasta>/resume.html" "applications/<pasta>/Curriculo_<Nome>.pdf"
```

---

### Fase 6: Auditoria ATS, Pitch & Rastreamento
1. Executa `scripts/ats_scorer.py` e salva em `ats-audit.md`.
2. Gera `pitch-linkedin.md` com mensagem curta para conectar com recrutadores no LinkedIn.
3. Adiciona uma nova linha com status e links em `applications-tracker.md`.

---

### Fase 7: Devolução Imediata no Chat
O agente apresenta no chat:
- 🎯 **Score ATS e Análise de Gaps**.
- ❓ **Resumo das Respostas de Formulário** (se houver perguntas).
- 💬 **Pitch para LinkedIn**.
- 📄 **Links Clicáveis:**
  - PDF: `[Curriculo_<Nome>.pdf](file:///c:/Projects/cv-agents/applications/<pasta>/Curriculo_<Nome>.pdf)`
  - Pasta da Candidatura: `[Ver Arquivos da Vaga](file:///c:/Projects/cv-agents/applications/<pasta>/)`
  - Rastreador Geral: `[applications-tracker.md](file:///c:/Projects/cv-agents/applications-tracker.md)`
