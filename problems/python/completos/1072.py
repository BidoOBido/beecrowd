n = int(input())

nin = 0
nout = 0
for i in range(n):
    lido = int(input())
    if 10 <= lido <= 20:
        nin += 1
    else:
        nout += 1

print('%s in\n%s out' % (nin, nout))
