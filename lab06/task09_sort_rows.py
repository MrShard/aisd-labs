# Лабораторная 6, задача 9
# Дана матрица M x N. Упорядочить строки так, чтобы их первые элементы
# образовывали возрастающую последовательность.
# Сортируем строки целиком, сравнивая их по первому элементу (сортировка вставками).

M = int(input("Количество строк M: "))
N = int(input("Количество столбцов N: "))
matrix = []
print(f"Введите {M} строк по {N} чисел через пробел:")
for i in range(M):
    matrix.append(list(map(float, input().split())))

for i in range(1, M):
    current_row = matrix[i]
    j = i - 1
    while j >= 0 and matrix[j][0] > current_row[0]:
        matrix[j + 1] = matrix[j]     # сдвигаем строку вниз
        j -= 1
    matrix[j + 1] = current_row

print("Результат:")
for row in matrix:
    print(*row)
