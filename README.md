# 🎯 CV-Agents — Sistema Inteligente de Adaptação de Currículos com IA & ATS

Agente autônomo, agnóstico e universal para processar oportunidades de qualquer plataforma de emprego, gerenciar pacotes autônomos de candidatura, adaptar currículos com base factual e gerar PDFs oficiais de alta fidelidade.

---

## 🏛️ Arquitetura de Dados: Pacotes Autônomos em `applications/`

Toda oportunidade enviada ao comando `/new-opportunity` é armazenada em uma pasta própria e isolada:

```text
c:\Projects\cv-agents\applications\2026-11_empresa_cargo\
├── job-description.md       # 📥 Texto bruto da vaga (preserva o histórico original)
├── company-context.md       # 🏢 Contexto da empresa (produtos, nicho, notas do usuário)
├── screening-questions.md   # ❓ Perguntas do formulário respondidas no modelo STAR
├── resume.html              # 🌐 Código semântico do currículo adaptado
├── Curriculo_<Nome>.pdf     # 📄 PDF final A4 pronto para envio (padrão oficial)
├── ats-audit.md             # 📊 Auditoria ATS e análise de gaps
└── pitch-linkedin.md        # 💬 Mensagem de abordagem personalizada para o recrutador
```

### Inteligência Cumulativa nos Índices Centrais:
- **[`career-knowledge.md`](career-knowledge.md):** Fonte única da verdade da carreira (zero alucinação).
- **[`applications-tracker.md`](applications-tracker.md):** Painel geral de status de todas as candidaturas.
- **[`questions-bank.md`](questions-bank.md):** Banco de perguntas frequentes de processos seletivos e respostas reutilizáveis, garantindo aprendizado contínuo do agente.

---

## ⚡ Como Acionar: `/new-opportunity`

```text
/new-opportunity
```

### Formas de envio no Chat:
1. **Comando simples:** Digite `/new-opportunity` e o agente solicitará a vaga, contexto e perguntas.
2. **Envio completo:** Digite `/new-opportunity` e envie junto:
   - A descrição da vaga.
   - O contexto da empresa ou notas extras (opcional).
   - As perguntas do formulário de inscrição (opcional).

O agente processará tudo de forma contínua e devolverá o kit completo em `applications/` com o PDF compilado!

---

## 📁 Estrutura Completa do Projeto

```text
c:\Projects\cv-agents\
├── career-knowledge.md                 # 🧠 ÚNICA FONTE DA VERDADE (dados 100% verificados)
├── applications-tracker.md             # 📋 Rastreador geral de candidaturas
├── questions-bank.md                   # ❓ Banco central de perguntas de formulários/entrevistas
├── README.md                           # Documentação deste projeto
├── docs/
│   └── ai-ats-screening-guide.md       # Guia de funcionamento de robôs de ATS e IA
├── templates/
│   ├── CV_English_Lucas_Camargo_QA.pdf # PDF de referência visual padrão oficial
│   ├── resume-template-en.html         # Template HTML oficial com placeholders dinâmicos (Inglês)
│   └── resume-template-pt.html         # Template HTML oficial com placeholders dinâmicos (Português)
├── scripts/
│   ├── generate_pdf.py                 # Script CLI de renderização HTML -> PDF via Chromium
│   └── ats_scorer.py                   # Avaliador de score ATS e compatibilidade com IA
├── jobs/                               # Onde você pode salvar vagas em arquivo .txt
└── applications/                       # 📦 Onde ficam os pacotes autônomos de cada vaga
```
