for t in range(int(input())):
    maior = 0
    caminho = {}

    n, d = [int(i) for i in (input().split())]
    pedras = input().split()

    for i in range(len(pedras)):
        tam, dist = pedras[i].split('-')
        caminho[int(dist)] = tam

    pos = 0
    for dist, tam in list(caminho.items()):
        passo = dist - pos
        if passo > maior:
            maior = passo

        if tam == 'S':
            caminho.pop(dist, None)

    print(maior)
