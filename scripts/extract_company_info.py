#!/usr/bin/env python3
"""
extract_company_info.py — Extrai informações institucionais cruciais de um website via Playwright.

Uso:
    python scripts/extract_company_info.py <URL> [Nome_Opcional]
"""

import sys
import os
import json
import re
from urllib.parse import urlparse

def sanitize_url(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        return "https://" + url
    return url

def extract_domain_name(url):
    parsed = urlparse(sanitize_url(url))
    domain = parsed.netloc.replace("www.", "").split(".")[0]
    return domain.capitalize()

def crawl_company_site(target_url, company_name=None):
    from playwright.sync_api import sync_playwright

    url = sanitize_url(target_url)
    inferred_name = company_name or extract_domain_name(url)

    result = {
        "company_name": inferred_name,
        "url": url,
        "title": "",
        "meta_description": "",
        "headings": [],
        "about_text": "",
        "products_text": "",
        "tech_ai_mentions": [],
        "clients_partners": [],
        "raw_text_summary": ""
    }

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = context.new_page()

        try:
            page.goto(url, wait_until="domcontentloaded", timeout=25000)
            page.wait_for_timeout(2000)

            result["title"] = page.title()

            # Meta description
            meta_desc = page.query_selector('meta[name="description"]') or page.query_selector('meta[property="og:description"]')
            if meta_desc:
                result["meta_description"] = meta_desc.get_attribute("content") or ""

            # Extração de cabeçalhos relevantes (H1, H2)
            headings = []
            for h in page.query_selector_all("h1, h2"):
                txt = h.inner_text().strip()
                if txt and len(txt) > 3 and len(txt) < 120 and txt not in headings:
                    headings.append(txt)
            result["headings"] = headings[:12]

            # Captura de texto visível principal
            body_text = page.inner_text("body")
            
            # Busca de menções a IA / Tecnologia
            ai_keywords = [r"\bIA\b", r"\bAI\b", r"intelig[eê]ncia artificial", r"machine learning", r"algoritmo", r"automação", r"cloud", r"nuvem", r"api"]
            found_ai = []
            for line in body_text.splitlines():
                line_clean = line.strip()
                if len(line_clean) > 20 and len(line_clean) < 250:
                    for kw in ai_keywords:
                        if re.search(kw, line_clean, re.IGNORECASE):
                            if line_clean not in found_ai:
                                found_ai.append(line_clean)
                            break
            result["tech_ai_mentions"] = found_ai[:8]

            # Limpeza de texto para resumo
            clean_lines = [l.strip() for l in body_text.splitlines() if len(l.strip()) > 25]
            result["raw_text_summary"] = " \n".join(clean_lines[:40])

        except Exception as e:
            result["error"] = str(e)
        finally:
            browser.close()

    return result

def main():
    if len(sys.argv) < 2:
        print("Uso: python extract_company_info.py <URL> [Nome_Opcional]")
        sys.exit(1)

    target_url = sys.argv[1]
    name = sys.argv[2] if len(sys.argv) > 2 else None

    info = crawl_company_site(target_url, name)
    print(json.dumps(info, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
