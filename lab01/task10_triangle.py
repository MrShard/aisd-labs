# Лабораторная 1, задача 10
# Даны координаты трёх вершин треугольника. Найти его периметр и площадь.
# Стороны считаем как расстояния между вершинами,
# площадь — по формуле Герона: S = sqrt(p(p-a)(p-b)(p-c)), где p — полупериметр.

import math

x1 = float(input("x1 = "))
y1 = float(input("y1 = "))
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))
x3 = float(input("x3 = "))
y3 = float(input("y3 = "))

a = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
b = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
c = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)

P = a + b + c
p = P / 2
under_root = p * (p - a) * (p - b) * (p - c)
if under_root < 0:
    under_root = 0
S = math.sqrt(under_root)

print(f"Периметр P = {P}")
print(f"Площадь S = {S}")
