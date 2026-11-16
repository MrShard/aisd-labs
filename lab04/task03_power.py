# Лабораторная 4, задача 3
# Рекурсивно возвести x в целую степень n.
#   x^0 = 1
#   x^n = x * x^(n-1)        для n > 0
#   x^n = 1 / x^(-n)         для n < 0

def power(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(x, -n)
    return x * power(x, n - 1)


x = float(input("x = "))
n = int(input("n (целое) = "))

if x == 0 and n < 0:
    print("0 нельзя возводить в отрицательную степень")
else:
    print(f"{x}^{n} = {power(x, n)}")
