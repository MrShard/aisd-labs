# Лабораторная 5, задача 7
# Дан целочисленный массив без одинаковых чисел. Проверить, образуют ли элементы
# арифметическую прогрессию. Если да — вывести разность, иначе 0.

arr = list(map(int, input("Элементы массива через пробел: ").split()))

d = arr[1] - arr[0]
is_progression = True
for i in range(2, len(arr)):
    if arr[i] - arr[i - 1] != d:
        is_progression = False
        break                      # дальше проверять не нужно

print(d if is_progression else 0)
