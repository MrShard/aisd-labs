"""Лабораторная работа № 3 «Циклы». Объединённый запуск."""


# В ручном режиме читаю строку с клавиатуры. В примере беру первую готовую строку.
def read_line(prompt, example_lines):
    if example_lines is None:
        return input(prompt)

    # pop(0) возвращает первую строку и убирает её из списка этого запуска.
    line = example_lines.pop(0)
    print(prompt + line)
    return line


def task01_candy_price(example_lines=None):
    # Лабораторная 3, задача 1
    # Дана цена 1 кг конфет. Вывести стоимость 0.1, 0.2, ..., 1 кг конфет.

    price = float(read_line("Цена 1 кг конфет: ", example_lines))

    for i in range(1, 11):
        weight = i / 10   # 0.1, 0.2, ..., 1.0
        cost = weight * price
        print(f"{weight:.1f} кг — {cost:.2f}")


def task02_product(example_lines=None):
    # Лабораторная 3, задача 2
    # Дано целое N (> 0). Найти произведение 1.1 * 1.2 * 1.3 * ... (N сомножителей).

    N = int(read_line("N = ", example_lines))

    product = 1.0
    factor = 1.1
    for i in range(N):
        product *= factor
        factor += 0.1

    print(f"Произведение = {round(product, 6)}")


def task03_square_by_odds(example_lines=None):
    # Лабораторная 3, задача 3
    # Дано целое N (> 0). Найти N^2 по формуле N^2 = 1 + 3 + 5 + ... + (2N - 1).
    # После добавления каждого слагаемого выводить текущую сумму.

    N = int(read_line("N = ", example_lines))

    total = 0
    for i in range(1, N + 1):
        term = 2 * i - 1        # очередное нечётное число
        total += term
        print(f"+ {term} -> сумма = {total}")

    print(f"{N}^2 = {total}")


def task04_power_sum(example_lines=None):
    # Лабораторная 3, задача 4
    # Дано вещественное A и целое N (> 0). Одним циклом найти сумму 1 + A + A^2 + ... + A^N.
    # Идея: не возводим в степень каждый раз, а храним текущую степень и умножаем её на A.

    A = float(read_line("A = ", example_lines))
    N = int(read_line("N = ", example_lines))

    total = 1.0     # слагаемое A^0 = 1
    power = 1.0     # текущая степень A
    for i in range(N):
        power *= A
        total += power

    print(f"Сумма = {total}")


def task05_alternating_sum(example_lines=None):
    # Лабораторная 3, задача 5
    # Дано вещественное A и целое N (> 0). Одним циклом найти
    # 1 - A + A^2 - A^3 + ... ± A^N. Условный оператор не использовать.
    # Идея: каждое следующее слагаемое = предыдущее * (-A), тогда знак чередуется сам.

    A = float(read_line("A = ", example_lines))
    N = int(read_line("N = ", example_lines))

    total = 1.0
    term = 1.0
    for i in range(N):
        term *= -A
        total += term

    print(f"Сумма = {total}")


def task06_repeat_numbers(example_lines=None):
    # Лабораторная 3, задача 6
    # Даны целые A < B. Вывести все числа от A до B включительно,
    # каждое число столько раз, каково его значение (3 выводится 3 раза).

    A = int(read_line("A = ", example_lines))
    B = int(read_line("B = ", example_lines))

    for number in range(A, B + 1):
        for _ in range(number):
            print(number, end=" ")
        print()


def task07_free_length(example_lines=None):
    # Лабораторная 3, задача 7
    # Даны A > B > 0. На отрезке длины A разместили максимум отрезков длины B без наложений.
    # Без умножения и деления найти длину незанятой части отрезка A.
    # Идея: вычитаем B из A, пока остаток не станет меньше B.

    from fractions import Fraction

    A = Fraction(read_line("A = ", example_lines))
    B = Fraction(read_line("B = ", example_lines))

    if not A > B > 0:
        print("Длины должны удовлетворять условию A > B > 0")
    else:
        # Десятичный ввод преобразуется в точную дробь.
        rest = A
        while rest >= B:
            rest -= B

        print(f"Незанятая часть = {float(round(rest, 6))}")


