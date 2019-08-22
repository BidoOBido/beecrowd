p1 = [float(i) for i in (input().split())]
p2 = [float(i) for i in (input().split())]

dist = ((((p2[0]-p1[0])**2) + ((p2[1]-p1[1])**2))**(1/2))

print("%.4f" % dist)
