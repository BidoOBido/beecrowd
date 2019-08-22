def fracao(num, den):
    while den != 0:
        r = num % den
        num = den
        den = r
    if num > 0:
        return num
    else:
        return num * -1


casos = int(input())
saida = ''

for i in range(casos):
    linha = input().split()

    N1, N2 = int(linha[0]), int(linha[4])
    D1, D2 = int(linha[2]), int(linha[6])

    if linha[3] == '+':
        N, D = (N1*D2 + N2*D1), (D1*D2)
    elif linha[3] == '-':
        N, D = (N1*D2 - N2*D1), (D1*D2)
    elif linha[3] == '*':
        N, D = (N1*N2), (D1*D2)
    elif linha[3] == '/':
        N, D = (N1*D2), (N2*D1)

    S = fracao(N, D)
    saida += str(N) + '/' + str(D) + ' = '
    if S > 1:
        saida += str(int(N/S)) + '/' + str(int(D/S)) + '\n'
    else:
        saida += str(N) + '/' + str(D) + '\n'

print(saida, end='')
