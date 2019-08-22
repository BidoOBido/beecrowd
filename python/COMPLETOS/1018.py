valor = int(input())
saida = valor

valores = [100, 50, 20, 10, 5, 2, 1]
notas = {}

for i in valores:
    notas[i] = int(valor/i)
    valor -= (notas[i] * i)


print("""%i
%i nota(s) de R$ 100,00
%i nota(s) de R$ 50,00
%i nota(s) de R$ 20,00
%i nota(s) de R$ 10,00
%i nota(s) de R$ 5,00
%i nota(s) de R$ 2,00
%i nota(s) de R$ 1,00""" % (saida, notas[100], notas[50], notas[20], notas[10], notas[5], notas[2], notas[1]))
