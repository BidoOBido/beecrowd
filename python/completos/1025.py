caso = 0


def _resposta(_lpecas, _lpalpites):
    retorno = []

    for _palpite in _lpalpites:
        if _lpecas.count(_palpite) == 0:
            retorno.append('{} not found'.format(_palpite))
        else:
            retorno.append('{} found at {}'.format(
                _palpite, _lpecas.index(_palpite)+1))

    return retorno


while True:
    pecas, palpites = [int(i) for i in (input().split())]

    if (pecas == 0 and palpites == 0):
        break

    caso += 1
    lista_pecas = []
    lista_palpites = []

    for _ in range(pecas):
        lista_pecas.append(int(input()))

    for _ in range(palpites):
        lista_palpites.append(int(input()))

    lista_pecas.sort()
    print('CASE# {}:'.format(caso))
    print(*_resposta(lista_pecas, lista_palpites), sep='\n')
