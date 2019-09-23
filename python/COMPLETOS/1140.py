while True:
    frase = input()
    if frase == '*':
        break

    saida = 'Y'
    entrada = list(frase.split())
    for i in range(len(entrada)):
        if entrada[i][0].upper() != entrada[0][0].upper():
            saida = 'N'
            break

    print(saida)
