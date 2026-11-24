# Лабораторная 5, задача 7
# Дан целочисленный массив без одинаковых чисел. Проверить, образуют ли элементы
# арифметическую прогрессию. Если да — вывести разность, иначе 0.

parts = input("Элементы массива через пробел: ").split()
arr = []
for part in parts:
    arr.append(int(part))

if len(arr) < 2:
    print(0)
else:
    d = arr[1] - arr[0]
    is_progression = True
    for i in range(2, len(arr)):
        if arr[i] - arr[i - 1] != d:
            is_progression = False
            break

    if is_progression:
        print(d)
    else:
        print(0)
