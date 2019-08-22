casos = int(input())

saida = []
for i in range(casos):
    linha = [chr(ord(x)+3) for x in list(input())]
    saida.append(linha)

print(*saida, sep='\n')
