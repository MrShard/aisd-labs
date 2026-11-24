# Лабораторная 6, задача 6
# Дана матрица M x N. В каждой строке поменять местами минимальный и максимальный элементы.

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

for row in matrix:
    min_index = 0
    max_index = 0
    for j in range(N):
        if row[j] < row[min_index]:
            min_index = j
        if row[j] > row[max_index]:
            max_index = j
    saved_value = row[min_index]
    row[min_index] = row[max_index]
    row[max_index] = saved_value

print("Результат:")
for row in matrix:
    for i in range(len(row)):
        if i > 0:
            print(" ", end="")
        print(row[i], end="")
    print()
