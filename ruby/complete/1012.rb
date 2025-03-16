A, B, C = gets.chomp.split(" ").map(&:to_f)
PI = 3.14159

TRIANGULO = (A * C) / 2
CIRCULO = PI * C * C
TRAPEZIO = ((A + B) * C) / 2
QUADRADO = B * B
RETANGULO = A * B


puts format("TRIANGULO: %.3f\nCIRCULO: %.3f\nTRAPEZIO: %.3f\nQUADRADO: %.3f\nRETANGULO: %.3f",
TRIANGULO, CIRCULO, TRAPEZIO, QUADRADO, RETANGULO)
