# Лабораторная 5, задача 9
# Дан массив размера N. Найти номер его последнего локального максимума
# (элемента, который больше любого из своих соседей).
# У крайних элементов только один сосед.

parts = input("Элементы массива через пробел: ").split()
arr = []
for part in parts:
    arr.append(float(part))
N = len(arr)

answer = 0      # 0 — если локальных максимумов нет
for i in range(N):
    bigger_than_left = True
    bigger_than_right = True
    if i > 0:
        bigger_than_left = arr[i] > arr[i - 1]
    if i < N - 1:
        bigger_than_right = arr[i] > arr[i + 1]
    if bigger_than_left and bigger_than_right:
        answer = i + 1          # запоминаем номер (с 1); в итоге останется последний

print(f"Номер последнего локального максимума: {answer}")
