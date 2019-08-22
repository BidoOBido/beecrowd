n = int(input())

s = n * 4

for i in range(1, s+1):
    if i % 4 == 0:
        print('PUM')
    else:
        print('%s' % i, end=' ')
