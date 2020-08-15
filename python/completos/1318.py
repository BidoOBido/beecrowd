while True:
  n, m = [int(c) for c in input().split()]
  if (n == m and m == 0):
    break
  
  l = [int(c) for c in input().split()]
  l.sort()

  ant = -1
  aux = -1
  rep = 0

  for i in l:
    if (ant == i and aux != i):
      aux = i
      rep = rep + 1

    ant = i

  print(rep)
