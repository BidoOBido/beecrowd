valida = 0
invalida = 0
soma = 0

while True:
    nota = float(input())

    if 0 <= nota <= 10:
        valida += 1
        soma += nota
    else:
        invalida += 1

    if valida == 2:
        break

for i in range(invalida):
    print('nota invalida')

print('media = %.2f' % float(soma/2))

