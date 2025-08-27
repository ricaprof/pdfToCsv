import pdfplumber
import re
import csv

saida = "lancamentos_nomePessoa_formatado.csv"
chunk_size = 100
total_paginas = 6000  # ajuste conforme necessário

with open(saida, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Campo1","Campo2","Campo3","Campo4","Campo5","Nome","nomePessoa","Valor"])

    for inicio in range(1):
        fim = min(inicio + chunk_size, total_paginas)
        print(f"🔄 Processando páginas {inicio+1} até {fim}...")

        # abre o PDF apenas para esse bloco
        with pdfplumber.open("arquivo.pdf") as pdf:
            for page in pdf.pages[500:530]:
                texto = page.extract_text()
                if not texto:
                    continue
                linhas = texto.split("\n")
                for i, linha in enumerate(linhas):
                    linha = linha.strip()
                    if "nomePessoa" in linha.upper() and i > 0:
                       # linha_cima = linhas[i-1].strip()
                        match = re.match(r'^(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(.*)', linha)
                        if match:
                            col1, col2, col3, col4, col5, resto = match.groups()
                            valor_match = re.search(r'(\d{1,3}(?:\.\d{3})*,\d{2})$', resto)
                            if valor_match:
                                valor = valor_match.group(1)
                                nome = resto[:valor_match.start()].strip()
                                # escreve direto no CSV
                                writer.writerow([col1, col2, col3, col4, col5, nome, linha, valor])

        print(f"✅ Bloco {inicio+1}-{fim} concluído!")

print(f"🚀 Extração concluída! Arquivo gerado: {saida}")
