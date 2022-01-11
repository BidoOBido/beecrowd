def menor_carta(jogador_carta):
    menor = 14
    for carta in jogador_carta.values():
        if carta < menor:
            menor = carta

    return menor


def remover_jogadores_inativos(menor_carta, jogador_carta):
    jogadores_ativos = []
    todas_iguais = True

    nomes = []
    for jogador, carta in jogador_carta.items():
        if menor_carta < carta:
            jogadores_ativos.append(jogador)

        if carta != menor_carta:
            todas_iguais = False

        nomes.append(jogador)

    if todas_iguais:
        return nomes

    return jogadoresAtivos


while True:
    numNomes = int(input())

    if numNomes == 0:
        break

    jogadores = input().split(" ")

    cartas = []
    for l in range(4):
        cartasLinha = [int(c) for c in input().split()]
        cartas.extend(cartasLinha)

    jogadorCarta = {}
    while len(jogadores) >= 1:

        for index, jogador in enumerate(jogadores):
            jogadorCarta[jogador] = cartas[index]

        if len(jogadores) <= len(cartas):
            cartas = cartas[len(jogadores):len(cartas)]

        jogadoresAtivos = removerJogadoresInativos(
            menorCarta(jogadorCarta), jogadorCarta)

        if jogadores == jogadoresAtivos:
            # print(jogadores, "venceram o jogo")
            break

        jogadores = jogadoresAtivos

        if len(jogadores) > len(cartas):
            # print(jogadores, "venceram o jogo e cabou o baralho")
            break

        jogadorCarta.clear()

    print(*jogadores, sep=' ', end=' ')
    print()
