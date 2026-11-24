"""Лабораторная работа № 3 «Циклы». Объединённый запуск."""


def task01_candy_price(read_input):
    # Лабораторная 3, задача 1
    # Дана цена 1 кг конфет. Вывести стоимость 0.1, 0.2, ..., 1 кг конфет.

    price = float(read_input("Цена 1 кг конфет: "))

    for i in range(1, 11):
        weight = i / 10   # 0.1, 0.2, ..., 1.0
        cost = weight * price
        print(f"{weight:.1f} кг — {cost:.2f}")


def task02_product(read_input):
    # Лабораторная 3, задача 2
    # Дано целое N (> 0). Найти произведение 1.1 * 1.2 * 1.3 * ... (N сомножителей).

    N = int(read_input("N = "))

    product = 1.0
    factor = 1.1
    for i in range(N):
        product *= factor
        factor += 0.1

    print(f"Произведение = {round(product, 6)}")


def task03_square_by_odds(read_input):
    # Лабораторная 3, задача 3
    # Дано целое N (> 0). Найти N^2 по формуле N^2 = 1 + 3 + 5 + ... + (2N - 1).
    # После добавления каждого слагаемого выводить текущую сумму.

    N = int(read_input("N = "))

    total = 0
    for i in range(1, N + 1):
        term = 2 * i - 1        # очередное нечётное число
        total += term
        print(f"+ {term} -> сумма = {total}")

    print(f"{N}^2 = {total}")


def task04_power_sum(read_input):
    # Лабораторная 3, задача 4
    # Дано вещественное A и целое N (> 0). Одним циклом найти сумму 1 + A + A^2 + ... + A^N.
    # Идея: не возводим в степень каждый раз, а храним текущую степень и умножаем её на A.

    A = float(read_input("A = "))
    N = int(read_input("N = "))

    total = 1.0     # слагаемое A^0 = 1
    power = 1.0     # текущая степень A
    for i in range(N):
        power *= A
        total += power

    print(f"Сумма = {total}")


def task05_alternating_sum(read_input):
    # Лабораторная 3, задача 5
    # Дано вещественное A и целое N (> 0). Одним циклом найти
    # 1 - A + A^2 - A^3 + ... ± A^N. Условный оператор не использовать.
    # Идея: каждое следующее слагаемое = предыдущее * (-A), тогда знак чередуется сам.

    A = float(read_input("A = "))
    N = int(read_input("N = "))

    total = 1.0
    term = 1.0
    for i in range(N):
        term *= -A
        total += term

    print(f"Сумма = {total}")


def task06_repeat_numbers(read_input):
    # Лабораторная 3, задача 6
    # Даны целые A < B. Вывести все числа от A до B включительно,
    # каждое число столько раз, каково его значение (3 выводится 3 раза).

    A = int(read_input("A = "))
    B = int(read_input("B = "))

    for number in range(A, B + 1):
        for _ in range(number):
            print(number, end=" ")
        print()


def task07_free_length(read_input):
    # Лабораторная 3, задача 7
    # Даны A > B > 0. На отрезке длины A разместили максимум отрезков длины B без наложений.
    # Без умножения и деления найти длину незанятой части отрезка A.
    # Идея: вычитаем B из A, пока остаток не станет меньше B.

    from fractions import Fraction

    A = Fraction(read_input("A = "))
    B = Fraction(read_input("B = "))

    if not A > B > 0:
        print("Длины должны удовлетворять условию A > B > 0")
    else:
        # Десятичный ввод преобразуется в точную дробь.
        rest = A
        while rest >= B:
            rest -= B

        print(f"Незанятая часть = {float(round(rest, 6))}")


def task08_min_k(read_input):
    # Лабораторная 3, задача 8
    # Дано целое N (> 1). Найти наименьшее K, при котором 1 + 2 + ... + K >= N,
    # и вывести K и эту сумму.

    N = int(read_input("N = "))

    K = 0
    total = 0
    while total < N:
        K += 1
        total += K

    print(f"K = {K}, сумма = {total}")


def task09_deposit(read_input):
    # Лабораторная 3, задача 9
    # Начальный вклад 1000 руб. Каждый месяц вклад растёт на P процентов (0 < P < 25).
    # Определить, через сколько месяцев K вклад превысит 1100 руб., и итоговую сумму S.

    from decimal import Decimal, localcontext

    P = Decimal(read_input("Процент P (0 < P < 25): "))

    if not P.is_finite() or not 0 < P < 25:
        print("Процент должен удовлетворять условию 0 < P < 25")
    else:
        with localcontext() as context:
            # Учитываем значащие цифры P, чтобы при малой ставке множитель отличался от 1.
            context.prec = max(28, len(P.as_tuple().digits) - min(P.adjusted(), 0) + 24)
            factor = 1 + P / 100
            initial_balance = Decimal(1000)
            target_balance = Decimal(1100)
            S = initial_balance
            K = 0

            if P < Decimal("0.01"):
                # Ищем первый целый месяц после достижения порога по формуле сложных процентов.
                threshold_month = (target_balance / initial_balance).ln() / factor.ln()
                K = int(threshold_month) + 1
                S = initial_balance * factor ** K
                while S <= target_balance:
                    K += 1
                    S *= factor
                while K > 1 and S / factor > target_balance:
                    K -= 1
                    S /= factor
            else:
                while S <= target_balance:
                    S *= factor
                    K += 1

            print(f"K = {K} мес., S = {S:.2f} руб.")


def task10_gcd(read_input):
    # Лабораторная 3, задача 10
    # Даны целые положительные A и B. Найти НОД по алгоритму Евклида.
    # Алгоритм: пока B != 0, заменяем (A, B) на (B, A % B). Когда B станет 0, ответ — A.

    A = int(read_input("A = "))
    B = int(read_input("B = "))

    a, b = A, B
    while b != 0:
        a, b = b, a % b

    print(f"НОД({A}, {B}) = {a}")


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
    '1': ('Стоимость конфет', task01_candy_price, ('50',)),
    '2': ('Произведение', task02_product, ('3',)),
    '3': ('Квадрат через сумму', task03_square_by_odds, ('4',)),
    '4': ('Сумма степеней', task04_power_sum, ('2', '3')),
    '5': ('Сумма с чередованием знаков', task05_alternating_sum, ('2', '3')),
    '6': ('Повторение чисел', task06_repeat_numbers, ('2', '4')),
    '7': ('Свободная часть отрезка', task07_free_length, ('0.3', '0.1')),
    '8': ('Наименьшее K', task08_min_k, ('10',)),
    '9': ('Банковский вклад', task09_deposit, ('5',)),
    '10': ('НОД', task10_gcd, ('48', '18')),
}


def main():
    print('Лабораторная работа № 3 «Циклы»')
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
