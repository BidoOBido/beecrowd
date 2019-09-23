import collections as col

quantidade_corridas, pilotos = [int(i) for i in input().split()]

# le a posicao dos pilotos
posicoes = []
for i in range(quantidade_corridas):
    classificacao = {}
    posicao_aux = [int(j) for j in input().split()]
    for k in range(1, pilotos+1):
        classificacao[k] = posicao_aux[k-1]
    posicoes.append(classificacao)

# le os sistemas de pontuacao
sistemas_pontuacao = []
for l in range(int(input())):
    sistemas_pontuacao.append([int(m) for m in input().split()])

# calcula saidas
for n in range(quantidade_corridas):
    # saida = []
    for o in range(sistemas_pontuacao[n][0]):  # para os k pilotos que ganham pontos
        pontuacao = {}
        for p in range(1, pilotos + 1):
            aux = pontuacao.get(p, 0) + sistemas_pontuacao[o][posicoes[n][p]]
            pontuacao[p] = aux

        # saida.append(col.Counter(pontuacao))
        print(col.Counter(pontuacao).most_common(1))


