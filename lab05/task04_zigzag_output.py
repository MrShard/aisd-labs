# Лабораторная 5, задача 4
# Дан массив A размера N. Вывести элементы в порядке: A1, AN, A2, AN-1, A3, AN-2, ...
# Используем два указателя: left идёт с начала, right — с конца.

parts = input("Элементы массива через пробел: ").split()
A = []
for part in parts:
    A.append(float(part))

result = []
left = 0
right = len(A) - 1
while left <= right:
    result.append(A[left])
    if left != right:          # чтобы не вывести средний элемент дважды
        result.append(A[right])
    left += 1
    right -= 1

print(result)
