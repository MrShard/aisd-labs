# Лабораторная 6, задача 2
# Дана матрица M x N и число K (1 <= K <= M). Найти сумму и произведение элементов K-й строки.

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

K = int(input(f"K (1..{M}): "))

row = matrix[K - 1]       # строка с номером K имеет индекс K-1
total = 0
product = 1
for x in row:
    total += x
    product *= x

print(f"Сумма = {total}, произведение = {product}")
