# Лабораторная 5, задача 2
# Дано N (> 1), первый член A и знаменатель D геометрической прогрессии.
# Сформировать массив из N первых членов: A, A*D, A*D^2, ...

N = int(input("N = "))
A = float(input("A = "))
D = float(input("D = "))

arr = [A]
for i in range(1, N):
    arr.append(arr[-1] * D)

print(arr)
