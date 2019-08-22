from collections import Counter

valores = Counter([])
sub = [('C', 'coelhos'), ('R', 'ratos'), ('S', 'sapos')]
for i in range(int(input())):
    entrada = input().split()
    valores[entrada[1]] += int(entrada[0])

total = sum(valores.values())
totais = []
percentuais = []

for chave, valor in sub:
    percentual = float((valores[chave]/total) * 100)

    totais.append('Total de %s: %i' % (valor, valores[chave]))
    percentuais.append('Percentual de %s: %.2f %s' % (valor, percentual, '%'))

print('Total: %s cobaias' % total)
print(*totais, sep='\n')
print(*percentuais, sep='\n')
