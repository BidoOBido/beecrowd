while True:
    try:
        val1, val2 = [int(x) for x in input().split()]
    except EOFError:
        break
    print(int(val1 ^ val2))
