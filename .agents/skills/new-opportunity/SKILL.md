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

### Etapa 1: Localização, Carregamento & Checagem de Validade (TTL) do `company-report.md`
1. O agente identifica o nome da empresa na descrição da vaga ou parâmetro e normaliza o nome da pasta (ex: `stone`, `cora`, `nubank`).
2. Verifica se o arquivo `reports/<empresa>/company-report.md` já existe:
   - **Se NÃO existir:** Notifica o usuário: *"Não encontrei o relatório prévio da empresa. Recomendo rodar `/company-report <URL>` primeiro para gerar a inteligência estratégica da empresa. Deseja pausar para rodar o relatório ou prosseguir apenas com a descrição da vaga?"*
   - **Se existir:** Avalia o frescor do relatório através do metadado `generated_at`:
     - **0 a 60 dias:** Status **Fresco/Válido**. O agente utiliza os dados imediatamente sem necessidade de reprocessamento.
     - **61 a 90 dias:** Status **Atenção**. O agente utiliza os dados existentes, mas emite um aviso no chat: *"O relatório da empresa foi gerado há X dias e continua válido, mas pode ter novidades recentes."*
     - **Acima de 90 dias:** Status **Expirado**. O agente alerta: *"O relatório desta empresa foi gerado há X dias (> 90 dias) e expirou. Recomendo rodar `/company-report <URL>` para atualizar produtos e liderança antes de gerar o currículo. Deseja atualizar agora ou prosseguir com o dossiê atual?"*
3. Carrega as variáveis-chave do dossiê:
   - *Proposta de Valor & Produtos Core*
   - *Momento Atual & Desafios de Negócio (expansão, escala, confiabilidade)*
   - *Como a empresa trabalha com IA e Engenharia*
   - *Cultura, Valores e Liderança*
   - *Perguntas Estratégicas geradas para a Entrevista*

---

### Etapa 1.5: Gestão de Múltiplas Vagas & Detecção de Duplicidade
Uma mesma empresa pode abrir diferentes posições ou republicar a mesma vaga:
1. O agente examina a pasta `reports/<empresa>/jobs/`.
2. Se já existirem outras vagas salvas:
   - Compara a descrição da nova vaga com as já salvas em `reports/<empresa>/jobs/*/job-description.md`.
   - **Se a descrição for 90%+ idêntica (Vaga Duplicada/Reaberta):**
     O agente informa: *"Identifiquei que esta vaga é idêntica à vaga já processada em `reports/<empresa>/jobs/<slug>`. Deseja reutilizar o currículo já gerado ou criar uma variação?"*
   - **Se a descrição for diferente:**
     Gera um novo currículo especializado para a nova função, reutilizando 100% do dossiê institucional existente de `reports/<empresa>/company-report.md`.
3. Cria a subpasta dedicada da vaga: `reports/<empresa>/jobs/<ano-mes_slug-da-vaga>/`.

---

### Etapa 2: A Matriz de Cruzamento Estratégico & Padrões de Triagem por IA
Ao compilar o currículo e os artefatos, o agente aplica as regras dos **motores de triagem por IA (LLMs e ATS modernos)**:
- **Hard Filters Explícitos:** Localização/modelo remoto, senioridade e stack mandatória aparecem de forma clara e legível no cabeçalho e resumo.
- **Co-ocorrência Semântica:** Palavras-chave exigidas são inseridas contextualizadas na experiência prática (ex.: *Playwright + CI/CD + Page Object Model*), evitando repetições artificiais (*keyword stuffing*).
- **Fórmula de Impacto (Google X-Y-Z / STAR):** Cada bullet de experiência deve conter *Verbo de Ação + Contexto Técnico + Resultado Quantificado* (ex.: *50% de redução no tempo de regressão*, *24x aumento de vendas*).

| Seção do Entregável | Como o `company-report` é Utilizado | Regra de Zero Alucinação |
|---|---|---|
| **1. Resumo Profissional (`Professional Summary`)** | O resumo do currículo é calibrado para citar a indústria da empresa (Fintech, Healthtech, SaaS, etc.) e como a especialidade do candidato resolve os desafios de escala, qualidade ou IA identificados no relatório da empresa. | Usa **somente** títulos, anos de experiência e competências reais comprovadas em `career-knowledge.md`. |
| **2. Priorização de Bullets de Experiência** | Os bullets de realizações são reordenados para dar destaque àqueles que resolvem as dores e espelham a stack citada no `company-report` (ex: se a empresa foca em microsserviços, APIs e automação com Playwright/Python, os bullets dessas conquistas aparecem no topo de cada experiência). | **Nunca** altera números, métricas ou cria projetos que não existam em `career-knowledge.md`. |
| **3. Pitch de Abordagem para LinkedIn (`pitch-linkedin.md`)** | O pitch menciona explicitamente o momento atual ou produtos destacados no `company-report` (ex: *"Acompanho a evolução da [Empresa] em [Produto X] e o foco de vocês em [Inovação/Escala]..."*), gerando conexão imediata com o Tech Recruiter ou Hiring Manager. | Conecta o momento real da empresa com a experiência real do candidato. |
| **4. Respostas de Formulário (`screening-questions.md`)** | Questões clássicas como *"Por que você quer trabalhar na [Empresa]?"* ou *"Como você se conecta com nossos valores?"* são respondidas cruzando a missão/valores catalogados no relatório com a trajetória real do candidato. | Respostas estruturadas no método STAR, salvas também em `questions-bank.md`. |
| **5. Dossiê de Alinhamento para Entrevista (`interview-prep.md`)** | Cria uma folha rápida conectando as perguntas sugeridas no `company-report` com os 5 Desafios STAR do candidato de `career-knowledge.md`. | Fornece ao candidato os melhores exemplos prontos para cada potencial pergunta. |

---

## 📦 Topologia de Arquivos em `reports/<empresa>/`

O ecossistema separa os arquivos institucionais das vagas individuais:

```text
reports/<empresa>/
├── company-report.html         # ✅ Dossiê institucional visual (Passo 1 - TTL 90 dias)
├── company-report.md           # ✅ Dossiê estruturado com metadados (Passo 1)
├── company-report.pdf          # ✅ PDF do dossiê para leitura rápida (Passo 1)
│
└── jobs/
    └── <ano-mes_slug-da-vaga>/  # ✅ Subpasta isolada para cada oportunidade
        ├── Curriculo_<Nome>_<Vaga>.pdf # Currículo oficial A4 pronto para envio
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
