while True:
    i = int(input())
    if (i == 0):
        break

    for _ in range(i):
        l = [int(e) for e in input().split()]
        valido = len([1 for e in l if e <= 127]) == 1
        if valido:
            for j in range(len(l)):
                if l[j] <= 127:
                    print(chr(j + 65))
                    break
        else:
            print('*')
