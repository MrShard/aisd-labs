# Лабораторная 3, задача 6
# Даны целые A < B. Вывести все числа от A до B включительно,
# каждое число столько раз, каково его значение (3 выводится 3 раза).

A = int(input("A = "))
B = int(input("B = "))

for number in range(A, B + 1):
    for _ in range(number):
        print(number, end=" ")
    print()
