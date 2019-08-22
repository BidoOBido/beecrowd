import math

saida = []


def primeira(entrada):
    if 'A' <= entrada.upper() <= 'Z':
        return chr((ord(entrada)+3))
    else:
        return entrada


def terceiro(frase):
    retorno = []
    for f in range(len(frase)):
        if f >= math.trunc(len(frase)/2):
            retorno.append(chr((ord(frase[f]) - 1)))
        else:
            retorno.append(frase[f])

    return retorno


for i in range(int(input())):
    linha = input()
    pr = [primeira(i) for i in linha]
    sg = pr[::-1]
    tr = terceiro(sg)

    print("".join(tr))
