import csv

entrada = "loureiro.csv"
saida = "loureiro_formatado.csv"

with open(entrada, newline="", encoding="utf-8") as f_in, \
     open(saida, mode="w", newline="", encoding="utf-8") as f_out:

    reader = csv.reader(f_in)
    writer = csv.writer(f_out)
    
    # Cabeçalho
    writer.writerow(["Campo1","Campo2","Campo3","Campo4","Campo5","Resto","Valor"])
    
    next(reader)  # pula o cabeçalho antigo

    for row in reader:
        linha = row[0]  # toda a linha original está em uma coluna

        # Divide a linha em partes pelo espaço
        partes = linha.split()

        if len(partes) >= 6:
            # Os cinco primeiros campos
            c1, c2, c3, c4, c5 = partes[:5]

            # Valor (último elemento)
            valor = partes[-1]

            # Resto do conteúdo entre os cinco primeiros campos e o valor
            resto = " ".join(partes[5:-1])

            # Escreve no CSV separado por vírgula
            writer.writerow([c1, c2, c3, c4, c5, resto, valor])
