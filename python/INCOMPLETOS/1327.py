import sys
from collections import Counter, deque


def cartas_repetida(jogadores_cr):
    ocorrencias = Counter(jogadores_cr)
    return ocorrencias.most_common()


if __name__ == "__main__":
    menor = sys.maxsize
    vencedores = []

    while True:
        n_nomes = int(input())
        if n_nomes == 0:
            break

        cartas = deque([])
        jogadores = {}
        nomes = input().split()

        for i in range(4):
            lido = [int(j) for j in input().split()]
            cartas.extend(lido)

        while True:  # Falta realizar a validação de fim de jogo
            for i in range(n_nomes):
                jogadores[nomes[i]] = cartas.popleft()

            menores = []

            for nome_menor, carta_menor in jogadores.items():
                if carta_menor < menor:
                    menores.clear()
                    menores.append(nome_menor)
                    menor = carta_menor
                elif carta_menor == menor:
                    menores.append(nome_menor)

            if menor not in cartas_repetida(jogadores):
                n_nomes -= len(menores)
                for eliminado in menores:
                    nomes.pop(nomes.index(eliminado))

        vencedores.append(*nomes, sep=' ')

    print(*vencedores, sep='\n')
