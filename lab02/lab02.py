"""Лабораторная работа № 2 «Ветвления». Объединённый запуск."""


def task01_max_or_zero(read_input):
    # Лабораторная 2, задача 1
    # Даны целые A и B. Если они не равны — присвоить обеим переменным большее значение,
    # если равны — присвоить обеим 0. Вывести новые значения A и B.

    A = int(read_input("A = "))
    B = int(read_input("B = "))

    # В Python вместо фигурных скобок — двоеточие и отступ.
    if A != B:
        biggest = max(A, B)
        A = biggest
        B = biggest
    else:
        A = 0
        B = 0

    print(f"A = {A}, B = {B}")


def task02_two_largest_sum(read_input):
    # Лабораторная 2, задача 2
    # Даны три числа. Найти сумму двух наибольших из них.

    a = float(read_input("Первое число: "))
    b = float(read_input("Второе число: "))
    c = float(read_input("Третье число: "))

    # Находим наименьшее число через условия и не берём его в сумму
    if a <= b and a <= c:
        result = b + c
    elif b <= a and b <= c:
        result = a + c
    else:
        result = a + b

    print(f"Сумма двух наибольших = {result}")


def task03_closest_point(read_input):
    # Лабораторная 2, задача 3
    # На плоскости точки A, B, C. Определить, какая из точек B или C ближе к A,
    # и вывести эту точку и её расстояние от A.

    import math

    xa = float(read_input("xA = "))
    ya = float(read_input("yA = "))
    xb = float(read_input("xB = "))
    yb = float(read_input("yB = "))
    xc = float(read_input("xC = "))
    yc = float(read_input("yC = "))

    dist_ab = math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)
    dist_ac = math.sqrt((xc - xa) ** 2 + (yc - ya) ** 2)

    if dist_ab < dist_ac:
        print(f"Ближе точка B({xb}, {yb}), расстояние = {dist_ab}")
    elif dist_ac < dist_ab:
        print(f"Ближе точка C({xc}, {yc}), расстояние = {dist_ac}")
    else:
        print(f"Точки B и C находятся на одинаковом расстоянии = {dist_ab}")


def task04_quadrant(read_input):
    # Лабораторная 2, задача 4
    # Даны координаты точки, не лежащей на осях. Определить номер координатной четверти.
    #   II  |  I
    #  -----+-----
    #  III  |  IV

    x = float(read_input("x = "))
    y = float(read_input("y = "))

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


def task05_number_description(read_input):
    # Лабораторная 2, задача 5
    # Дано целое число. Вывести описание вида «отрицательное четное число»,
    # «нулевое число», «положительное нечетное число».

    n = int(read_input("Введите целое число: "))

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


def task06_digits_description(read_input):
    # Лабораторная 2, задача 6
    # Дано целое число от 1 до 999. Вывести описание вида
    # «четное двузначное число», «нечетное трехзначное число».

    n = int(read_input("Введите число от 1 до 999: "))

    if n < 1 or n > 999:
        print("Число вне диапазона 1–999")
    else:
        parity = "четное" if n % 2 == 0 else "нечетное"

        if n < 10:
            digits = "однозначное"
        elif n < 100:
            digits = "двузначное"
        else:
            digits = "трехзначное"

        print(f"{parity} {digits} число")


def task07_date_text(read_input):
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

    day = int(read_input("День (1–31): "))
    month = int(read_input("Месяц (1–12): "))

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


def task08_tasks_count(read_input):
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
    tens = {2: "двадцать", 3: "тридцать", 4: "сорок"}

    n = int(read_input("Количество заданий (10–40): "))

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


def task09_number_words(read_input):
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

    n = int(read_input("Введите число от 100 до 999: "))

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

        print(f"{n} — «{' '.join(parts)}»")


def task10_eastern_calendar(read_input):
    # Лабораторная 2, задача 10
    # Восточный календарь: 60-летний цикл из пяти 12-летних подциклов цвета
    # (зеленый, красный, желтый, белый, черный). Годы внутри подцикла — животные.
    # 1984 — начало цикла, «год зеленой крысы». По номеру года определить название.

    colors = ["зеленой", "красной", "желтой", "белой", "черной"]
    animals = ["крысы", "коровы", "тигра", "зайца", "дракона", "змеи",
               "лошади", "овцы", "обезьяны", "курицы", "собаки", "свиньи"]

    year = int(read_input("Введите год: "))

    offset = year - 1984
    # В Python остаток от деления отрицательного числа неотрицательный (-1 % 60 == 59),
    # поэтому формула работает и для годов раньше 1984.
    color_index = (offset % 60) // 12
    animal_index = offset % 12

    print(f"{year} — год {colors[color_index]} {animals[animal_index]}")


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
    '1': ('Максимум или ноль', task01_max_or_zero, ('5', '5')),
    '2': ('Два наибольших числа', task02_two_largest_sum, ('2', '2', '5')),
    '3': ('Ближайшая точка', task03_closest_point, ('0', '0', '3', '4', '-3', '4')),
    '4': ('Координатная четверть', task04_quadrant, ('-3', '4')),
    '5': ('Описание числа', task05_number_description, ('-3',)),
    '6': ('Чётность и число цифр', task06_digits_description, ('100',)),
    '7': ('Дата словами', task07_date_text, ('29', '2')),
    '8': ('Количество заданий', task08_tasks_count, ('21',)),
    '9': ('Трёхзначное число словами', task09_number_words, ('814',)),
    '10': ('Восточный календарь', task10_eastern_calendar, ('1983',)),
}


def main():
    print('Лабораторная работа № 2 «Ветвления»')
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
