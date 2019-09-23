def rafael(x, y):
    return (3*x)**2 + y**2


def beto(x, y):
    return 2*(x**2) + (5*y)**2


def carlos(x, y):
    return -100*x + y**3


for i in range(int(input())):
    n1, n2 = [int(j) for j in input().split()]
    n_rafael = rafael(n1, n2)
    n_beto = beto(n1, n2)
    n_carlos = carlos(n1, n2)

    maior = max(n_rafael, n_beto, n_carlos)

    if maior == n_rafael:
        print('Rafael ganhou')
    elif maior == n_beto:
        print('Beto ganhou')
    elif maior == n_carlos:
        print('Carlos ganhou')
