# Лабораторная 6, задача 7
# Дана матрица M x N. Поменять местами столбцы, содержащие минимальный
# и максимальный элементы всей матрицы.

M = int(input("Количество строк M: "))
N = int(input("Количество столбцов N: "))
matrix = []
print(f"Введите {M} строк по {N} чисел через пробел:")
for i in range(M):
    parts = input().split()
    row = []
    for part in parts:
        row.append(float(part))
    matrix.append(row)

min_col = 0
max_col = 0
min_value = matrix[0][0]
max_value = matrix[0][0]
for i in range(M):
    for j in range(N):
        if matrix[i][j] < min_value:
            min_value = matrix[i][j]
            min_col = j
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
            max_col = j

# меняем местами элементы двух столбцов в каждой строке
for i in range(M):
    saved_value = matrix[i][min_col]
    matrix[i][min_col] = matrix[i][max_col]
    matrix[i][max_col] = saved_value

print(f"Минимум в столбце {min_col + 1}, максимум в столбце {max_col + 1}")
if min_col == max_col:
    print("Это один и тот же столбец — матрица не меняется")
print("Результат:")
for row in matrix:
    for i in range(len(row)):
        if i > 0:
            print(" ", end="")
        print(row[i], end="")
    print()
