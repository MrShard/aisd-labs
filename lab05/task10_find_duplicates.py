# Лабораторная 5, задача 10
# Дан целочисленный массив, содержащий ровно два одинаковых элемента.
# Найти номера одинаковых элементов и вывести их по возрастанию.

parts = input("Элементы массива через пробел: ").split()
arr = []
for part in parts:
    arr.append(int(part))
N = len(arr)

found = False
for i in range(N):
    for j in range(i + 1, N):          # сравниваем каждую пару (i < j) один раз
        if arr[i] == arr[j]:
            print(f"Номера одинаковых элементов: {i + 1} {j + 1}")
            found = True
            break
    if found:
        break

if not found:
    print("Одинаковых элементов нет")
