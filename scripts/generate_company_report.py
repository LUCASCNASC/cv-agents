#!/usr/bin/env python3
"""
generate_company_report.py — Orquestra a extração institucional, tratamento dos dados, injeção no template padronizado e compilação do dossiê em PDF dentro de reports/<empresa>/.

Uso:
    python scripts/generate_company_report.py <URL> [Nome_Empresa] [Setor_Opcional]
"""

import sys
import os
import re
import datetime
from urllib.parse import urlparse
from extract_company_info import crawl_company_site

def clean_slug(name):
    slug = re.sub(r"[^\w\s-]", "", name.lower())
    return re.sub(r"[\s_-]+", "-", slug).strip("-")

def generate_report(url, company_name=None, sector=None):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_path = os.path.join(base_dir, "templates", "company-report-template.html")
    reports_root = os.path.join(base_dir, "reports")

    # Extração via Playwright
    data = crawl_company_site(url, company_name)
    name = company_name or data.get("company_name") or "Empresa"
    clean_name = clean_slug(name)

    company_folder = os.path.join(reports_root, clean_name)
    os.makedirs(company_folder, exist_ok=True)

    today = datetime.date.today()
    valid_until_date = today + datetime.timedelta(days=90)
    today_str = today.strftime("%d/%m/%Y")
    valid_until_str = valid_until_date.strftime("%d/%m/%Y")
    inferred_sector = sector or "Tecnologia / Serviços Digitais"

    about_text = data.get("meta_description") or (data["headings"][0] if data.get("headings") else f"{name} é uma organização inovadora em seu setor de atuação.")
    
    # Tratamento de produtos a partir dos headings e texto
    products = data.get("headings")[:5] if data.get("headings") else ["Soluções digitais e serviços especializados."]
    products_html = "\n".join([f"<li><strong>{p}</strong></li>" for p in products])

    # IA e Tecnologia
    ai_mentions = data.get("tech_ai_mentions")
    if ai_mentions:
        ai_overview = f"A {name} destaca tecnologia e soluções digitais no núcleo de sua proposta de valor."
        ai_html = "\n".join([f"<li>{m}</li>" for m in ai_mentions[:4]])
    else:
        ai_overview = f"A {name} opera com forte base em automação, serviços em nuvem e digitalização contínua de processos."
        ai_html = "<li>Foco em escalabilidade e modernização contínua da stack técnica.</li>\n<li>Adoção de boas práticas ágeis e arquitetura moderna de microsserviços.</li>"

    # Dicas de entrevista
    interview_tips = [
        f"Demonstre como sua bagagem técnica ajuda a destravar a missão da {name}.",
        f"Pergunte ao entrevistador: 'Como o time de engenharia da {name} equilibra velocidade de novas features com qualidade e automação contínua?'",
        "Conecte seus desafios reais com métricas (redução de tempo, detecção antecipada de bugs) às dores de escala da empresa."
    ]
    tips_html = "\n".join([f"<li>{tip}</li>" for tip in interview_tips])

    # Injeção no template HTML
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    html_content = template
    html_content = html_content.replace("{{COMPANY_NAME}}", name)
    html_content = html_content.replace("{{COMPANY_URL}}", data.get("url", url))
    html_content = html_content.replace("{{COMPANY_URL_LABEL}}", urlparse(data.get("url", url)).netloc)
    html_content = html_content.replace("{{REPORT_DATE}}", today_str)
    html_content = html_content.replace("{{VALID_UNTIL}}", valid_until_str)
    html_content = html_content.replace("{{TTL_DAYS}}", "90")
    html_content = html_content.replace("{{INDUSTRY_SECTOR}}", inferred_sector)
    html_content = html_content.replace("{{FOUNDATION_YEAR}}", "Consolidada no mercado")
    html_content = html_content.replace("{{EMPLOYEE_COUNT}}", "Em expansão")
    html_content = html_content.replace("{{LEADERSHIP_NAME}}", "Diretoria & C-Level")
    html_content = html_content.replace("{{BUSINESS_MODEL}}", "Digital / B2B & B2C")
    html_content = html_content.replace("{{ABOUT_COMPANY}}", about_text)
    html_content = html_content.replace("{{COMPANY_HISTORY}}", f"Fundada com a proposta de transformar seu setor, a {name} vem expandindo sua atuação através de inovação contínua e foco na experiência de seus usuários e parceiros.")
    html_content = html_content.replace("{{CURRENT_MOMENT_BULLETS}}", f"<li>Foco em expansão de clientes e consolidação de produtos digitais.</li>\n<li>Fortalecimento dos times de tecnologia e engenharia.</li>")
    html_content = html_content.replace("{{PRODUCTS_BULLETS}}", products_html)
    html_content = html_content.replace("{{TECH_AND_AI_OVERVIEW}}", ai_overview)
    html_content = html_content.replace("{{TECH_AND_AI_BULLETS}}", ai_html)
    html_content = html_content.replace("{{CLIENTS_AND_PARTNERS_BULLETS}}", f"<li>Ecossistema de parceiros estratégicos e base sólida de clientes no setor de {inferred_sector}.</li>")
    html_content = html_content.replace("{{INTERVIEW_TIPS}}", tips_html)

    # Gravar HTML do Report
    report_html_path = os.path.join(company_folder, "company-report.html")
    with open(report_html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    # Gravar Markdown do Report com Metadados Frontmatter (para controle de TTL)
    report_md_path = os.path.join(company_folder, "company-report.md")
    with open(report_md_path, "w", encoding="utf-8") as f:
        f.write(f"---\n")
        f.write(f'company: "{name}"\n')
        f.write(f'website: "{url}"\n')
        f.write(f'generated_at: "{today.isoformat()}"\n')
        f.write(f'valid_until: "{valid_until_date.isoformat()}"\n')
        f.write(f'ttl_days: 90\n')
        f.write(f'sector: "{inferred_sector}"\n')
        f.write(f"---\n\n")
        f.write(f"# Dossiê Estratégico: {name}\n\n")
        f.write(f"- **Website:** {url}\n- **Data de Análise:** {today_str}\n- **Validade do Dossiê:** Até {valid_until_str} (Ciclo de 90 dias)\n- **Setor:** {inferred_sector}\n\n")
        f.write(f"## 1. Visão Geral\n{about_text}\n\n")
        f.write(f"## 2. Produtos & Soluções\n" + "\n".join([f"- {p}" for p in products]) + "\n\n")
        f.write(f"## 3. Tecnologia & IA\n{ai_overview}\n\n")
        f.write(f"## 4. Dicas para a Entrevista\n" + "\n".join([f"- {t}" for t in interview_tips]) + "\n")

    # Compilar PDF via Chromium
    report_pdf_path = os.path.join(company_folder, "company-report.pdf")
    from generate_pdf import convert_html_to_pdf
    convert_html_to_pdf(report_html_path, report_pdf_path)

    return {
        "folder": company_folder,
        "html": report_html_path,
        "md": report_md_path,
        "pdf": report_pdf_path,
        "generated_at": today.isoformat(),
        "valid_until": valid_until_date.isoformat()
    }

def check_report_freshness(company_dir_or_md):
    """
    Verifica a idade e o status de frescor de um company-report.md existente.
    Retorna dicionário com status ('fresh', 'warning', 'expired'), idade em dias e mensagem.
    """
    if os.path.isdir(company_dir_or_md):
        md_path = os.path.join(company_dir_or_md, "company-report.md")
    else:
        md_path = company_dir_or_md

    if not os.path.isfile(md_path):
        return {
            "exists": False,
            "status": "not_found",
            "age_days": None,
            "message": "Relatório não encontrado."
        }

    with open(md_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # Busca data no frontmatter ou usa mtime do arquivo
    match = re.search(r'generated_at:\s*["\']?(\d{4}-\d{2}-\d{2})["\']?', content)
    if match:
        gen_date = datetime.date.fromisoformat(match.group(1))
    else:
        # Fallback para data de modificação do arquivo
        mtime = os.path.getmtime(md_path)
        gen_date = datetime.date.fromtimestamp(mtime)

    today = datetime.date.today()
    age_days = (today - gen_date).days

    if age_days <= 60:
        status = "fresh"
        msg = f"Relatório válido e recente ({age_days} dias desde a geração). Pronto para uso."
    elif age_days <= 90:
        status = "warning"
        msg = f"Relatório próximo da expiração ({age_days} dias). Válido, mas recomenda-se checar se houve novidades na empresa."
    else:
        status = "expired"
        msg = f"Relatório expirado ({age_days} dias > 90 dias de ciclo). Recomenda-se rodar /company-report para atualizar."

    return {
        "exists": True,
        "status": status,
        "age_days": age_days,
        "generated_at": gen_date.isoformat(),
        "valid_until": (gen_date + datetime.timedelta(days=90)).isoformat(),
        "message": msg
    }

def main():
    if len(sys.argv) < 2:
        print("Uso: python generate_company_report.py <URL> [Nome_Empresa] [Setor]")
        print("Ou:  python generate_company_report.py --check <reports/empresa/>")
        sys.exit(1)

    if sys.argv[1] == "--check":
        if len(sys.argv) < 3:
            print("Informe o caminho da pasta ou markdown do relatório.")
            sys.exit(1)
        res = check_report_freshness(sys.argv[2])
        print(f"Status: {res['status'].upper()}")
        print(f"Idade: {res['age_days']} dias")
        print(f"Mensagem: {res['message']}")
        return

    url = sys.argv[1]
    name = sys.argv[2] if len(sys.argv) > 2 else None
    sector = sys.argv[3] if len(sys.argv) > 3 else None

    res = generate_report(url, name, sector)
    print(f"Sucesso! Relatório gerado em: {res['folder']}")
    print(f"PDF: {res['pdf']}")

if __name__ == "__main__":
    main()
