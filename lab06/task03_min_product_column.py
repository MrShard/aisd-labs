# Лабораторная 6, задача 3
# Дана матрица M x N. Найти номер столбца с наименьшим произведением элементов
# и вывести этот номер и само произведение.

M = int(input("Количество строк M: "))
N = int(input("Количество столбцов N: "))
matrix = []
print(f"Введите {M} строк по {N} чисел через пробел:")
for i in range(M):
    matrix.append(list(map(float, input().split())))

best_column = 0
best_product = None
for j in range(N):
    product = 1
    for i in range(M):
        product *= matrix[i][j]
    if best_product is None or product < best_product:
        best_product = product
        best_column = j

print(f"Столбец номер {best_column + 1}, произведение = {best_product}")
