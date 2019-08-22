dias = int(input())
anos = int(dias/365)
dias -= (anos * 365)
mes = int(dias/30)
dias -= (mes * 30)

print("%i ano(s)\n%i mes(es)\n%i dia(s)" % (anos, mes, dias))
