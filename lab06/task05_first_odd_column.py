# Лабораторная 6, задача 5
# Дана целочисленная матрица M x N. Найти номер первого столбца, содержащего
# только нечётные числа. Если таких нет — вывести 0.

M = int(input("Количество строк M: "))
N = int(input("Количество столбцов N: "))
matrix = []
print(f"Введите {M} строк по {N} целых чисел через пробел:")
for i in range(M):
    matrix.append(list(map(int, input().split())))

answer = 0
for j in range(N):
    all_odd = True
    for i in range(M):
        if matrix[i][j] % 2 == 0:
            all_odd = False
            break
    if all_odd:
        answer = j + 1
        break

print(answer)
