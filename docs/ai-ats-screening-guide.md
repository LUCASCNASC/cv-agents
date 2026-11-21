# 🤖 Guia Definitivo: Como Funciona a Triagem de Currículos por IA & ATS

Este documento detalha o funcionamento interno dos sistemas modernos de recrutamento orientados por Inteligência Artificial e ATS (*Applicant Tracking Systems*), servindo de base para a engenharia de prompts e geração de currículos no projeto **CV-Agent**.

---

## 1. O Novo Cenário do Recrutamento: Da Triagem Tradicional à Triagem por IA

Atualmente, **mais de 90% das grandes empresas e 70% das médias/startups** utilizam sistemas automatizados antes de qualquer contato humano. Esse processo divide-se em duas camadas:

```
[ Candidatura Enviada (PDF/Texto) ]
                │
                ▼
      ┌──────────────────┐
      │   CAMADA 1: ATS  │  (Greenhouse, Lever, Workday, Ashby, Gupy)
      │  Parsing & Regex │  -> Converte PDF em texto estruturado
      └─────────┬────────┘
                │
                ▼
      ┌──────────────────┐
      │  CAMADA 2: IA    │  (Agentes LLMs, Embeddings Vetoriais)
      │ Semantic Matching│  -> Avalia aderência contextual, realizações e score
      └─────────┬────────┘
                │
                ▼
[ Recrutador Humano / Hiring Manager ] (Lê os top 5-10% recomendados)
```

---

## 2. Camada 1: O Que o ATS Tradicional Avalia (Parsing & Estrutura)

Os motores de ATS tradicionais não "leem" o design visual; eles convertem o arquivo em texto puro (JSON estruturado):

- **Parsing de Seções:** O parser busca por cabeçalhos padrão (`EXPERIENCE`, `EDUCATION`, `SKILLS`, `SUMMARY`). Seções com nomes inventados ou criativos podem ser ignoradas.
- **Hierarquia de Cargos:** O parser procura padrões do tipo: `[Cargo] | [Data]` seguido por `[Empresa] | [Local]`.
- **Armadilhas que eliminam currículos no ATS:**
  - Tabelas complexas de múltiplas colunas (o leitor costuma ler linhas cruzadas, misturando colunas).
  - Imagens, ícones decorativos com texto dentro, caixas flutuantes de texto.
  - Fontes obscuras ou caracteres especiais não padrão.
  - PDFs baseados em imagem (sem camada vetorial de texto selecionável).
  
> **Como nosso sistema resolve:** O template padrão ([CV_English_Lucas_Camargo_QA.pdf](../templates/CV_English_Lucas_Camargo_QA.pdf) e seus equivalentes HTML) utiliza layout linear vertical, tipografia Arial pura, sem tabelas quebradas, gerando PDFs vetoriais com **100% de taxa de extração semântica**.

---

## 3. Camada 2: Como a IA (LLMs & Embeddings) Avalia o Currículo

Ferramentas modernas (ex: Eightfold AI, Phenom, Ashby AI, além de recrutadores usando Claude/ChatGPT para ranquear inscrições) utilizam processamento de linguagem natural avançado:

### A. Similaridade Semântica (Embeddings)
O sistema gera um vetor numérico da descrição da vaga e um vetor do currículo.
- Não basta apenas repetir uma palavra-chave 20 vezes (técnica antiga de "keyword stuffing", hoje penalizada).
- A IA avalia o **contexto de uso**: se a vaga pede "Playwright com CI/CD", a IA verifica se a experiência descreve *como* o Playwright foi integrado ao GitLab CI/CD e qual foi o resultado dessa integração.

### B. O Princípio STAR & Métricas de Negócio
LLMs são treinados para valorizar sentenças que demonstram impacto real:
- **Fraco:** *"Responsável por testes de regressão no sistema."*
- **Forte (Score Alto na IA):** *"Reduziu o tempo de execução da regressão em 50% através da implementação de framework Cypress POM integrado ao GitHub Actions."*
- A IA pontua mais alto sentenças com **Verbo de Ação + Contexto Técnico + Resultado Quantificado**.

### C. Densidade de Hard Skills vs. Contexto de Domínio
- **Hard Skills Exatas:** Se a vaga pede *PostgreSQL, k6, Docker e AWS Lambda*, a ausência literal desses termos reduz o score de match.
- **Conhecimento de Domínio:** A IA correlaciona setores. Para uma vaga em fintech, menções a *crédito consignado, mobile banking, APIs governamentais e integridade transacional* elevam o score de relevância contextual mesmo se não constarem explicitamente como obrigatórias na vaga.

---

## 4. O Checklist do Agente para Bater a Triagem de IA (Score 90+)

Ao adaptar um currículo pelo comando `/new-opportunity`, o agente aplica as seguintes regras:

1. **Espelhamento do Título da Vaga:** O título profissional no topo do currículo deve refletir a nomenclatura da vaga.
2. **Resumo Contextualizado com as Dores da Empresa:** O primeiro parágrafo deve responder exatamente aos 2 ou 3 maiores desafios técnicos citados na vaga.
3. **Harmonização Exata de Palavras-Chave:** Todas as ferramentas obrigatórias da vaga devem constar na seção `TECHNICAL SKILLS` e serem repetidas dentro de pelo menos um bullet point de experiência prática.
4. **Métricas Explícitas:** Manter sempre as métricas reais registradas (ex: 24x vendas, 50% redução de tempo, Top 5 nacional).
5. **Contexto Institucional:** Se a empresa valoriza alta escalabilidade ou segurança, esses valores devem permear a redação das experiências.
