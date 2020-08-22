s = 0
for _ in range(5):
    if not(int(input()) % 2):
        s = s + 1

print('{} valores pares'.format(s))
