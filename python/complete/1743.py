a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = []

for i, v in enumerate(a):
    if (v + b[i] != 1):
        print('N')
        exit()

print('Y')