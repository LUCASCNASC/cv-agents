---
name: new-opportunity
description: Passo 2 do fluxo. Adapta o currículo com base na vaga informada e no contexto estratégico gerado pelo /company-report (salvo em reports/<empresa>/company-report.md), compilando o currículo final em PDF e o kit completo de candidatura diretamente dentro de reports/<empresa>/.
---

# Fluxo de Candidatura: New Opportunity (`/new-opportunity`)

Este comando é o **Passo 2** do fluxo estratégico de candidaturas. Ele consome o contexto de inteligência gerado no **Passo 1 (`/company-report`)**, cruza com os dados factuais do candidato ([`career-knowledge.md`](../../../career-knowledge.md)) e gera um kit de candidatura cirúrgico dentro de **`reports/<empresa>/`**.

---

## 🚀 Como Acionar

No chat, envie o comando com a descrição da vaga (ou apontando para o arquivo):

```text
/new-opportunity [cole a descrição da vaga aqui]
```
ou informando a empresa e a vaga:
```text
/new-opportunity empresa: "NomeEmpresa" [descrição da vaga]
```

---

## 🧠 Protocolo de Utilização do Contexto do `company-report`

Quando o `/new-opportunity` é executado, o agente deve seguir **obrigatoriamente** as seguintes etapas de contextualização:

### Etapa 1: Localização & Carregamento do `company-report.md`
1. O agente identifica o nome da empresa na descrição da vaga ou parâmetro e normaliza o nome da pasta (ex: `stone`, `cora`, `nubank`).
2. Verifica se o arquivo `reports/<empresa>/company-report.md` já existe.
   - **Se existir (Cenário Ideal):** Lê o arquivo integralmente e carrega as seguintes variáveis-chave:
     - *Proposta de Valor & Produtos Core*
     - *Momento Atual & Desafios de Negócio (expansão, escala, confiabilidade)*
     - *Como a empresa trabalha com IA e Engenharia*
     - *Cultura, Valores e Liderança*
     - *Perguntas Estratégicas geradas para a Entrevista*
   - **Se NÃO existir:** Notifica o usuário: *"Não encontrei o relatório prévio da empresa. Recomendo rodar `/company-report <URL>` primeiro para gerar a inteligência estratégica da empresa. Deseja pausar para rodar o relatório ou prosseguir apenas com a descrição da vaga?"*

---

### Etapa 2: A Matriz de Cruzamento Estratégico (Onde o Contexto é Injetado)

O contexto do `company-report` é injetado diretamente em **5 áreas fundamentais** da candidatura:

| Seção do Entregável | Como o `company-report` é Utilizado | Regra de Zero Alucinação |
|---|---|---|
| **1. Resumo Profissional (`Professional Summary`)** | O resumo do currículo é calibrado para citar a indústria da empresa (Fintech, Healthtech, SaaS, etc.) e como a especialidade do candidato resolve os desafios de escala, qualidade ou IA identificados no relatório da empresa. | Usa **somente** títulos, anos de experiência e competências reais comprovadas em `career-knowledge.md`. |
| **2. Priorização de Bullets de Experiência** | Os bullets de realizações são reordenados para dar destaque àqueles que resolvem as dores e espelham a stack citada no `company-report` (ex: se a empresa foca em microsserviços, APIs e automação com Playwright/Python, os bullets dessas conquistas aparecem no topo de cada experiência). | **Nunca** altera números, métricas ou cria projetos que não existam em `career-knowledge.md`. |
| **3. Pitch de Abordagem para LinkedIn (`pitch-linkedin.md`)** | O pitch menciona explicitamente o momento atual ou produtos destacados no `company-report` (ex: *"Acompanho a evolução da [Empresa] em [Produto X] e o foco de vocês em [Inovação/Escala]..."*), gerando conexão imediata com o Tech Recruiter ou Hiring Manager. | Conecta o momento real da empresa com a experiência real do candidato. |
| **4. Respostas de Formulário (`screening-questions.md`)** | Questões clássicas como *"Por que você quer trabalhar na [Empresa]?"* ou *"Como você se conecta com nossos valores?"* são respondidas cruzando a missão/valores catalogados no relatório com a trajetória real do candidato. | Respostas estruturadas no método STAR, salvas também em `questions-bank.md`. |
| **5. Dossiê de Alinhamento para Entrevista (`interview-prep.md`)** | Cria uma folha rápida conectando as perguntas sugeridas no `company-report` com os 5 Desafios STAR do candidato de `career-knowledge.md`. | Fornece ao candidato os melhores exemplos prontos para cada potencial pergunta. |

---

## 📦 Artefatos Gerados em `reports/<empresa>/`

Ao término da execução, todos os entregáveis do `/new-opportunity` ficam centralizados na pasta da empresa:

```text
reports/<empresa>/
├── company-report.html         # Dossiê institucional visual (Passo 1)
├── company-report.md           # Dossiê estruturado em markdown (Passo 1)
├── company-report.pdf          # PDF do dossiê para leitura rápida (Passo 1)
│
├── Curriculo_<Nome>_<Vaga>.pdf # ✅ Currículo oficial A4 pronto para envio (Passo 2)
├── resume.html                 # Código-fonte semântico do currículo
├── job-description.md          # Descrição integral da vaga guardada
├── pitch-linkedin.md           # Mensagem cirúrgica para o recrutador
├── screening-questions.md       # Respostas inteligentes a perguntas da vaga
├── interview-prep.md           # Cruzamento de cases STAR com as dores da empresa
└── ats-audit.md                # Relatório de pontuação ATS e palavras-chave
```

---

## 📋 Atualização Automática de Status

Após a compilação do PDF:
1. Registra a vaga no [`applications-tracker.md`](../../../applications-tracker.md) com status `Pronto para Envio` e link para o PDF gerado.
2. Salva novas respostas formuladas em [`questions-bank.md`](../../../questions-bank.md).
