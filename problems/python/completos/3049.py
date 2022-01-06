metade_area_total = (70 * 160) / 2


def areaTrapezio(altura, base_menor, base_maior):
    return ((base_maior + base_menor) * altura) / 2


b, t = int(input()), int(input())

area = areaTrapezio(70, b, t)

if area == metade_area_total:
    print(0)
elif area > metade_area_total:
    print(1)
else:
    print(2)
