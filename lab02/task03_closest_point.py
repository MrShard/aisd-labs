# Лабораторная 2, задача 3
# На плоскости точки A, B, C. Определить, какая из точек B или C ближе к A,
# и вывести эту точку и её расстояние от A.

import math

xa = float(input("xA = "))
ya = float(input("yA = "))
xb = float(input("xB = "))
yb = float(input("yB = "))
xc = float(input("xC = "))
yc = float(input("yC = "))

dist_ab = math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)
dist_ac = math.sqrt((xc - xa) ** 2 + (yc - ya) ** 2)

if dist_ab < dist_ac:
    print(f"Ближе точка B({xb}, {yb}), расстояние = {dist_ab}")
elif dist_ac < dist_ab:
    print(f"Ближе точка C({xc}, {yc}), расстояние = {dist_ac}")
else:
    print(f"Точки B и C находятся на одинаковом расстоянии = {dist_ab}")
