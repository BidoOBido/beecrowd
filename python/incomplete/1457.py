def fatorial(numero, fator):
    if numero < 0:
        return 1
    else:
        return fatorial(numero, (3 * fator))


n = int(input())

for _ in range(n):
    entrada = input()
    n = int(entrada.replace("!", ""))
    k = len(entrada.replace(str(n), ""))

    print(n, k)
