"""Лабораторная работа № 1 «Линейные алгоритмы». Объединённый запуск."""


def task01_rectangle(read_input):
    # Лабораторная 1, задача 1
    # Даны стороны прямоугольника a и b. Найти площадь S = a*b и периметр P = 2*(a + b).

    a = float(read_input("Введите сторону a: "))
    b = float(read_input("Введите сторону b: "))

    S = a * b
    P = 2 * (a + b)

    print(f"Площадь S = {S}")
    print(f"Периметр P = {P}")


def task02_circle_length(read_input):
    # Лабораторная 1, задача 2
    # Дан диаметр окружности d. Найти её длину L = π*d (π = 3.14).

    PI = 3.14

    d = float(read_input("Введите диаметр d: "))
    L = PI * d

    print(f"Длина окружности L = {round(L, 4)}")


def task03_average(read_input):
    # Лабораторная 1, задача 3
    # Даны два числа a и b. Найти их среднее арифметическое (a + b) / 2.

    a = float(read_input("Введите a: "))
    b = float(read_input("Введите b: "))

    average = (a + b) / 2

    print(f"Среднее арифметическое = {average}")


def task04_squares(read_input):
    # Лабораторная 1, задача 4
    # Даны два ненулевых числа. Найти сумму, разность, произведение и частное их квадратов.

    a = float(read_input("Введите первое ненулевое число: "))
    b = float(read_input("Введите второе ненулевое число: "))

    a2 = a ** 2
    b2 = b ** 2

    print(f"Квадраты: {a2} и {b2}")
    print(f"Сумма = {a2 + b2}")
    print(f"Разность = {a2 - b2}")
    print(f"Произведение = {a2 * b2}")
    print(f"Частное = {a2 / b2}")


def task05_abs(read_input):
    # Лабораторная 1, задача 5
    # Даны два ненулевых числа. Найти сумму, разность, произведение и частное их модулей.

    a = float(read_input("Введите первое ненулевое число: "))
    b = float(read_input("Введите второе ненулевое число: "))

    abs_a = abs(a)
    abs_b = abs(b)

    print(f"Модули: {abs_a} и {abs_b}")
    print(f"Сумма = {abs_a + abs_b}")
    print(f"Разность = {abs_a - abs_b}")
    print(f"Произведение = {abs_a * abs_b}")
    print(f"Частное = {abs_a / abs_b}")


def task06_distance(read_input):
    # Лабораторная 1, задача 6
    # Найти расстояние между двумя точками (x1, y1) и (x2, y2).
    # Формула: d = sqrt((x2 - x1)^2 + (y2 - y1)^2)

    import math

    x1 = float(read_input("x1 = "))
    y1 = float(read_input("y1 = "))
    x2 = float(read_input("x2 = "))
    y2 = float(read_input("y2 = "))

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    print(f"Расстояние между точками = {distance}")


def task07_segments_sum(read_input):
    # Лабораторная 1, задача 7
    # Даны три точки A, B, C на числовой оси. Найти длины отрезков AC и BC и их сумму.
    # Длина отрезка на оси = модуль разности координат.

    A = float(read_input("Координата точки A: "))
    B = float(read_input("Координата точки B: "))
    C = float(read_input("Координата точки C: "))

    AC = abs(A - C)
    BC = abs(B - C)

    print(f"AC = {AC}")
    print(f"BC = {BC}")
    print(f"AC + BC = {AC + BC}")


def task08_segments_product(read_input):
    # Лабораторная 1, задача 8
    # Даны три точки A, B, C на числовой оси, C лежит между A и B.
    # Найти произведение длин отрезков AC и BC.

    A = float(read_input("Координата точки A: "))
    B = float(read_input("Координата точки B: "))
    C = float(read_input("Координата точки C (между A и B): "))

    AC = abs(A - C)
    BC = abs(B - C)

    print(f"AC = {AC}, BC = {BC}")
    print(f"AC * BC = {AC * BC}")


def task09_rectangle_by_vertices(read_input):
    # Лабораторная 1, задача 9
    # Даны координаты двух противоположных вершин прямоугольника (x1, y1), (x2, y2).
    # Стороны параллельны осям. Найти периметр и площадь.

    x1 = float(read_input("x1 = "))
    y1 = float(read_input("y1 = "))
    x2 = float(read_input("x2 = "))
    y2 = float(read_input("y2 = "))

    width = abs(x2 - x1)   # длина горизонтальной стороны
    height = abs(y2 - y1)  # длина вертикальной стороны

    P = 2 * (width + height)
    S = width * height

    print(f"Периметр P = {P}")
    print(f"Площадь S = {S}")


def task10_triangle(read_input):
    # Лабораторная 1, задача 10
    # Даны координаты трёх вершин треугольника. Найти его периметр и площадь.
    # Стороны считаем как расстояния между вершинами,
    # площадь — по формуле Герона: S = sqrt(p(p-a)(p-b)(p-c)), где p — полупериметр.

    import math

    x1 = float(read_input("x1 = "))
    y1 = float(read_input("y1 = "))
    x2 = float(read_input("x2 = "))
    y2 = float(read_input("y2 = "))
    x3 = float(read_input("x3 = "))
    y3 = float(read_input("y3 = "))

    a = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    b = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    c = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)

    P = a + b + c
    p = P / 2
    # max(..., 0) защищает от крошечных отрицательных значений из-за погрешности вычислений
    S = math.sqrt(max(p * (p - a) * (p - b) * (p - c), 0))

    print(f"Периметр P = {P}")
    print(f"Площадь S = {S}")


def task11_function1(read_input):
    # Лабораторная 1, задача 11
    # Найти значение функции y = 3x^6 - 6x^2 - 7 при данном x.

    x = float(read_input("Введите x: "))

    y = 3 * x ** 6 - 6 * x ** 2 - 7

    print(f"y = {y}")


def task12_function2(read_input):
    # Лабораторная 1, задача 12
    # Найти значение функции y = 4(x-3)^6 - 7(x-3)^3 + 2 при данном x.

    x = float(read_input("Введите x: "))

    t = x - 3  # выносим повторяющееся выражение в переменную
    y = 4 * t ** 6 - 7 * t ** 3 + 2

    print(f"y = {y}")


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
    '1': ('Прямоугольник по сторонам', task01_rectangle, ('3', '4')),
    '2': ('Длина окружности', task02_circle_length, ('10',)),
    '3': ('Среднее двух чисел', task03_average, ('2', '8')),
    '4': ('Действия с квадратами', task04_squares, ('-2', '1')),
    '5': ('Действия с модулями', task05_abs, ('-9', '3')),
    '6': ('Расстояние между точками', task06_distance, ('0', '0', '3', '4')),
    '7': ('Сумма длин отрезков', task07_segments_sum, ('-1', '4', '1')),
    '8': ('Произведение длин отрезков', task08_segments_product, ('0', '10', '3')),
    '9': ('Прямоугольник по вершинам', task09_rectangle_by_vertices, ('3', '0', '0', '4')),
    '10': ('Треугольник по вершинам', task10_triangle, ('0', '0', '3', '0', '0', '4')),
    '11': ('Значение функции', task11_function1, ('1',)),
    '12': ('Значение функции', task12_function2, ('4',)),
}


def main():
    print('Лабораторная работа № 1 «Линейные алгоритмы»')
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
