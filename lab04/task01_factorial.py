# Лабораторная 4, задача 1
# Рекурсивно вычислить факториал n: n! = n * (n-1)!, 0! = 1.

def factorial(n):
    if n <= 1:           # базовый случай — здесь рекурсия останавливается
        return 1
    return n * factorial(n - 1)


n = int(input("n = "))
if n < 0:
    print("Факториал отрицательного числа не определён")
else:
    print(f"{n}! = {factorial(n)}")
