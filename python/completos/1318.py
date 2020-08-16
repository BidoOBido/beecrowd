from itertools import groupby

while True:
    n, m = [int(c) for c in input().split()]
    if (n == m and m == 0):
        break

    l = [int(c) for c in input().split()]
    l.sort()

    print(len([1 for key, group in groupby(l) if len(list(group)) > 1]))
