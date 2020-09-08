while True:
    h1, m1, h2, m2 = [int(e) for e in input().split()]

    if (h1 + m1 + h2 + m2) == 0:
        break

    hm1 = h1*60 + m1
    hm2 = h2*60 + m2

    if hm1 > hm2:
        hm2 = hm2 + 1440

    print(hm2-hm1)
