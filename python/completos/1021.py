valor = float(input())
valor = round(valor, 2)

valores = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05, 0.01]
notas = {}

for i in valores:
    notas[i] = int(valor/i)
    valor -= (notas[i] * i)
    valor = round(valor, 2)

print("""NOTAS:
%i nota(s) de R$ 100.00
%i nota(s) de R$ 50.00
%i nota(s) de R$ 20.00
%i nota(s) de R$ 10.00
%i nota(s) de R$ 5.00
%i nota(s) de R$ 2.00
MOEDAS:
%i moeda(s) de R$ 1.00
%i moeda(s) de R$ 0.50
%i moeda(s) de R$ 0.25
%i moeda(s) de R$ 0.10
%i moeda(s) de R$ 0.05
%i moeda(s) de R$ 0.01""" % (notas[100], notas[50], notas[20], notas[10], notas[5], notas[2], notas[1], notas[0.5],
                             notas[0.25], notas[0.1], notas[0.05], notas[0.01]))
