"""Лабораторная работа № 1 «Линейные алгоритмы». Объединённый запуск."""


# В ручном режиме читаю строку с клавиатуры. В примере беру первую готовую строку.
def read_line(prompt, example_lines):
    if example_lines is None:
        return input(prompt)

    # pop(0) возвращает первую строку и убирает её из списка этого запуска.
    line = example_lines.pop(0)
    print(prompt + line)
    return line


def task01_rectangle(example_lines=None):
    # Лабораторная 1, задача 1
    # Даны стороны прямоугольника a и b. Найти площадь S = a*b и периметр P = 2*(a + b).

    a = float(read_line("Введите сторону a: ", example_lines))
    b = float(read_line("Введите сторону b: ", example_lines))

    S = a * b
    P = 2 * (a + b)

    print(f"Площадь S = {S}")
    print(f"Периметр P = {P}")


def task02_circle_length(example_lines=None):
    # Лабораторная 1, задача 2
    # Дан диаметр окружности d. Найти её длину L = π*d (π = 3.14).

    PI = 3.14

    d = float(read_line("Введите диаметр d: ", example_lines))
    L = PI * d

    print(f"Длина окружности L = {round(L, 4)}")


def task03_average(example_lines=None):
    # Лабораторная 1, задача 3
    # Даны два числа a и b. Найти их среднее арифметическое (a + b) / 2.

    a = float(read_line("Введите a: ", example_lines))
    b = float(read_line("Введите b: ", example_lines))

    average = (a + b) / 2

    print(f"Среднее арифметическое = {average}")


def task04_squares(example_lines=None):
    # Лабораторная 1, задача 4
    # Даны два ненулевых числа. Найти сумму, разность, произведение и частное их квадратов.

    a = float(read_line("Введите первое ненулевое число: ", example_lines))
    b = float(read_line("Введите второе ненулевое число: ", example_lines))

    a2 = a ** 2
    b2 = b ** 2

    print(f"Квадраты: {a2} и {b2}")
    print(f"Сумма = {a2 + b2}")
    print(f"Разность = {a2 - b2}")
    print(f"Произведение = {a2 * b2}")
    print(f"Частное = {a2 / b2}")


def task05_abs(example_lines=None):
    # Лабораторная 1, задача 5
    # Даны два ненулевых числа. Найти сумму, разность, произведение и частное их модулей.

    a = float(read_line("Введите первое ненулевое число: ", example_lines))
    b = float(read_line("Введите второе ненулевое число: ", example_lines))

    abs_a = abs(a)
    abs_b = abs(b)

    print(f"Модули: {abs_a} и {abs_b}")
    print(f"Сумма = {abs_a + abs_b}")
    print(f"Разность = {abs_a - abs_b}")
    print(f"Произведение = {abs_a * abs_b}")
    print(f"Частное = {abs_a / abs_b}")


def task06_distance(example_lines=None):
    # Лабораторная 1, задача 6
    # Найти расстояние между двумя точками (x1, y1) и (x2, y2).
    # Формула: d = sqrt((x2 - x1)^2 + (y2 - y1)^2)

    import math

    x1 = float(read_line("x1 = ", example_lines))
    y1 = float(read_line("y1 = ", example_lines))
    x2 = float(read_line("x2 = ", example_lines))
    y2 = float(read_line("y2 = ", example_lines))

    dx = x2 - x1
    dy = y2 - y1
    distance = math.sqrt(dx ** 2 + dy ** 2)

    print(f"Расстояние между точками = {distance}")


def task07_segments_sum(example_lines=None):
    # Лабораторная 1, задача 7
    # Даны три точки A, B, C на числовой оси. Найти длины отрезков AC и BC и их сумму.
    # Длина отрезка на оси = модуль разности координат.

    A = float(read_line("Координата точки A: ", example_lines))
    B = float(read_line("Координата точки B: ", example_lines))
    C = float(read_line("Координата точки C: ", example_lines))

    AC = abs(A - C)
    BC = abs(B - C)

    print(f"AC = {AC}")
    print(f"BC = {BC}")
    print(f"AC + BC = {AC + BC}")


def task08_segments_product(example_lines=None):
    # Лабораторная 1, задача 8
    # Даны три точки A, B, C на числовой оси, C лежит между A и B.
    # Найти произведение длин отрезков AC и BC.

    A = float(read_line("Координата точки A: ", example_lines))
    B = float(read_line("Координата точки B: ", example_lines))
    C = float(read_line("Координата точки C (между A и B): ", example_lines))

    AC = abs(A - C)
    BC = abs(B - C)

    print(f"AC = {AC}, BC = {BC}")
    print(f"AC * BC = {AC * BC}")


