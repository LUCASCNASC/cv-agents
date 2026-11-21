#!/usr/bin/env python3
"""
generate_pdf.py — Converte arquivos HTML em PDF utilizando o motor Chromium (Google Chrome ou Microsoft Edge) headless.

Uso via linha de comando:
    python scripts/generate_pdf.py caminho/arquivo.html caminho/saida.pdf
"""

import sys
import os
import subprocess
import shutil

CHROME_CANDIDATE_PATHS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"),
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Edge\Application\msedge.exe"),
]

def find_chromium_browser():
    """Localiza o executável do Chrome ou Edge instalado na máquina."""
    for path in CHROME_CANDIDATE_PATHS:
        if os.path.isfile(path):
            return path
    
    # Fallback procurando no PATH do sistema
    for cmd in ["chrome", "google-chrome", "msedge", "chromium"]:
        found = shutil.which(cmd)
        if found:
            return found
            
    return None

def convert_html_to_pdf(html_path, output_pdf_path):
    """
    Renderiza o HTML fornecido em PDF usando Chrome/Edge headless.
    """
    html_abs = os.path.abspath(html_path)
    pdf_abs = os.path.abspath(output_pdf_path)

    if not os.path.isfile(html_abs):
        raise FileNotFoundError(f"Arquivo HTML de entrada não encontrado: {html_abs}")

    browser_path = find_chromium_browser()
    if not browser_path:
        raise RuntimeError("Nenhum navegador Chromium (Google Chrome ou Microsoft Edge) foi encontrado no sistema.")

    # Garante que a pasta de destino exista
    os.makedirs(os.path.dirname(pdf_abs), exist_ok=True)

    # Argumentos do Chromium para impressão limpa de PDF
    cmd = [
        browser_path,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--no-pdf-header-footer",  # Remove cabeçalhos automáticos de URL e data
        f"--print-to-pdf={pdf_abs}",
        html_abs
    ]

    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    if not os.path.isfile(pdf_abs) or os.path.getsize(pdf_abs) == 0:
        raise RuntimeError(
            f"Falha ao gerar PDF. Código de saída: {result.returncode}\n"
            f"Stderr: {result.stderr}\nStdout: {result.stdout}"
        )

    return pdf_abs

def main():
    if len(sys.argv) < 3:
        print("Uso: python generate_pdf.py <caminho_html> <caminho_pdf>")
        sys.exit(1)

    html_file = sys.argv[1]
    pdf_file = sys.argv[2]

    try:
        pdf_path = convert_html_to_pdf(html_file, pdf_file)
        file_size_kb = os.path.getsize(pdf_path) / 1024
        print(f"Sucesso! PDF gerado em: {pdf_path} ({file_size_kb:.1f} KB)")
    except Exception as e:
        print(f"Erro: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