def task08_min_k(example_lines=None):
    # Лабораторная 3, задача 8
    # Дано целое N (> 1). Найти наименьшее K, при котором 1 + 2 + ... + K >= N,
    # и вывести K и эту сумму.

    N = int(read_line("N = ", example_lines))

    K = 0
    total = 0
    while total < N:
        K += 1
        total += K

    print(f"K = {K}, сумма = {total}")


def task09_deposit(example_lines=None):
    # Лабораторная 3, задача 9
    # Начальный вклад 1000 руб. Каждый месяц вклад растёт на P процентов (0 < P < 25).
    # Определить, через сколько месяцев K вклад превысит 1100 руб., и итоговую сумму S.

    from decimal import Decimal, localcontext

    P = Decimal(read_line("Процент P (0 < P < 25): ", example_lines))

    if not P.is_finite() or P <= 0 or P >= 25:
        print("Процент должен удовлетворять условию 0 < P < 25")
    else:
        with localcontext() as context:
            digits = len(P.as_tuple().digits)
            places = -P.adjusted()
            if places < 0:
                places = 0
            context.prec = digits + places + 28

            factor = 1 + P / 100
            initial_balance = Decimal(1000)
            target = Decimal(1100)

            if P >= Decimal("0.01"):
                K = 0
                S = initial_balance
                while S <= target:
                    S *= factor
                    K += 1
            else:
                low = 0
                high = 1
                while initial_balance * factor ** high <= target:
                    low = high
                    high *= 2

                while high - low > 1:
                    month = (low + high) // 2
                    balance = initial_balance * factor ** month
                    if balance > target:
                        high = month
                    else:
                        low = month

                K = high
                S = initial_balance * factor ** K

            print(f"K = {K} мес., S = {S:.2f} руб.")


def task10_gcd(example_lines=None):
    # Лабораторная 3, задача 10
    # Даны целые положительные A и B. Найти НОД по алгоритму Евклида.
    # Алгоритм: пока B != 0, заменяем (A, B) на (B, A % B). Когда B станет 0, ответ — A.

    A = int(read_line("A = ", example_lines))
    B = int(read_line("B = ", example_lines))

    a = A
    b = B
    while b != 0:
        remainder = a % b
        a = b
        b = remainder

    print(f"НОД({A}, {B}) = {a}")


TITLES = [
    'Стоимость конфет',
    'Произведение',
    'Квадрат через сумму',
    'Сумма степеней',
    'Сумма с чередованием знаков',
    'Повторение чисел',
    'Свободная часть отрезка',
    'Наименьшее K',
    'Банковский вклад',
    'НОД',
]

EXAMPLES = [
    ['50'],
    ['3'],
    ['4'],
    ['2', '3'],
    ['2', '3'],
    ['2', '4'],
    ['0.3', '0.1'],
    ['10'],
    ['5'],
    ['48', '18'],
]


# Подготавливаю входные данные и обычным if выбираю нужную задачу.
def run_task(number, use_example):
    example_lines = None
    if use_example:
        # Копирую пример, потому что read_line забирает использованные строки.
        example_lines = EXAMPLES[number - 1].copy()
    if number == 1:
        task01_candy_price(example_lines)
    elif number == 2:
        task02_product(example_lines)
    elif number == 3:
        task03_square_by_odds(example_lines)
    elif number == 4:
        task04_power_sum(example_lines)
    elif number == 5:
        task05_alternating_sum(example_lines)
    elif number == 6:
        task06_repeat_numbers(example_lines)
    elif number == 7:
        task07_free_length(example_lines)
    elif number == 8:
        task08_min_k(example_lines)
    elif number == 9:
        task09_deposit(example_lines)
    elif number == 10:
        task10_gcd(example_lines)


def main():
    print('Лабораторная работа № 3 «Циклы»')
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
