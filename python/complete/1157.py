n = int(input())

if n == 1:
    print(1)
else:
    x = int(n ** (1/2))

    l = [1, n]
    for i in range(2, x + 1):
        if not(n % i):
            l.append(i)
            l.append(int(n/i))

    l.sort()

    print(*l, sep='\n')
