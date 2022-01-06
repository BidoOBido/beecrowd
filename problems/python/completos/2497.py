cont = 0
while True:
    n = int(input())
    if n == -1:
        break

    cont += 1
    print('Experiment {}: {} full cycle(s)'.format(cont, int(n/2)))