def task09_rectangle_by_vertices(example_lines=None):
    # Лабораторная 1, задача 9
    # Даны координаты двух противоположных вершин прямоугольника (x1, y1), (x2, y2).
    # Стороны параллельны осям. Найти периметр и площадь.

    x1 = float(read_line("x1 = ", example_lines))
    y1 = float(read_line("y1 = ", example_lines))
    x2 = float(read_line("x2 = ", example_lines))
    y2 = float(read_line("y2 = ", example_lines))

    width = abs(x2 - x1)   # длина горизонтальной стороны
    height = abs(y2 - y1)  # длина вертикальной стороны

    P = 2 * (width + height)
    S = width * height

    print(f"Периметр P = {P}")
    print(f"Площадь S = {S}")


def task10_triangle(example_lines=None):
    # Лабораторная 1, задача 10
    # Даны координаты трёх вершин треугольника. Найти его периметр и площадь.
    # Стороны считаем как расстояния между вершинами,
    # площадь — по формуле Герона: S = sqrt(p(p-a)(p-b)(p-c)), где p — полупериметр.

    import math

    x1 = float(read_line("x1 = ", example_lines))
    y1 = float(read_line("y1 = ", example_lines))
    x2 = float(read_line("x2 = ", example_lines))
    y2 = float(read_line("y2 = ", example_lines))
    x3 = float(read_line("x3 = ", example_lines))
    y3 = float(read_line("y3 = ", example_lines))

    a = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    b = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    c = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)

    P = a + b + c
    p = P / 2
    under_root = p * (p - a) * (p - b) * (p - c)
    if under_root < 0:
        under_root = 0
    S = math.sqrt(under_root)

    print(f"Периметр P = {P}")
    print(f"Площадь S = {S}")


def task11_function1(example_lines=None):
    # Лабораторная 1, задача 11
    # Найти значение функции y = 3x^6 - 6x^2 - 7 при данном x.

    x = float(read_line("Введите x: ", example_lines))

    y = 3 * x ** 6 - 6 * x ** 2 - 7

    print(f"y = {y}")


def task12_function2(example_lines=None):
    # Лабораторная 1, задача 12
    # Найти значение функции y = 4(x-3)^6 - 7(x-3)^3 + 2 при данном x.

    x = float(read_line("Введите x: ", example_lines))

    t = x - 3  # выносим повторяющееся выражение в переменную
    y = 4 * t ** 6 - 7 * t ** 3 + 2

    print(f"y = {y}")


TITLES = [
    'Прямоугольник по сторонам',
    'Длина окружности',
    'Среднее двух чисел',
    'Действия с квадратами',
    'Действия с модулями',
    'Расстояние между точками',
    'Сумма длин отрезков',
    'Произведение длин отрезков',
    'Прямоугольник по вершинам',
    'Треугольник по вершинам',
    'Значение функции',
    'Значение функции',
]

EXAMPLES = [
    ['3', '4'],
    ['10'],
    ['2', '8'],
    ['-2', '1'],
    ['-9', '3'],
    ['0', '0', '3', '4'],
    ['-1', '4', '1'],
    ['0', '10', '3'],
    ['3', '0', '0', '4'],
    ['0', '0', '3', '0', '0', '4'],
    ['1'],
    ['4'],
]


# Подготавливаю входные данные и обычным if выбираю нужную задачу.
def run_task(number, use_example):
    example_lines = None
    if use_example:
        # Копирую пример, потому что read_line забирает использованные строки.
        example_lines = EXAMPLES[number - 1].copy()
    if number == 1:
        task01_rectangle(example_lines)
    elif number == 2:
        task02_circle_length(example_lines)
    elif number == 3:
        task03_average(example_lines)
    elif number == 4:
        task04_squares(example_lines)
    elif number == 5:
        task05_abs(example_lines)
    elif number == 6:
        task06_distance(example_lines)
    elif number == 7:
        task07_segments_sum(example_lines)
    elif number == 8:
        task08_segments_product(example_lines)
    elif number == 9:
        task09_rectangle_by_vertices(example_lines)
    elif number == 10:
        task10_triangle(example_lines)
    elif number == 11:
        task11_function1(example_lines)
    elif number == 12:
        task12_function2(example_lines)


def main():
    print('Лабораторная работа № 1 «Линейные алгоритмы»')
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
