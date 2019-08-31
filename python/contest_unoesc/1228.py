def troca(org, des, lista):
    aux = lista[org]
    lista[org] = lista[des]
    lista[des] = aux


while True:
    try:
        cont = 0
        concorrentes = int(input())
        largada = [int(i) for i in input().split()]
        chegada = [int(i) for i in input().split()]

        for i in range(concorrentes):
            while largada[i] != chegada[i]:
                

        print(cont)

    except EOFError:
        break
