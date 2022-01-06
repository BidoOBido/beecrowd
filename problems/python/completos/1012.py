PI = 3.14159
linha = input().split()
A = float(linha[0])
B = float(linha[1])
C = float(linha[2])

triangulo = (A * C) / 2
circulo = PI * C ** 2
trapezio = (((A + B) * C) / 2)
quadrado = B ** 2
retangulo = A * B

print("TRIANGULO: %.3f\nCIRCULO: %.3f\nTRAPEZIO: %.3f\nQUADRADO: %.3f\nRETANGULO: %.3f" % (triangulo, circulo, trapezio,
                                                                                           quadrado, retangulo))
