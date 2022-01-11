def calcular(x, text):
    sum = 0
    for i in range(len(text)):
        sum = sum + (ord(text[i]) - 65) + x + i

    return sum


for _ in range(int(input())):
    n = 0
    for i in range(int(input())):
        n = n + calcular(i, input())
    print(n)
