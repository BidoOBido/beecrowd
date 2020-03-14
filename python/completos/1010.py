linha1 = input().split()
linha2 = input().split()

quantidade1, quantidade2 = int(linha1[1]), int(linha2[1])
valor1, valor2 = float(linha1[2]), float(linha2[2])

total = (quantidade1 * valor1) + (quantidade2 * valor2)

print("VALOR A PAGAR: R$ %.2f" % total)
