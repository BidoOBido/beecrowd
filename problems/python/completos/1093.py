import math

while True:
    ev1, ev2, at, d = [int(e) for e in input().split()]

    if ((ev1 + ev2 + at + d) == 0):
        break

    p = at/6

    ev1 = math.ceil(ev1/d)
    ev2 = math.ceil(ev2/d)

    if (p == 0.5):
        p1 = ev2/(ev1+ev2)
        print('{:.1f}'.format((1 - p1)*100))
    else:
        q = 1 - p

        p1 = (1-(p/q)**ev2)/(1-(p/q)**(ev1+ev2))

        print('{:.1f}'.format((1 - p1)*100))
