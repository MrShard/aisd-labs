"""Лабораторная работа № 2 «Ветвления». Объединённый запуск."""


# В ручном режиме читаю строку с клавиатуры. В примере беру первую готовую строку.
def read_line(prompt, example_lines):
    if example_lines is None:
        return input(prompt)

    # pop(0) возвращает первую строку и убирает её из списка этого запуска.
    line = example_lines.pop(0)
    print(prompt + line)
    return line


def task01_max_or_zero(example_lines=None):
    # Лабораторная 2, задача 1
    # Даны целые A и B. Если они не равны — присвоить обеим переменным большее значение,
    # если равны — присвоить обеим 0. Вывести новые значения A и B.

    A = int(read_line("A = ", example_lines))
    B = int(read_line("B = ", example_lines))

    # В Python вместо фигурных скобок — двоеточие и отступ.
    if A != B:
        if A > B:
            biggest = A
        else:
            biggest = B
        A = biggest
        B = biggest
    else:
        A = 0
        B = 0

    print(f"A = {A}, B = {B}")


def task02_two_largest_sum(example_lines=None):
    # Лабораторная 2, задача 2
    # Даны три числа. Найти сумму двух наибольших из них.

    a = float(read_line("Первое число: ", example_lines))
    b = float(read_line("Второе число: ", example_lines))
    c = float(read_line("Третье число: ", example_lines))

    # Находим наименьшее число через условия и не берём его в сумму
    if a <= b and a <= c:
        result = b + c
    elif b <= a and b <= c:
        result = a + c
    else:
        result = a + b

    print(f"Сумма двух наибольших = {result}")


def task03_closest_point(example_lines=None):
    # Лабораторная 2, задача 3
    # На плоскости точки A, B, C. Определить, какая из точек B или C ближе к A,
    # и вывести эту точку и её расстояние от A.

    import math

    xa = float(read_line("xA = ", example_lines))
    ya = float(read_line("yA = ", example_lines))
    xb = float(read_line("xB = ", example_lines))
    yb = float(read_line("yB = ", example_lines))
    xc = float(read_line("xC = ", example_lines))
    yc = float(read_line("yC = ", example_lines))

    square_ab = (xb - xa) ** 2 + (yb - ya) ** 2
    square_ac = (xc - xa) ** 2 + (yc - ya) ** 2
    dist_ab = math.sqrt(square_ab)
    dist_ac = math.sqrt(square_ac)

    if square_ab < square_ac:
        print(f"Ближе точка B({xb}, {yb}), расстояние = {dist_ab}")
    elif square_ac < square_ab:
        print(f"Ближе точка C({xc}, {yc}), расстояние = {dist_ac}")
    else:
        print(f"Точки B и C находятся на одинаковом расстоянии = {dist_ab}")


def task04_quadrant(example_lines=None):
    # Лабораторная 2, задача 4
    # Даны координаты точки, не лежащей на осях. Определить номер координатной четверти.
    #   II  |  I
    #  -----+-----
    #  III  |  IV

    x = float(read_line("x = ", example_lines))
    y = float(read_line("y = ", example_lines))

    if x == 0 or y == 0:
        print("Точка лежит на оси, четверть не определена")
    elif x > 0 and y > 0:
        print("Четверть 1")
    elif x < 0 and y > 0:
        print("Четверть 2")
    elif x < 0 and y < 0:
        print("Четверть 3")
    else:
        print("Четверть 4")


def task05_number_description(example_lines=None):
    # Лабораторная 2, задача 5
    # Дано целое число. Вывести описание вида «отрицательное четное число»,
    # «нулевое число», «положительное нечетное число».

    n = int(read_line("Введите целое число: ", example_lines))

    if n == 0:
        print("нулевое число")
    else:
        if n > 0:
            sign = "положительное"
        else:
            sign = "отрицательное"

        if n % 2 == 0:
            parity = "четное"
        else:
            parity = "нечетное"

        print(f"{sign} {parity} число")


def task06_digits_description(example_lines=None):
    # Лабораторная 2, задача 6
    # Дано целое число от 1 до 999. Вывести описание вида
    # «четное двузначное число», «нечетное трехзначное число».

    n = int(read_line("Введите число от 1 до 999: ", example_lines))

    if n < 1 or n > 999:
        print("Число вне диапазона 1–999")
    else:
        if n % 2 == 0:
            parity = "четное"
        else:
            parity = "нечетное"

        if n < 10:
            digits = "однозначное"
        elif n < 100:
            digits = "двузначное"
        else:
            digits = "трехзначное"

        print(f"{parity} {digits} число")


def task07_date_text(example_lines=None):
    # Лабораторная 2, задача 7
    # Дан день (1–31) и месяц (1–12). Вывести дату текстом, например «пятое января».

    # Нулевой элемент пустой, чтобы индекс совпадал с номером дня/месяца
    day_words = [
        "", "первое", "второе", "третье", "четвертое", "пятое", "шестое", "седьмое",
        "восьмое", "девятое", "десятое", "одиннадцатое", "двенадцатое", "тринадцатое",
        "четырнадцатое", "пятнадцатое", "шестнадцатое", "семнадцатое", "восемнадцатое",
        "девятнадцатое", "двадцатое",
    ]
    months = [
        "", "января", "февраля", "марта", "апреля", "мая", "июня",
        "июля", "августа", "сентября", "октября", "ноября", "декабря",
    ]
    # Максимальное число дней в каждом месяце (февраль — 29, с учётом високосного года)
    days_in_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    day = int(read_line("День (1–31): ", example_lines))
    month = int(read_line("Месяц (1–12): ", example_lines))

    if month < 1 or month > 12:
        print("Неверный номер месяца")
    elif day < 1 or day > days_in_month[month]:
        print("В этом месяце нет такого дня")
    else:
        if day <= 20:
            day_text = day_words[day]
        elif day < 30:
            day_text = "двадцать " + day_words[day - 20]   # 21 -> "двадцать первое"
        elif day == 30:
            day_text = "тридцатое"
        else:
            day_text = "тридцать первое"

        print(f"{day_text} {months[month]}")


