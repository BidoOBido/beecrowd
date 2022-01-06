n = [float(i) for i in input().split()]
m = float(n[0] * 0.2 + n[1] * 0.3 + n[2] * 0.4 + n[3] * 0.1)

print('Media: {:.1f}'.format(m))

if m >= 7:
    print('Aluno aprovado.')
elif m < 5:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    ne = float(input())
    print('Nota do exame: {:.1f}'.format(ne))
    nme = (m + ne) / 2
    if nme >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado')
    print('Media final: {:.1f}'.format(nme))
