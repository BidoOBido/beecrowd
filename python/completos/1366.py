while True:
    tamanhos = int(input())
    if tamanhos == 0:
        break

    retangulos = 0
    meios = 0
    for i in range(tamanhos):
        tamanho, quantidade = [int(i) for i in input().split()]

        if quantidade >= 4:
            retangulos += int(quantidade / 4)
            quantidade = quantidade % 4

        meios += int(quantidade / 2)

    retangulos += int(meios / 2)

    print(retangulos)
