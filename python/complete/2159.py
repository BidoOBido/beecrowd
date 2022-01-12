import math

n = int(input())

min = (n / math.log(n))

max = (1.25506 * min)

print(round(min, 1), round(max, 1))
