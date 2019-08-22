from functools import lru_cache

#@lru_cache(maxsize=1000)
def fibonacci(num, mod):
    global counter
    counter += 1
    if num <= 1:
        return num
    else:
        return (fibonacci(num-1, u)+fibonacci(num-2, u)) % mod


n, u = -1, -1

while (n != 0) or (u != 0):
    counter = 0
    linha = [int(i) for i in input().split()]
    n, u = linha

    fibonacci(n, u)
    print(counter)
