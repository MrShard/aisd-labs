"""Лабораторная работа № 4 «Рекурсия». Объединённый запуск."""


def task01_factorial(read_input):
    # Лабораторная 4, задача 1
    # Рекурсивно вычислить факториал n: n! = n * (n-1)!, 0! = 1.

    def factorial(n):
        if n <= 1:           # базовый случай — здесь рекурсия останавливается
            return 1
        return n * factorial(n - 1)


    n = int(read_input("n = "))
    if n < 0:
        print("Факториал отрицательного числа не определён")
    else:
        print(f"{n}! = {factorial(n)}")


def task02_fibonacci(read_input):
    # Лабораторная 4, задача 2
    # Рекурсивно вычислить n-е число Фибоначчи: F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2).
    # Внимание: простая рекурсия работает медленно для n > 35 (много повторных вызовов).

    def fibonacci(n):
        if n < 2:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)


    n = int(read_input("n = "))
    if n < 0:
        print("n должно быть неотрицательным")
    else:
        print(f"F({n}) = {fibonacci(n)}")


def task03_power(read_input):
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


    x = float(read_input("x = "))
    n = int(read_input("n (целое) = "))

    if x == 0 and n < 0:
        print("0 нельзя возводить в отрицательную степень")
    else:
        print(f"{x}^{n} = {power(x, n)}")


def task04_palindrome(read_input):
    # Лабораторная 4, задача 4
    # Рекурсивно проверить, является ли строка палиндромом.
    # Идея: строка — палиндром, если первый и последний символы равны
    # и середина (без них) тоже палиндром. Пустая строка и строка из 1 символа — палиндромы.

    def is_palindrome(s):
        if len(s) <= 1:
            return True
        if s[0] != s[-1]:
            return False
        return is_palindrome(s[1:-1])


    text = read_input("Введите строку: ")
    # Убираем пробелы и знаки препинания, приводим к нижнему регистру,
    # чтобы «А роза упала на лапу Азора» тоже считалась палиндромом
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())

    if is_palindrome(cleaned):
        print("Это палиндром")
    else:
        print("Это не палиндром")


def task05_binary_search(read_input):
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


    arr = list(map(int, read_input("Отсортированный массив через пробел: ").split()))
    target = int(read_input("Что ищем: "))

    index = binary_search(arr, target, 0, len(arr) - 1)
    if index == -1:
        print("Элемент не найден")
    else:
        print(f"Элемент найден, индекс = {index} (номер {index + 1})")


def task06_reverse_words(read_input):
    # Лабораторная 4, задача 6
    # Рекурсивно поменять порядок слов в строке на обратный.
    # Идея: reverse(["a", "b", "c"]) = reverse(["b", "c"]) + ["a"]

    def reverse_words(words):
        if len(words) <= 1:
            return words
        return reverse_words(words[1:]) + [words[0]]


    text = read_input("Введите строку: ")
    words = text.split()
    print(" ".join(reverse_words(words)))


def task07_prime_sum(read_input):
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


    n = int(read_input("Введите число (>= 2): "))
    result = decompose(n)

    if result is None:
        print("Число нельзя разложить на сумму простых")
    else:
        print(f"{n} = " + " + ".join(str(p) for p in result))


def task08_count_digits(read_input):
    # Лабораторная 4, задача 8
    # Рекурсивно подсчитать количество цифр в числе.
    # Идея: если число < 10, в нём одна цифра; иначе 1 + количество цифр в n // 10.

    def count_digits(n):
        if n < 10:
            return 1
        return 1 + count_digits(n // 10)


    n = int(read_input("Введите целое число: "))
    print(f"Количество цифр: {count_digits(abs(n))}")


def task09_hanoi(read_input):
    # Лабораторная 4, задача 9
    # Рекурсивное решение головоломки «Ханойская башня».
    # Чтобы перенести n дисков со стержня source на target:
    #   1) перенести n-1 дисков на вспомогательный стержень helper;
    #   2) перенести самый большой диск на target;
    #   3) перенести n-1 дисков с helper на target.
    # Всего ходов: 2^n - 1.

    moves = 0


    def hanoi(n, source, target, helper):
        nonlocal moves
        if n == 0:
            return
        hanoi(n - 1, source, helper, target)
        moves += 1
        print(f"Ход {moves}: диск {n} со стержня {source} на стержень {target}")
        hanoi(n - 1, helper, target, source)


    n = int(read_input("Количество дисков: "))
    hanoi(n, "A", "C", "B")
    print(f"Всего ходов: {moves}")


def run_example(solve, example_inputs):
    """Передаёт задаче готовые данные и показывает их в консоли."""
    values = iter(example_inputs)

    def read_example(prompt=""):
        value = next(values)
        print(f"{prompt}{value}")
        return value

    solve(read_example)


def run_selected(solve, example_inputs):
    mode = input("Enter — пример, 1 — ручной ввод: ").strip()
    if not mode:
        run_example(solve, example_inputs)
    elif mode == "1":
        solve(input)
    else:
        print("Для примера нажмите Enter, для ручного ввода введите 1.")


TASKS = {
    '1': ('Факториал', task01_factorial, ('5',)),
    '2': ('Число Фибоначчи', task02_fibonacci, ('8',)),
    '3': ('Целая степень', task03_power, ('2', '-3')),
    '4': ('Палиндром', task04_palindrome, ('А роза упала на лапу Азора',)),
    '5': ('Бинарный поиск', task05_binary_search, ('1 3 5 7 9', '9')),
    '6': ('Слова в обратном порядке', task06_reverse_words, ('я люблю код',)),
    '7': ('Сумма простых чисел', task07_prime_sum, ('27',)),
    '8': ('Количество цифр', task08_count_digits, ('-12304',)),
    '9': ('Ханойская башня', task09_hanoi, ('2',)),
}


def main():
    print('Лабораторная работа № 4 «Рекурсия»')
    for number, (title, _, _) in TASKS.items():
        print(f"{number}. {title}")

    choice = input("Номер задачи или Enter / 0 — все примеры: ").strip()
    if choice in ("", "0"):
        for number, (title, solve, example_inputs) in TASKS.items():
            print(f"\n=== Задача {number}. {title} ===")
            run_example(solve, example_inputs)
        print(f"\nВыполнено примеров: {len(TASKS)}")
        return

    number = choice.lstrip("0")
    task = TASKS.get(number)
    if task is None:
        print("Нет задачи с таким номером.")
        return

    title, solve, example_inputs = task
    print(f"\n=== Задача {number}. {title} ===")
    run_selected(solve, example_inputs)


if __name__ == "__main__":
    main()
