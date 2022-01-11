mensagem_criptografada = input()
crib = input()
possibilidade = 0

for i in range((len(mensagem_criptografada) - len(crib))+1):
    valido = True
    teste = mensagem_criptografada[i:len(crib)+i]
    for i in range(len(teste)):
        if teste[i] == crib[i]:
            valido = False
            break

    if valido:
        possibilidade += 1

print(possibilidade)
