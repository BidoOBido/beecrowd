p = []
t = []
for _ in range(3):
    p.append(int(input()))

t.append(p[1] * 2 + p[2] * 4)
t.append(p[0] * 2 + p[2] * 2)
t.append(p[0] * 4 + p[1] * 2)

print(min(t))
