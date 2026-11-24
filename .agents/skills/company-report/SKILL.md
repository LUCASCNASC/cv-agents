---
name: company-report
description: Inicia o agente de inteligência institucional. Acessa o site da empresa via Playwright, extrai informações estratégicas para a entrevista (visão, história, momento, produtos, IA, parceiros, liderança), trata os dados sem gastar tokens desnecessários e gera um relatório padronizado em HTML e PDF dentro de reports/<empresa>/.
---

# Agente: Company Report (`/company-report`)

Este agente é o **Passo 1** do fluxo de preparação de candidaturas. Ele realiza a raspagem e tratamento institucional do site da empresa via **Playwright MCP / Script Playwright**, estruturando um dossiê executivo pré-entrevista e criando a pasta oficial da empresa dentro de `reports/<empresa>/`.

---

## 🚀 Como Acionar

No chat, digite o comando passando a URL do site institucional (e opcionalmente o nome da empresa):

```text
/company-report https://site-da-empresa.com
```
ou
```text
/company-report "Nome da Empresa" https://site-da-empresa.com
```

---

## 📋 Informações Cruciais Extraídas

O agente e as ferramentas de Playwright extraem e estruturam:
1. **Sobre a Empresa:** Visão geral, missão e proposta de valor clara.
2. **História:** Fundação, trajetória e marcos do negócio.
3. **Momento Atual:** Crescimento recente, expansões, notícias de mercado ou rodadas.
4. **Produtos & Serviços:** Portfólio de soluções core e o que a empresa vende/oferece.
5. **Uso de IA & Tecnologia:** Inovações, arquitetura, menções a inteligência artificial, automação e cloud.
6. **Principais Parceiros & Clientes:** Marcas atendidas e ecossistema parceiro.
7. **Liderança & Estrutura:** Fundadores, C-level e porte estimado da equipe.
8. **Cheat-Sheet para a Entrevista:** Dicas de conexão técnica e perguntas inteligentes para fazer ao entrevistador.

---

## ⚙️ Processamento & Economia de Tokens

- O conteúdo bruto é extraído via Chromium headless (Playwright).
- O agente saneia as informações e **injeta diretamente no template padronizado** [`templates/company-report-template.html`](../../../templates/company-report-template.html), evitando geração manual redundante de CSS/HTML e economizando tokens.
- O resultado é compilado automaticamente para PDF via Chromium.

---

## 📁 Estrutura de Saída (`reports/<empresa>/`)

O agente cria e organiza o dossiê institucional na raiz da pasta da empresa:
```text
reports/<empresa>/
├── company-report.html  # Relatório padronizado em HTML (com data e validade visual)
├── company-report.md    # Dossiê em Markdown com metadados Frontmatter (TTL de 90 dias)
└── company-report.pdf   # PDF oficial A4 pronto para impressão/revisão
```

### ⏳ Ciclo de Validade & Metadados (TTL de 90 Dias)
O arquivo `company-report.md` é gerado com metadados estruturados para controle de obsolescência:
```yaml
---
company: "Nome da Empresa"
website: "https://site-da-empresa.com"
generated_at: "2026-11-23"
valid_until: "2027-02-21"
ttl_days: 90
sector: "Fintech / Serviços Digitais"
---
```
- **0 a 60 dias:** Relatório considerado **recente/fresco**; pode ser reutilizado diretamente por qualquer vaga da mesma empresa.
- **61 a 90 dias:** Relatório **válido com aviso**; recomenda-se verificar novidades pontuais.
- **Acima de 90 dias:** Relatório **expirado**; o comando `/new-opportunity` alertará para regerar o dossiê.

Essa mesma pasta será utilizada no **Passo 2** pelo comando `/new-opportunity`, que criará subpastas isoladas em `reports/<empresa>/jobs/<vaga>/` para permitir múltiplas candidaturas na mesma empresa sem sobrescrever arquivos!
