segundos = int(input())
minutos = int(segundos/60)
segundos -= (minutos * 60)
horas = int(minutos/60)
minutos -= (horas*60)

print("%i:%i:%i" % (horas, minutos, segundos))
