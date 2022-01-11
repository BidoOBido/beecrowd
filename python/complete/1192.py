for _ in range(int(input())):
    c = input()
    n0, n2 = int(c[0]), int(c[2])
    if n0 == n2:
        print(n0*n2)
    elif (c[1].isupper()):
        print(n2-n0)
    elif (c[1].islower()):
        print(n0+n2)
