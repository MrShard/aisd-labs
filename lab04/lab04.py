"""Лабораторная работа № 4 «Рекурсия». Объединённый запуск."""


# В ручном режиме читаю строку с клавиатуры. В примере беру первую готовую строку.
def read_line(prompt, example_lines):
    if example_lines is None:
        return input(prompt)

    # pop(0) возвращает первую строку и убирает её из списка этого запуска.
    line = example_lines.pop(0)
    print(prompt + line)
    return line


def task01_factorial(example_lines=None):
    # Лабораторная 4, задача 1
    # Рекурсивно вычислить факториал n: n! = n * (n-1)!, 0! = 1.

    def factorial(n):
        if n <= 1:           # базовый случай — здесь рекурсия останавливается
            return 1
        return n * factorial(n - 1)


    n = int(read_line("n = ", example_lines))
    if n < 0:
        print("Факториал отрицательного числа не определён")
    else:
        print(f"{n}! = {factorial(n)}")


def task02_fibonacci(example_lines=None):
    # Лабораторная 4, задача 2
    # Рекурсивно вычислить n-е число Фибоначчи: F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2).
    # Внимание: простая рекурсия работает медленно для n > 35 (много повторных вызовов).

    def fibonacci(n):
        if n < 2:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)


    n = int(read_line("n = ", example_lines))
    if n < 0:
        print("n должно быть неотрицательным")
    else:
        print(f"F({n}) = {fibonacci(n)}")


def task03_power(example_lines=None):
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


    x = float(read_line("x = ", example_lines))
    n = int(read_line("n (целое) = ", example_lines))

    if x == 0 and n < 0:
        print("0 нельзя возводить в отрицательную степень")
    else:
        print(f"{x}^{n} = {power(x, n)}")


def task04_palindrome(example_lines=None):
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


    text = read_line("Введите строку: ", example_lines)
    cleaned = ""
    for character in text:
        if character.isalnum():
            cleaned += character.lower()

    if is_palindrome(cleaned):
        print("Это палиндром")
    else:
        print("Это не палиндром")


def task05_binary_search(example_lines=None):
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


    parts = read_line("Отсортированный массив через пробел: ", example_lines).split()
    arr = []
    for part in parts:
        arr.append(int(part))
    target = int(read_line("Что ищем: ", example_lines))

    index = binary_search(arr, target, 0, len(arr) - 1)
    if index == -1:
        print("Элемент не найден")
    else:
        print(f"Элемент найден, индекс = {index} (номер {index + 1})")


def task06_reverse_words(example_lines=None):
    # Лабораторная 4, задача 6
    # Рекурсивно поменять порядок слов в строке на обратный.
    # Идея: reverse(["a", "b", "c"]) = reverse(["b", "c"]) + ["a"]

    def reverse_words(words):
        if len(words) <= 1:
            return words
        return reverse_words(words[1:]) + [words[0]]


    text = read_line("Введите строку: ", example_lines)
    words = text.split()
    print(" ".join(reverse_words(words)))


def task07_prime_sum(example_lines=None):
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


    n = int(read_line("Введите число (>= 2): ", example_lines))
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


def task08_count_digits(example_lines=None):
    # Лабораторная 4, задача 8
    # Рекурсивно подсчитать количество цифр в числе.
    # Идея: если число < 10, в нём одна цифра; иначе 1 + количество цифр в n // 10.

    def count_digits(n):
        if n < 10:
            return 1
        return 1 + count_digits(n // 10)


    n = int(read_line("Введите целое число: ", example_lines))
    print(f"Количество цифр: {count_digits(abs(n))}")


def task09_hanoi(example_lines=None):
    # Лабораторная 4, задача 9
    # Рекурсивное решение головоломки «Ханойская башня».
    # Чтобы перенести n дисков со стержня source на target:
    #   1) перенести n-1 дисков на вспомогательный стержень helper;
    #   2) перенести самый большой диск на target;
    #   3) перенести n-1 дисков с helper на target.
    # Всего ходов: 2^n - 1.

    def hanoi(n, source, target, helper, moves=0):
        if n == 0:
            return moves

        moves = hanoi(n - 1, source, helper, target, moves)

        moves += 1
        print(f"Ход {moves}: диск {n} со стержня {source} на стержень {target}")

        return hanoi(n - 1, helper, target, source, moves)


    n = int(read_line("Количество дисков: ", example_lines))
    moves = hanoi(n, "A", "C", "B")
    print(f"Всего ходов: {moves}")


TITLES = [
    'Факториал',
    'Число Фибоначчи',
    'Целая степень',
    'Палиндром',
    'Бинарный поиск',
    'Слова в обратном порядке',
    'Сумма простых чисел',
    'Количество цифр',
    'Ханойская башня',
]

EXAMPLES = [
    ['5'],
    ['8'],
    ['2', '-3'],
    ['А роза упала на лапу Азора'],
    ['1 3 5 7 9', '9'],
    ['я люблю код'],
    ['27'],
    ['-12304'],
    ['2'],
]


# Подготавливаю входные данные и обычным if выбираю нужную задачу.
def run_task(number, use_example):
    example_lines = None
    if use_example:
        # Копирую пример, потому что read_line забирает использованные строки.
        example_lines = EXAMPLES[number - 1].copy()
    if number == 1:
        task01_factorial(example_lines)
    elif number == 2:
        task02_fibonacci(example_lines)
    elif number == 3:
        task03_power(example_lines)
    elif number == 4:
        task04_palindrome(example_lines)
    elif number == 5:
        task05_binary_search(example_lines)
    elif number == 6:
        task06_reverse_words(example_lines)
    elif number == 7:
        task07_prime_sum(example_lines)
    elif number == 8:
        task08_count_digits(example_lines)
    elif number == 9:
        task09_hanoi(example_lines)


def main():
    print('Лабораторная работа № 4 «Рекурсия»')
    for index in range(len(TITLES)):
        print(f"{index + 1}. {TITLES[index]}")

    choice = input("Номер задачи или Enter / 0 — все примеры: ").strip()
    if choice == "" or choice == "0":
        # Общий прогон подставляет пример для каждой задачи по очереди.
        for number in range(1, len(TITLES) + 1):
            print(f"\n=== Задача {number}. {TITLES[number - 1]} ===")
            run_task(number, True)
        print(f"\nВыполнено примеров: {len(TITLES)}")
        return

    choice = choice.lstrip("0")
    if not choice.isdecimal() or len(choice) > 2:
        print("Нет задачи с таким номером.")
        return
    number = int(choice)
    if number < 1 or number > len(TITLES):
        print("Нет задачи с таким номером.")
        return

    print(f"\n=== Задача {number}. {TITLES[number - 1]} ===")
    mode = input("Enter — пример, 1 — ручной ввод: ").strip()
    if mode == "":
        run_task(number, True)
    elif mode == "1":
        run_task(number, False)
    else:
        print("Для примера нажмите Enter, для ручного ввода введите 1.")


if __name__ == "__main__":
    main()
