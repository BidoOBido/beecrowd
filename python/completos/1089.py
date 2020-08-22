while True:
    # Número de entradas
    n = int(input())
    # Teste da entrada
    if (n == 0):
        break
    # Entrada das magnitudes
    m = [int(i) for i in input().split()]
    mx = m.index(max(m))

    crescendo = False
    pico = 1
    for i in range(len(m)):
        idx = (mx+i) % len(m)
        nIdx = (idx+1) % len(m)
        if (((m[nIdx] - m[idx]) > 0) != crescendo):
            crescendo = not(crescendo)
            pico = pico + 1

    print(pico)
