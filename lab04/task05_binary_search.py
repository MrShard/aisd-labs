# Лабораторная 4, задача 5
# Рекурсивный бинарный поиск элемента в отсортированном массиве.
# Возвращает индекс элемента или -1, если его нет.

def binary_search(arr, target, left, right):
    if left > right:              # область поиска пуста — элемента нет
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] > target:         # искомое левее середины
        return binary_search(arr, target, left, mid - 1)
    return binary_search(arr, target, mid + 1, right)   # искомое правее


parts = input("Отсортированный массив через пробел: ").split()
arr = []
for part in parts:
    arr.append(int(part))
target = int(input("Что ищем: "))

index = binary_search(arr, target, 0, len(arr) - 1)
if index == -1:
    print("Элемент не найден")
else:
    print(f"Элемент найден, индекс = {index} (номер {index + 1})")
