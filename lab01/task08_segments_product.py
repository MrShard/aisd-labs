# Лабораторная 1, задача 8
# Даны три точки A, B, C на числовой оси, C лежит между A и B.
# Найти произведение длин отрезков AC и BC.

A = float(input("Координата точки A: "))
B = float(input("Координата точки B: "))
C = float(input("Координата точки C (между A и B): "))

AC = abs(A - C)
BC = abs(B - C)

print(f"AC = {AC}, BC = {BC}")
print(f"AC * BC = {AC * BC}")
