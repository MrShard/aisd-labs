# Лабораторная 4, задача 2
# Рекурсивно вычислить n-е число Фибоначчи: F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2).
# Внимание: простая рекурсия работает медленно для n > 35 (много повторных вызовов).

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("n = "))
if n < 0:
    print("n должно быть неотрицательным")
else:
    print(f"F({n}) = {fibonacci(n)}")
