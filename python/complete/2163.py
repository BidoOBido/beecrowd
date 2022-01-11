def isSabre(x, y):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i != 0 and j != 0) and (mx[x+i][y+j] != 7):
                return False

    return True


n, m = [int(i) for i in input().split()]
mx = []
for _ in range(n):
    mx.append([int(i) for i in input().split()])

rx, ry = 0, 0
for li in range(1, len(mx) - 1):
    for ci in range(1, len(mx[li]) - 1):
        if mx[li][ci] == 42:
            if isSabre(li, ci):
                rx, ry = li+1, ci+1
                break
    if (rx + ry) > 0:
        break

print('{} {}'.format(rx, ry))
