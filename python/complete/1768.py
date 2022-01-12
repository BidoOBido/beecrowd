while True:

    try:
        n = int(input())

        def gerarEstrelas(s, n):
            return (f"{' ' * ((n - s) // 2)}{'*' * s}")


        for i in range(1, n + 1, 2):
            print(gerarEstrelas(i, n))

        print(gerarEstrelas(1, n))
        print(gerarEstrelas(3, n)+'\n')
    except EOFError:
        break
