# 🧠 AGENTS.md — Memória & Diretrizes de Longo Prazo do CV-Agents

> **Para qualquer Agente Antigravity:** Este arquivo é carregado automaticamente na inicialização de qualquer sessão neste projeto. Ele constitui a **Memória Permanente e as Regras Operacionais de Longo Prazo** do ecossistema `cv-agents`.

---

## 🎯 1. Identidade & Missão do Projeto
O `cv-agents` é um ecossistema inteligente, agnóstico e permanente para:
1. **Inteligência de Mercado (`/company-report`):** Pesquisar e estruturar dossiês estratégicos de empresas pré-entrevista via Playwright.
2. **Candidaturas Cirúrgicas (`/new-opportunity`):** Adaptar currículos em PDF de alta compatibilidade ATS/IA, responder formulários de triagem e gerar pitches para LinkedIn.
3. **Memória de Longo Prazo:** Rastrear processos seletivos, acumular respostas de formulários e reter aprendizados de entrevistas ao longo de meses e anos.

---

## 🗺️ 2. Mapa da Memória Permanente (Onde Buscar Informações)

Sempre que uma nova mensagem for recebida, o agente deve consultar estes arquivos para recuperar o contexto histórico antes de responder:

| Arquivo de Memória | Propósito & Conteúdo | Quando Consultar |
|---|---|---|
| **[`career-knowledge.md`](career-knowledge.md)** | **Fonte Única da Verdade (SSOT):** Dados factuais, histórico profissional, números, métricas (24x vendas, 50% redução de tempo) e competências do candidato. | **Sempre** que gerar currículos, resumos ou respostas técnicas. |
| **[`applications-tracker.md`](applications-tracker.md)** | **Painel Geral de Candidaturas:** Histórico de todas as empresas já abordadas, datas, scores e status de processos. | Para checar se o usuário já aplicou para aquela empresa anteriormente ou consultar status. |
| **[`questions-bank.md`](questions-bank.md)** | **Banco de Inteligência de Questões:** Respostas no modelo STAR acumuladas ao longo de dezenas de candidaturas. | Para reaproveitar e refinar respostas de formulários e entrevistas. |
| **[`reports/<empresa>/`](reports/)** | **Dossiês & Currículos Gerados:** Histórico isolado de cada empresa, incluindo relatório pré-entrevista, vaga na íntegra e currículo enviado. | Antes de gerar uma nova versão para a mesma empresa ou para preparar o usuário para uma entrevista. |
| **[`memory/interview-learnings.md`](memory/interview-learnings.md)** | **Aprendizados de Entrevistas:** Feedbacks recebidos, perguntas difíceis feitas por entrevistadores e pontos fortes. | Para ajustar o pitch e preparar respostas cada vez mais afiadas. |
| **[`memory/salary-and-negotiations.md`](memory/salary-and-negotiations.md)** | **Histórico de Remuneração:** Faixas salariais informadas por recrutadores (BRL/USD) e pretensões do candidato. | Para apoiar respostas sobre pretensão salarial e negociação. |
| **[`memory/target-preferences.md`](memory/target-preferences.md)** | **Preferências de Carreira:** Tipos de empresa desejados, modelo de trabalho (remoto, fuso), stacks prioritárias. | Para orientar a tomada de decisão do agente ao ranquear oportunidades. |

---

## ⚖️ 3. Regras Inegociáveis do Sistema

1. **Zero Alucinação Factual:** O agente NUNCA inventa empresas, ferramentas, datas, certificações ou números de impacto que não constem em `career-knowledge.md`.
2. **Padrão Visual Estrito:** Todos os currículos gerados devem seguir o modelo minimalista, sem serifa, de alta pontuação ATS de [`templates/CV_English_Lucas_Camargo_QA.pdf`](templates/CV_English_Lucas_Camargo_QA.pdf).
3. **Economia de Tokens:** Relatórios de empresa utilizam o template estruturado [`templates/company-report-template.html`](templates/company-report-template.html), evitando reescrever CSS/HTML no chat.
4. **Resiliência e Celeridade:** Consultas web e LinkedIn são bônus (*best-effort*). Se a página for inacessível ou privada, o agente avança imediatamente com os dados fornecidos na vaga.
5. **Aprendizado Contínuo:** Sempre que uma nova resposta brilhante for elaborada para uma candidatura, o agente deve catalogá-la em `questions-bank.md` para benefício de candidaturas futuras.

---

## 🔄 4. Os Dois Fluxos Oficiais Integrados & Sinergia de Contexto

```text
Passo 1: /company-report <URL> ───► Gera dossiê e cria reports/<empresa>/company-report.md
                                             │
                                             ▼ (Injeção de Contexto Estratégico)
Passo 2: /new-opportunity <Vaga> ──► Absorve o company-report.md + career-knowledge.md
                                     └──► Gera currículo em PDF + kit dentro de reports/<empresa>/
```

### 🎯 Como o contexto do `company-report` alimenta o `new-opportunity`:
1. **Resumo Profissional Alinhado:** Conecta a especialidade do candidato com a indústria, proposta de valor e momento técnico da empresa descobertos no relatório.
2. **Priorização de Bullets:** Dá maior destaque às realizações reais de `career-knowledge.md` que resolvem diretamente os desafios de engenharia e tecnologia da empresa.
3. **Pitch de Abordagem para Recrutadores (`pitch-linkedin.md`):** Cita os produtos e marcos reais da empresa apurados no dossiê, gerando um contato hiperpersonalizado.
4. **Respostas a Questões Culturais e de Negócio (`screening-questions.md`):** Cruza a missão e valores da empresa com a história e casos STAR do candidato.
5. **Preparação de Entrevista (`interview-prep.md`):** Mapeia os 5 desafios STAR do candidato contra as dores e perguntas sugeridas no relatório da empresa.
