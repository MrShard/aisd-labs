# Лабораторная 6, задача 8
# Дана матрица M x N (M и N чётные). Поменять местами левую верхнюю
# и правую нижнюю четверти матрицы.

M = int(input("Количество строк M (чётное): "))
N = int(input("Количество столбцов N (чётное): "))
matrix = []
print(f"Введите {M} строк по {N} чисел через пробел:")
for i in range(M):
    matrix.append(list(map(float, input().split())))

half_m = M // 2
half_n = N // 2
for i in range(half_m):
    for j in range(half_n):
        # элемент (i, j) левой верхней четверти соответствует
        # элементу (i + half_m, j + half_n) правой нижней
        i2 = i + half_m
        j2 = j + half_n
        matrix[i][j], matrix[i2][j2] = matrix[i2][j2], matrix[i][j]

print("Результат:")
for row in matrix:
    print(*row)
