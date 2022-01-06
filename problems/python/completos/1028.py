import math

n = int(input())
for _ in range(n):
    f = [int(i) for i in input().split()]
    
    print(math.gcd(f[0], f[1]))