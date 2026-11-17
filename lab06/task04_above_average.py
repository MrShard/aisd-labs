# Лабораторная 6, задача 4
# Дана матрица M x N. В каждом столбце найти количество элементов,
# больших среднего арифметического этого столбца.

M = int(input("Количество строк M: "))
N = int(input("Количество столбцов N: "))
matrix = []
print(f"Введите {M} строк по {N} чисел через пробел:")
for i in range(M):
    matrix.append(list(map(float, input().split())))

for j in range(N):
    column = [matrix[i][j] for i in range(M)]
    average = sum(column) / M
    count = 0
    for x in column:
        if x > average:
            count += 1
    print(f"Столбец {j + 1}: среднее = {average:.2f}, больше среднего: {count}")
