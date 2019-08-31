import collections

lista = []

for i in range(int(input())):
    lista.append(int(input()))

lista = collections.Counter(lista)

for k, v in sorted(lista.items()):
    print('{} aparece {} vez(es)'.format(k, v))
