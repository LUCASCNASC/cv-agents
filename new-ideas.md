# 💡 Backlog de Ideias & Evolução do Sistema

---

## ✅ Funcionalidades Concluídas

### 1. 🤖 Agente e Comando `/company-report` (CONCLUÍDO)
- [x] **Relatório Pré-Entrevista Padronizado:** Gera dossiê executivo sobre a empresa antes da entrevista sem gastar tokens desnecessários, injetando dados em template HTML/CSS fixo ([`templates/company-report-template.html`](templates/company-report-template.html)) e compilando para PDF A4 via Chromium.
- [x] **Conexão Playwright MCP & Scripts:** Configurado servidor em [`.vscode/mcp.json`](.vscode/mcp.json) e crawler em [`scripts/extract_company_info.py`](scripts/extract_company_info.py) para extração automatizada de sites corporativos.
- [x] **Acionamento Manual por URL:** Aceita a URL diretamente no chat: `/company-report https://site-da-empresa.com`.
- [x] **Extração de Informações Cruciais para a Entrevista:**
  - Visão geral, missão e proposta de valor.
  - História da empresa e marcos fundamentais.
  - Momento atual (crescimento, notícias, rodadas, expansões).
  - Produtos e soluções core.
  - Como trabalham com IA e tecnologia.
  - Principais parceiros e clientes.
  - Liderança (C-level, fundadores) e porte da equipe.
  - Perguntas e dicas estratégicas para fazer ao entrevistador.
- [x] **Tratamento & Injeção de Dados:** Conteúdo saneado e estruturado sem ruídos de scraping antes de compilar o relatório.
- [x] **Pasta Centralizada `reports/<empresa>/`:** Cada execução cria automaticamente uma subpasta dedicada da empresa dentro de `reports/`, salvando `company-report.html`, `company-report.md` e `company-report.pdf`.

---

### 2. 🎯 Integração com o Agente `/new-opportunity` (CONCLUÍDO)
- [x] **Armazenamento Integrado em `reports/<empresa>/`:** O currículo oficial em PDF e todos os artefatos gerados pelo `/new-opportunity` agora são salvos na pasta da respectiva empresa criada pelo `/company-report`.
- [x] **Consumo Profundo de Contexto Prévio:** Se o `/company-report` já tiver sido gerado, o `/new-opportunity` lê `reports/<empresa>/company-report.md` para:
  - Alinhar o Resumo Profissional à indústria e momento técnico da empresa.
  - Priorizar e ordenar bullets de experiência que respondem às dores e tecnologias apuradas.
  - Hiperpersonalizar a mensagem de abordagem no LinkedIn (`pitch-linkedin.md`).
  - Responder perguntas culturais e de valores da empresa no formulário (`screening-questions.md`).
  - Gerar dossiê de preparação cruzando cases STAR com as potenciais perguntas (`interview-prep.md`).

---

### 3. 🔄 Alinhamento do Fluxo em 2 Passos (CONCLUÍDO)
- [x] **Passo 1:** Executar `/company-report <URL>` para criar a pasta da empresa e gerar o dossiê institucional.
- [x] **Passo 2:** Executar `/new-opportunity <vaga>` para gerar o currículo personalizado em PDF dentro da pasta daquela empresa.
- [x] **Documentação no README:** Diagrama do fluxo e passo a passo detalhado documentados no [`README.md`](README.md).
- [x] **Segurança e `.gitignore`:** Pasta `reports/` adicionada ao [`.gitignore`](.gitignore) e documentada a localização correta na raiz (`c:\Projects\cv-agents\reports\`).

---

### 4. 🧠 Sistema de Contexto e Memória de Longo Prazo (CONCLUÍDO)
- [x] **Instrução Mestre Permanente (`AGENTS.md`):** Criado [`AGENTS.md`](AGENTS.md) na raiz do projeto, carregado automaticamente pelo Antigravity em qualquer sessão/chat para garantir que o agente nunca perca o contexto histórico.
- [x] **Pasta `memory/`:**
  - [`memory/interview-learnings.md`](memory/interview-learnings.md): Acúmulo de perguntas reais feitas em entrevistas, feedbacks e pontos fortes.
  - [`memory/salary-and-negotiations.md`](memory/salary-and-negotiations.md): Histórico de faixas salariais (BRL/USD) e ofertas recebidas.
  - [`memory/target-preferences.md`](memory/target-preferences.md): Preferências de carreira, stacks alvo (Playwright, IA) e modelos de trabalho (100% remoto).
- [x] **Banco de Questões Cumulativo (`questions-bank.md`):** Registro de perguntas frequentes de formulários com respostas no modelo STAR.
- [x] **Painel de Candidaturas (`applications-tracker.md`):** Rastreamento de todas as vagas, datas, scores e status de processos.

---

### 5. 🌐 Padronização Universal & Triagem por IA (CONCLUÍDO)
- [x] **Fonte Única da Verdade (`career-knowledge.md`):** Informações do candidato vêm exclusivamente deste arquivo (zero alucinação, 100% factual e bilíngue).
- [x] **Modelo Visual Padrão:** Layout e tipografia idênticos ao [`templates/CV_English_Lucas_Camargo_QA.pdf`](templates/CV_English_Lucas_Camargo_QA.pdf).
- [x] **Guia Técnico de IA & ATS:** Criado [`docs/ai-ats-screening-guide.md`](docs/ai-ats-screening-guide.md) e auditor de score [`scripts/ats_scorer.py`](scripts/ats_scorer.py).

---

## 🔮 Próximas Ideias & Melhorias Futuras (Backlog Aberto)
- [ ] **Simulador de Entrevista (Mock Interviewer):** Modo interativo onde o agente assume a persona do Tech Recruiter ou Engineering Manager da empresa-alvo e faz perguntas técnicas e comportamentais baseadas no `company-report.md`.
- [ ] **Gerador de Mensagens de Follow-up & Cold Mail:** Templates automatizados de mensagens de acompanhamento após 7, 14 e 21 dias da aplicação ou entrevista.
- [ ] **Extensão / Script de Auto-Fill para Gupy / Workday:** Auxiliar no preenchimento de formulários longos utilizando as respostas armazenadas no `questions-bank.md`.
- [ ] **Dashboard Local / CLI Interativo:** Script em Python simples (ex: via `rich` ou `typer`) para listar candidaturas abertas e status de processos diretamente no terminal.


- melhorar a geração de currículo com base nos padrões de análise de currúculo feita por IAs. Geralmente essa primeira etapa, primeiro filtro, é feito por IA, onde eles excluem candidatos sem análise humana, com base no que a vaga pede. Precisamos entender mais a lógica dessas IAs. Pra isso, pensei em utilizar o NotebookGemini, onde ele vai buscar fontes confiáveis sobre o assunto.

Definição de regras:
- quando temos mais de uma vaga da mesma empresa que vamos aplicar, utilizar o mesmo relatório gerado da companhia, mas currículos diferentes, caso as descrições das vagas sejam diferentes, pois alguamas empresas podem abrir mais de uma vaga igual.
- quando aplicamos para uma empresa e um pouco depois elas abrem uma outra vaga, já temos o relatório dela gerado, precisamos definir por quando tempo esse relatório permanece válido e a partir de quanto tempo temos que gerar um novo. Talvez seja um boa inserir a data de geração do relatório dentro do próriio, para termos controle.
