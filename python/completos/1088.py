import math


def mergeSort(lista):
    global contador

    if len(lista) > 1:
        meio = len(lista) // 2

        primeiraParte = lista[:meio]
        segundaParte = lista[meio:]

        mergeSort(primeiraParte)
        mergeSort(segundaParte)

        i, j, k = 0, 0, 0

        while i < len(primeiraParte) and j < len(segundaParte):
            if primeiraParte[i] < segundaParte[j]:
                lista[k] = primeiraParte[i]
                i += 1
            else:
                lista[k] = segundaParte[j]
                j += 1
            k += 1

        while i < len(primeiraParte):
            lista[k] = primeiraParte[i]
            i += 1
            k += 1

        while j < len(segundaParte):
            lista[k] = segundaParte[j]
            j += 1
            k += 1

        contador += k / 2


while True:
    v = [int(e) for e in input().split()]
    n = v.pop(0)

    if n == 0:
        break

    global contador
    contador = 0

    mergeSort(v)

    if (contador // 2) % 2:
        print('Carlos')
    else:
        print('Marcelo')