def task08_tasks_count(example_lines=None):
    # Лабораторная 2, задача 8
    # Дано число от 10 до 40 — количество учебных заданий.
    # Вывести строку с правильным согласованием: 18 — «восемнадцать учебных заданий».
    #
    # Правило согласования:
    #   оканчивается на 1 (кроме 11)        -> «учебное задание»   (21 — двадцать одно учебное задание)
    #   оканчивается на 2, 3, 4 (кроме 12–14) -> «учебных задания»   (22 — двадцать два учебных задания)
    #   все остальные                        -> «учебных заданий»

    # Слово "задание" среднего рода, поэтому "одно", а не "один"
    units = ["", "одно", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    teens = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать",
             "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    tens = ["", "", "двадцать", "тридцать", "сорок"]

    n = int(read_line("Количество заданий (10–40): ", example_lines))

    if n < 10 or n > 40:
        print("Число вне диапазона 10–40")
    else:
        if n < 20:
            number_text = teens[n - 10]
        else:
            number_text = tens[n // 10]
            if n % 10 != 0:
                number_text += " " + units[n % 10]

        last_digit = n % 10
        if 11 <= n <= 14:
            words = "учебных заданий"
        elif last_digit == 1:
            words = "учебное задание"
        elif 2 <= last_digit <= 4:
            words = "учебных задания"
        else:
            words = "учебных заданий"

        print(f"{n} — «{number_text} {words}»")


def task09_number_words(example_lines=None):
    # Лабораторная 2, задача 9
    # Дано целое число 100–999. Вывести его словами:
    # 256 — «двести пятьдесят шесть», 814 — «восемьсот четырнадцать».

    hundreds = ["", "сто", "двести", "триста", "четыреста", "пятьсот",
                "шестьсот", "семьсот", "восемьсот", "девятьсот"]
    tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят",
            "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    teens = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать",
             "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    units = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]

    n = int(read_line("Введите число от 100 до 999: ", example_lines))

    if n < 100 or n > 999:
        print("Число вне диапазона 100–999")
    else:
        h = n // 100        # сотни
        rest = n % 100      # последние две цифры

        parts = [hundreds[h]]
        if 10 <= rest <= 19:
            parts.append(teens[rest - 10])
        else:
            if rest // 10 > 0:
                parts.append(tens[rest // 10])
            if rest % 10 > 0:
                parts.append(units[rest % 10])

        number_text = parts[0]
        for i in range(1, len(parts)):
            number_text += " " + parts[i]
        print(f"{n} — «{number_text}»")


def task10_eastern_calendar(example_lines=None):
    # Лабораторная 2, задача 10
    # Восточный календарь: 60-летний цикл из пяти 12-летних подциклов цвета
    # (зеленый, красный, желтый, белый, черный). Годы внутри подцикла — животные.
    # 1984 — начало цикла, «год зеленой крысы». По номеру года определить название.

    colors = ["зеленой", "красной", "желтой", "белой", "черной"]
    animals = ["крысы", "коровы", "тигра", "зайца", "дракона", "змеи",
               "лошади", "овцы", "обезьяны", "курицы", "собаки", "свиньи"]

    year = int(read_line("Введите год: ", example_lines))

    offset = year - 1984
    # В Python остаток от деления отрицательного числа неотрицательный (-1 % 60 == 59),
    # поэтому формула работает и для годов раньше 1984.
    color_index = (offset % 60) // 12
    animal_index = offset % 12

    print(f"{year} — год {colors[color_index]} {animals[animal_index]}")


TITLES = [
    'Максимум или ноль',
    'Два наибольших числа',
    'Ближайшая точка',
    'Координатная четверть',
    'Описание числа',
    'Чётность и число цифр',
    'Дата словами',
    'Количество заданий',
    'Трёхзначное число словами',
    'Восточный календарь',
]

EXAMPLES = [
    ['5', '5'],
    ['2', '2', '5'],
    ['0', '0', '3', '4', '-3', '4'],
    ['-3', '4'],
    ['-3'],
    ['100'],
    ['29', '2'],
    ['21'],
    ['814'],
    ['1983'],
]


# Подготавливаю входные данные и обычным if выбираю нужную задачу.
def run_task(number, use_example):
    example_lines = None
    if use_example:
        # Копирую пример, потому что read_line забирает использованные строки.
        example_lines = EXAMPLES[number - 1].copy()
    if number == 1:
        task01_max_or_zero(example_lines)
    elif number == 2:
        task02_two_largest_sum(example_lines)
    elif number == 3:
        task03_closest_point(example_lines)
    elif number == 4:
        task04_quadrant(example_lines)
    elif number == 5:
        task05_number_description(example_lines)
    elif number == 6:
        task06_digits_description(example_lines)
    elif number == 7:
        task07_date_text(example_lines)
    elif number == 8:
        task08_tasks_count(example_lines)
    elif number == 9:
        task09_number_words(example_lines)
    elif number == 10:
        task10_eastern_calendar(example_lines)


def main():
    print('Лабораторная работа № 2 «Ветвления»')
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
