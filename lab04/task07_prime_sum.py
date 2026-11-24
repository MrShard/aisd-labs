# Лабораторная 4, задача 7
# Рекурсивно разложить число на сумму простых чисел.
# Идея: берём наибольшее простое p <= n, такое что остаток n - p можно разложить
# (остаток 1 разложить нельзя), и рекурсивно раскладываем остаток.
# Пример: 10 = 7 + 3, 11 = 11, 27 = 23 + 2 + 2


def is_prime(k):
    if k < 2:
        return False
    d = 2
    while d * d <= k:
        if k % d == 0:
            return False
        d += 1
    return True


def decompose(n):
    """Возвращает список простых чисел с суммой n или None, если разложить нельзя."""
    if n == 0:
        return []                      # разложили полностью
    for p in range(n, 1, -1):
        if is_prime(p) and n - p != 1:
            rest = decompose(n - p)
            if rest is not None:
                return [p] + rest
    return None


n = int(input("Введите число (>= 2): "))
result = decompose(n)

if result is None:
    print("Число нельзя разложить на сумму простых")
else:
    text = f"{n} = "
    for i in range(len(result)):
        if i > 0:
            text += " + "
        text += str(result[i])
    print(text)
