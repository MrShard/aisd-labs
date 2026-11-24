# Лабораторная 5, задача 6
# Дан массив размера N и числа K, L (1 <= K <= L <= N).
# Найти среднее арифметическое элементов с номерами от K до L включительно.

parts = input("Элементы массива через пробел: ").split()
arr = []
for part in parts:
    arr.append(float(part))
K = int(input("K = "))
L = int(input("L = "))

if not (1 <= K <= L <= len(arr)):
    print("Неверные K и L")
else:
    total = 0
    for number in range(K, L + 1):
        total += arr[number - 1]       # номер -> индекс
    print(f"Среднее = {total / (L - K + 1)}")
