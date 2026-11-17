# Лабораторная 6, задача 1
# Дана квадратная матрица порядка M (M нечётное). Начиная с A[1][1], двигаясь против
# часовой стрелки, вывести элементы по спирали: первый столбец (вниз), последняя строка
# (вправо), последний столбец (вверх), первая строка (влево), затем следующий «виток»...
# Последним выводится центральный элемент.

M = int(input("Порядок матрицы M (нечётное): "))
A = []
print(f"Введите {M} строк по {M} чисел через пробел:")
for i in range(M):
    A.append(list(map(int, input().split())))

result = []
top, bottom, left, right = 0, M - 1, 0, M - 1   # границы текущего витка

while top <= bottom:
    if top == bottom:                    # остался центральный элемент
        result.append(A[top][left])
        break
    for i in range(top, bottom + 1):     # вниз по левому столбцу
        result.append(A[i][left])
    for j in range(left + 1, right + 1): # вправо по нижней строке
        result.append(A[bottom][j])
    for i in range(bottom - 1, top - 1, -1):   # вверх по правому столбцу
        result.append(A[i][right])
    for j in range(right - 1, left, -1):       # влево по верхней строке
        result.append(A[top][j])
    # сужаем границы — переходим к внутреннему витку
    top += 1
    bottom -= 1
    left += 1
    right -= 1

print(*result)
