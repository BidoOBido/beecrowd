import sys


def fibonacci(n):
    Phi = (1 + pow(5, .5)) / 2
    phi = (-1) / Phi

    calculo = pow(Phi, n) - pow((phi), n)

    return round(calculo) / pow(5, .5)


case_counter = 0

while True:
    counter = 0
    case_counter += 1
    valor, base = [int(i) for i in input().split()]

    if (valor == 0) and (base == 0):
        break

    resultado = round(2 * fibonacci(valor+1) - 1) % base
    print('Case {}: {} {} {}'.format(case_counter, valor, base, resultado))

 # 0 1 1 2 3 5 8 13 21
