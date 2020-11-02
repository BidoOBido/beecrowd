n = int(input())
c = int(input())
v = []

for _ in range(n):
    v.append(int(input()))

bS = 0
cS = 0

for i in v:
    cS = max(0, cS + (i-c))
    bS = max(bS, cS)

print(bS)
