def calcula(pos, poslu, poskang):
    meio = (pos + 1) / 2
    valor = pos
    if poslu <= meio and poskang <= meio:
        valor = calcula(meio, poslu, poskang)
    elif poslu > meio and poskang > meio:
        valor = calcula(meio, (poslu-meio), (poskang-meio))

    return valor


lista = input().split()
lu = lista.index('9')
kang = lista.index('1')

part = len(lista)
res = calcula(part, lu, kang)

if res == 16:
    print('final')
elif res == 8:
    print('semifinal')
elif res == 4:
    print('quartas')
elif res == 1:
    print('oitavas')
