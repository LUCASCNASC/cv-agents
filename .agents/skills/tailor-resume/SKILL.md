---
name: tailor-resume
description: Adapts Lucas Camargo's resume to match specific job requirements using career-knowledge.md and automatically generates an ATS-optimized PDF matching the exact template of CV_English_Lucas_Camargo_QA.pdf.
---

# Skill: Adaptador Inteligente de Currículo (Tailor Resume)

Esta skill permite ao agente analisar a descrição de uma vaga de emprego, cruzar os requisitos com a base de conhecimento de carreira ([career-knowledge.md](../../../career-knowledge.md)) e produzir uma versão altamente personalizada do currículo em HTML e PDF profissional, **seguindo rigorosamente o design visual e a estrutura padrão do arquivo oficial `CV_English_Lucas_Camargo_QA.pdf`**.

---

## 🎨 Template Padrão Oficial: `CV_English_Lucas_Camargo_QA.pdf`

O template visual padrão adotado é o modelo clássico, minimalista e 100% otimizado para ATS (Applicant Tracking Systems) presente em `CV_English_Lucas_Camargo_QA.pdf`:
- **Tipografia:** Arial / Helvetica, limpa, sem serifa, contraste preto sobre branco.
- **Margens:** 20mm uniformes para formato A4.
- **Cabeçalho:** Nome em caixa alta e negrito (`LUCAS CAMARGO`), seguido por localização, telefone, e-mail e links discretos para LinkedIn e GitHub.
- **Seções em Caixa Alta:** `PROFESSIONAL SUMMARY` (ou `RESUMO PROFISSIONAL`), `TECHNICAL SKILLS` (ou `COMPETÊNCIAS TÉCNICAS`), `PROFESSIONAL EXPERIENCE` (ou `EXPERIÊNCIA PROFISSIONAL`) e `EDUCATION & LANGUAGES` (ou `FORMAÇÃO ACADÊMICA & IDIOMAS`).
- **Formatação de Experiências:**
  - Linha 1: **Cargo | Período** (Negrito)
  - Linha 2: *Empresa | Localidade* (Itálico)
  - Bullets com marcadores circulares padrão e recuo de 20px.

Os arquivos de template que implementam esse design são:
- [resume-template-en.html](../../../templates/resume-template-en.html) (para vagas internacionais ou em inglês)
- [resume-template-pt.html](../../../templates/resume-template-pt.html) (para vagas em português)

---

## Diretrizes de Ouro (Fidelidade aos Fatos)

1. **Zero Alucinação:** Nunca invente empresas, tecnologias, datas, métricas ou responsabilidades que não constem expressamente em `career-knowledge.md`.
2. **Customização Estratégica:** A adaptação consiste em:
   - Escrever um **Resumo Profissional** cirúrgico conectando a bagagem de Lucas à dor principal da empresa contratante.
   - **Reordenar e destacar competências técnicas** (as ferramentas exigidas pela vaga devem vir em primeiro lugar dentro das categorias de `TECHNICAL SKILLS`).
   - **Priorizar os bullet points e conquistas** mais alinhados aos requisitos da vaga (ex: se a vaga pede APIs governamentais e fintech, destacar a Finnet e métricas de 24x vendas; se pede Playwright e IA, destacar a Gazin Tech).
   - Utilizar as palavras-chave da vaga para maximizar a pontuação em filtros ATS.
3. **Idioma:** Identificar o idioma da vaga (Português ou Inglês) e utilizar o respectivo template (`templates/resume-template-pt.html` ou `templates/resume-template-en.html`).

---

## Fluxo de Execução Passo a Passo

### 1. Coleta e Análise da Vaga
- O usuário fornece o texto da vaga no chat ou aponta para um arquivo em `jobs/`.
- Extrair:
  - Nome da Empresa e Título do Cargo.
  - Idioma alvo (`pt` ou `en`).
  - Nível de senioridade esperado.
  - Requisitos obrigatórios vs. diferenciais.
  - Stack técnica principal e palavras-chave.

### 2. Leitura da Base de Conhecimento
- Ler o arquivo `career-knowledge.md` para resgatar os detalhes das experiências (Gazin Tech, Finnet/Gooroo Crédito, Sabium Sistemas, NCS Sistemas Inteligentes), métricas (24x vendas, 50% redução de tempo), ferramentas e certificações.

### 3. Seleção & Redação do Conteúdo Personalizado
- **Resumo:** 3 a 4 linhas sintetizando os anos de experiência e a aderência exata aos desafios propostos na vaga.
- **Competências:** Separadas por categorias (`Automation Frameworks`, `Languages`, `DevOps & CI/CD`, `Cloud & Observability`, `Tools & Management`), priorizando as ferramentas exigidas.
- **Experiências:** 3 a 4 bullet points por empresa com foco em impacto mensurável, tecnologias aplicadas e resultados STAR.
- **Formação & Idiomas:** B.S. in Software Engineering (Unifatecie) + Certificações + Idiomas (Inglês Avançado C1 e Português Nativo).

### 4. Geração do HTML
- Carregar o template adequado (`templates/resume-template-pt.html` ou `templates/resume-template-en.html`).
- Substituir os placeholders pelo conteúdo gerado.
- Gravar o arquivo em `output/<empresa>-<cargo>/resume.html`.

### 5. Compilação para PDF
- Executar o script de compilação:
  ```powershell
  python scripts/generate_pdf.py "output/<empresa>-<cargo>/resume.html" "output/<empresa>-<cargo>/Curriculo_Lucas_Camargo.pdf"
  ```
- O script utiliza Google Chrome / Microsoft Edge em modo headless (`--headless=new --print-to-pdf`) para produzir um PDF com o visual idêntico ao `CV_English_Lucas_Camargo_QA.pdf`.

### 6. Relatório de Entrega ao Usuário
- Apresentar:
  - Tabela de **Aderência à Vaga (Match ATS)** mostrando quais requisitos foram atendidos e onde foram destacados.
  - Resumo das customizações realizadas.
  - Link clicável direto para o PDF gerado (`file:///...`).
