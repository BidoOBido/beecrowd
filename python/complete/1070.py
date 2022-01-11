x = int(input())
l = [i for i in range(x, x+12) if i % 2]

print(*l, sep='\n')
