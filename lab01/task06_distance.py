# Лабораторная 1, задача 6
# Найти расстояние между двумя точками (x1, y1) и (x2, y2).
# Формула: d = sqrt((x2 - x1)^2 + (y2 - y1)^2)

import math

x1 = float(input("x1 = "))
y1 = float(input("y1 = "))
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))

dx = x2 - x1
dy = y2 - y1
distance = math.sqrt(dx ** 2 + dy ** 2)

print(f"Расстояние между точками = {distance}")
