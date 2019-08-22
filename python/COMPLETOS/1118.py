def calculo():
    valida = 0
    invalida = 0
    soma = 0

    while valida != 2:
        nota = float(input())

        if 0 <= nota <= 10:
            valida += 1
            soma += nota
        else:
            invalida += 1

    for i in range(invalida):
        print('nota invalida')

    print('media = %.2f' % float(soma/2))


novo = 1
while novo == 1:
    novo = 0
    calculo()
    while not 1 <= novo <= 2:
        novo = int(input('novo calculo (1-sim 2-nao)\n'))
