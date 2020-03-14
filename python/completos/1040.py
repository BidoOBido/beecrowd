def main():
    def media(*args):
        return sum(args) / len(args)

    n1 = float(input())
    n2 = float(input())
    n3 = float(input())
    n4 = float(input())

    nmedia = media(n1, n2, n3, n4)

    if nmedia < 5.0:
        print('Aluno reprovado.')
        exit
    elif nmedia > 7.0:
        print('Aluno aprovado.')
        exit
    else:
        exame = input('Nota do exame: ')
        nmedia = media(nmedia, exame)

        if nmedia >= 5.0




if __name__ == "__main__":
    main()
