# Лабораторная 5, задача 5
# Дан массив A размера N. Вывести сначала элементы с нечётными номерами по возрастанию номеров,
# затем элементы с чётными номерами по убыванию номеров.
# Номера в задаче начинаются с 1, а индексы в Python — с 0:
# номер 1 -> индекс 0, номер 2 -> индекс 1 и т. д.

parts = input("Элементы массива через пробел: ").split()
A = []
for part in parts:
    A.append(float(part))
N = len(A)

result = []
# Нечётные номера 1, 3, 5, ... = индексы 0, 2, 4, ...
for i in range(0, N, 2):
    result.append(A[i])

last_even_number = N
if N % 2 != 0:
    last_even_number = N - 1
for number in range(last_even_number, 0, -2):
    result.append(A[number - 1])

print(result)
