def troca(org, des, lista):
    temp = lista[org]
    lista[org] = lista[des]
    lista[des] = temp


while True:
    try:
        concorrentes = int(input())
        largada = [int(n) for n in input().split()]
        chegada = [int(n) for n in input().split()]
        aux = [0] * concorrentes

        for i in range(concorrentes):
            for j in range(concorrentes):
                if largada[i] == chegada[j]:
                    aux[j] = i + concorrentes

        cont = 0
        for i in range(concorrentes):
            for j in range(i+1, concorrentes):
                if aux[i] > aux[j]:
                    troca(i, j, aux)
                    cont += 1

        print(cont)

    except EOFError:
        break
