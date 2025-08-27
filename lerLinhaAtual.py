import pdfplumber
import csv

arquivo_pdf = "arquivo.pdf"
arquivo_csv = "nomePessoa.csv"
bloco = 100  # processa 100 páginas por vez

# Primeiro, pega o total de páginas
with pdfplumber.open(arquivo_pdf) as pdf:
    total_paginas = len(pdf.pages)

# Abre o CSV **uma vez**, fora do loop de blocos
with open(arquivo_csv, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Linha"])  # cabeçalho

    # Loop pelos blocos
    for inicio in range(0, total_paginas, bloco):
        fim = min(inicio + bloco, total_paginas)
        print(f"🔄 Processando páginas {inicio} a {fim - 1}...")

        # Abre o PDF apenas para o bloco atual
        with pdfplumber.open(arquivo_pdf) as pdf:
            for page_number in range(inicio, fim):
                page = pdf.pages[page_number]
                texto = page.extract_text()
                if not texto:
                    continue
                linhas = texto.split("\n")
                for linha in linhas:
                    if "nomePessoa" in linha.upper():
                        # **Escreve direto no CSV aberto**
                        writer.writerow([linha.strip()])

print("🚀 Extração completa!")
