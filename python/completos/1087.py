def indiceDiagonalPrincipal(x, y):
    return x - y


def indiceDiagonalReversa(x, y):
    return (9-x) - y


def isDiagonal(x1, y1, x2, y2):
    return indiceDiagonalPrincipal(x1, y1) == indiceDiagonalPrincipal(x2, y2) or indiceDiagonalReversa(x1, y1) == indiceDiagonalReversa(x2, y2)


while True:
    x1, y1, x2, y2 = [int(x) for x in input().split()]

    if x1+y1+x2+y2 == 0:
        break

    r = -1

    if (x1 == x2) and (y1 == y2):
        r = 0
    elif (x1 == x2 or y1 == y2) or (isDiagonal(x1, y1, x2, y2)):
        r = 1
    else:
        r = 2

    print(r)
