#!/usr/bin/env python3
"""
ats_scorer.py — Avaliador automático de aderência ATS e compatibilidade com triagem por IA.

Uso:
    python scripts/ats_scorer.py <caminho_vaga.txt> <caminho_resume.html>
"""

import sys
import os
import re
from collections import Counter

TECH_PATTERNS = [
    r"playwright", r"cypress", r"postman", r"swagger", r"openapi", r"bruno",
    r"typescript", r"javascript", r"python", r"sql", r"postgresql", r"sql server",
    r"mongodb", r"docker", r"jenkins", r"gitlab", r"github actions", r"azure devops",
    r"bitbucket", r"aws", r"lambda", r"datadog", r"grafana", r"argo cd", r"k6",
    r"jira", r"confluence", r"qase", r"bdd", r"scrum", r"pom", r"page object model",
    r"appium", r"robot framework", r"claude", r"copilot", r"llm", r"mcp"
]

def clean_text(html_or_text):
    # Remove tags HTML se houver
    text = re.sub(r"<[^>]+>", " ", html_or_text)
    text = re.sub(r"\s+", " ", text)
    return text.lower()

def extract_keywords(text):
    found = set()
    for pattern in TECH_PATTERNS:
        if re.search(r"\b" + pattern + r"\b", text, re.IGNORECASE):
            found.add(pattern)
    return found

def analyze_match(job_text, resume_text):
    job_clean = clean_text(job_text)
    resume_clean = clean_text(resume_text)

    job_keywords = extract_keywords(job_clean)
    resume_keywords = extract_keywords(resume_clean)

    matched = job_keywords.intersection(resume_keywords)
    missing = job_keywords - resume_keywords

    score_keywords = (len(matched) / max(len(job_keywords), 1)) * 60

    # Checagem de métricas quantificadas (números, %, x)
    has_metrics = bool(re.search(r"\b\d+([.,]\d+)?%|\b\d+x\b|\b\d+\s*(anos|years|segundos|seconds|minutos|min)\b", resume_clean))
    score_metrics = 15 if has_metrics else 5

    # Checagem de seções obrigatórias para ATS
    sections = [r"summary|resumo", r"skills|competências", r"experience|experiência", r"education|formação"]
    sections_found = sum(1 for sec in sections if re.search(sec, resume_clean))
    score_sections = (sections_found / len(sections)) * 15

    # Checagem de contatos e links
    has_contact = bool(re.search(r"linkedin|github", resume_clean) and re.search(r"@\w+\.\w+", resume_clean))
    score_contact = 10 if has_contact else 0

    total_score = min(round(score_keywords + score_metrics + score_sections + score_contact), 100)

    return {
        "total_score": total_score,
        "job_keywords_count": len(job_keywords),
        "matched_keywords": sorted(list(matched)),
        "missing_keywords": sorted(list(missing)),
        "has_metrics": has_metrics,
        "sections_found": sections_found,
        "has_contact": has_contact
    }

def main():
    if len(sys.argv) < 3:
        print("Uso: python ats_scorer.py <vaga.txt> <resume.html>")
        sys.exit(1)

    job_path = sys.argv[1]
    resume_path = sys.argv[2]

    if not os.path.isfile(job_path):
        print(f"Arquivo da vaga não encontrado: {job_path}", file=sys.stderr)
        sys.exit(1)

    if not os.path.isfile(resume_path):
        print(f"Arquivo do currículo não encontrado: {resume_path}", file=sys.stderr)
        sys.exit(1)

    with open(job_path, "r", encoding="utf-8", errors="ignore") as f:
        job_content = f.read()

    with open(resume_path, "r", encoding="utf-8", errors="ignore") as f:
        resume_content = f.read()

    result = analyze_match(job_content, resume_content)

    print("=" * 60)
    print(f"📊 RELATÓRIO DE AUDITORIA ATS & COMPATIBILIDADE DE IA")
    print("=" * 60)
    print(f"🎯 Score Geral de Aderência: {result['total_score']} / 100")
    print(f"✅ Palavras-chave Detectadas ({len(result['matched_keywords'])}): {', '.join(result['matched_keywords']) if result['matched_keywords'] else 'Nenhuma'}")
    if result['missing_keywords']:
        print(f"⚠️ Palavras-chave Não Encontradas ({len(result['missing_keywords'])}): {', '.join(result['missing_keywords'])}")
    else:
        print(f"✨ 100% das palavras-chave técnicas da vaga foram atendidas!")
    print(f"📈 Métricas Quantitativas Presentes: {'Sim' if result['has_metrics'] else 'Não'}")
    print(f"📑 Estrutura de Seções ATS: {result['sections_found']}/4 presentes")
    print(f"📞 Informações de Contato & Links: {'Válidos' if result['has_contact'] else 'Incompletos'}")
    print("=" * 60)

if __name__ == "__main__":
    main()
