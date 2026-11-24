"""Лабораторная работа № 6 «Двумерные массивы». Объединённый запуск."""


# В ручном режиме читаю строку с клавиатуры. В примере беру первую готовую строку.
def read_line(prompt, example_lines):
    if example_lines is None:
        return input(prompt)

    # pop(0) возвращает первую строку и убирает её из списка этого запуска.
    line = example_lines.pop(0)
    print(prompt + line)
    return line


def task01_spiral(example_lines=None):
    # Лабораторная 6, задача 1
    # Дана квадратная матрица порядка M (M нечётное). Начиная с A[1][1], двигаясь против
    # часовой стрелки, вывести элементы по спирали: первый столбец (вниз), последняя строка
    # (вправо), последний столбец (вверх), первая строка (влево), затем следующий «виток»...
    # Последним выводится центральный элемент.

    M = int(read_line("Порядок матрицы M (нечётное): ", example_lines))
    A = []
    print(f"Введите {M} строк по {M} чисел через пробел:")
    for i in range(M):
        parts = read_line("", example_lines).split()
        row = []
        for part in parts:
            row.append(int(part))
        A.append(row)

    result = []
    top = 0
    bottom = M - 1
    left = 0
    right = M - 1

    while top <= bottom:
        if top == bottom:                    # остался центральный элемент
            result.append(A[top][left])
            break
        for i in range(top, bottom + 1):     # вниз по левому столбцу
            result.append(A[i][left])
        for j in range(left + 1, right + 1): # вправо по нижней строке
            result.append(A[bottom][j])
        for i in range(bottom - 1, top - 1, -1):   # вверх по правому столбцу
            result.append(A[i][right])
        for j in range(right - 1, left, -1):       # влево по верхней строке
            result.append(A[top][j])
        # сужаем границы — переходим к внутреннему витку
        top += 1
        bottom -= 1
        left += 1
        right -= 1

    for i in range(len(result)):
        if i > 0:
            print(" ", end="")
        print(result[i], end="")
    print()


def task02_row_sum_product(example_lines=None):
    # Лабораторная 6, задача 2
    # Дана матрица M x N и число K (1 <= K <= M). Найти сумму и произведение элементов K-й строки.

    M = int(read_line("Количество строк M: ", example_lines))
    N = int(read_line("Количество столбцов N: ", example_lines))
    matrix = []
    print(f"Введите {M} строк по {N} чисел через пробел:")
    for i in range(M):
        parts = read_line("", example_lines).split()
        row = []
        for part in parts:
            row.append(float(part))
        matrix.append(row)

    K = int(read_line(f"K (1..{M}): ", example_lines))

    row = matrix[K - 1]       # строка с номером K имеет индекс K-1
    total = 0
    product = 1
    for x in row:
        total += x
        product *= x

    print(f"Сумма = {total}, произведение = {product}")


def task03_min_product_column(example_lines=None):
    # Лабораторная 6, задача 3
    # Дана матрица M x N. Найти номер столбца с наименьшим произведением элементов
    # и вывести этот номер и само произведение.

    M = int(read_line("Количество строк M: ", example_lines))
    N = int(read_line("Количество столбцов N: ", example_lines))
    matrix = []
    print(f"Введите {M} строк по {N} чисел через пробел:")
    for i in range(M):
        parts = read_line("", example_lines).split()
        row = []
        for part in parts:
            row.append(float(part))
        matrix.append(row)

    best_column = 0
    best_product = None
    for j in range(N):
        product = 1
        for i in range(M):
            product *= matrix[i][j]
        if best_product is None or product < best_product:
            best_product = product
            best_column = j

    print(f"Столбец номер {best_column + 1}, произведение = {best_product}")


def task04_above_average(example_lines=None):
    # Лабораторная 6, задача 4
    # Дана матрица M x N. В каждом столбце найти количество элементов,
    # больших среднего арифметического этого столбца.

    M = int(read_line("Количество строк M: ", example_lines))
    N = int(read_line("Количество столбцов N: ", example_lines))
    matrix = []
    print(f"Введите {M} строк по {N} чисел через пробел:")
    for i in range(M):
        parts = read_line("", example_lines).split()
        row = []
        for part in parts:
            row.append(float(part))
        matrix.append(row)

    for j in range(N):
        column = []
        for i in range(M):
            column.append(matrix[i][j])
        average = sum(column) / M
        count = 0
        for value in column:
            if value > average:
                count += 1
        print(f"Столбец {j + 1}: среднее = {average:.2f}, больше среднего: {count}")


def task05_first_odd_column(example_lines=None):
    # Лабораторная 6, задача 5
    # Дана целочисленная матрица M x N. Найти номер первого столбца, содержащего
    # только нечётные числа. Если таких нет — вывести 0.

    M = int(read_line("Количество строк M: ", example_lines))
    N = int(read_line("Количество столбцов N: ", example_lines))
    matrix = []
    print(f"Введите {M} строк по {N} целых чисел через пробел:")
    for i in range(M):
        parts = read_line("", example_lines).split()
        row = []
        for part in parts:
            row.append(int(part))
        matrix.append(row)

    answer = 0
    for j in range(N):
        all_odd = True
        for i in range(M):
            if matrix[i][j] % 2 == 0:
                all_odd = False
                break
        if all_odd:
            answer = j + 1
            break

    print(answer)


def task06_swap_min_max_in_rows(example_lines=None):
    # Лабораторная 6, задача 6
    # Дана матрица M x N. В каждой строке поменять местами минимальный и максимальный элементы.

    M = int(read_line("Количество строк M: ", example_lines))
    N = int(read_line("Количество столбцов N: ", example_lines))
    matrix = []
    print(f"Введите {M} строк по {N} чисел через пробел:")
    for i in range(M):
        parts = read_line("", example_lines).split()
        row = []
        for part in parts:
            row.append(float(part))
        matrix.append(row)

    for row in matrix:
        min_index = 0
        max_index = 0
        for j in range(N):
            if row[j] < row[min_index]:
                min_index = j
            if row[j] > row[max_index]:
                max_index = j
        saved_value = row[min_index]
        row[min_index] = row[max_index]
        row[max_index] = saved_value

    print("Результат:")
    for row in matrix:
        for i in range(len(row)):
            if i > 0:
                print(" ", end="")
            print(row[i], end="")
        print()


def task07_swap_min_max_columns(example_lines=None):
    # Лабораторная 6, задача 7
    # Дана матрица M x N. Поменять местами столбцы, содержащие минимальный
    # и максимальный элементы всей матрицы.

    M = int(read_line("Количество строк M: ", example_lines))
    N = int(read_line("Количество столбцов N: ", example_lines))
    matrix = []
    print(f"Введите {M} строк по {N} чисел через пробел:")
    for i in range(M):
        parts = read_line("", example_lines).split()
        row = []
        for part in parts:
            row.append(float(part))
        matrix.append(row)

    min_col = 0
    max_col = 0
    min_value = matrix[0][0]
    max_value = matrix[0][0]
    for i in range(M):
        for j in range(N):
            if matrix[i][j] < min_value:
                min_value = matrix[i][j]
                min_col = j
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
                max_col = j

    # меняем местами элементы двух столбцов в каждой строке
    for i in range(M):
        saved_value = matrix[i][min_col]
        matrix[i][min_col] = matrix[i][max_col]
        matrix[i][max_col] = saved_value

    print(f"Минимум в столбце {min_col + 1}, максимум в столбце {max_col + 1}")
    if min_col == max_col:
        print("Это один и тот же столбец — матрица не меняется")
    print("Результат:")
    for row in matrix:
        for i in range(len(row)):
            if i > 0:
                print(" ", end="")
            print(row[i], end="")
        print()


def task08_swap_quarters(example_lines=None):
    # Лабораторная 6, задача 8
    # Дана матрица M x N (M и N чётные). Поменять местами левую верхнюю
    # и правую нижнюю четверти матрицы.

    M = int(read_line("Количество строк M (чётное): ", example_lines))
    N = int(read_line("Количество столбцов N (чётное): ", example_lines))
    matrix = []
    print(f"Введите {M} строк по {N} чисел через пробел:")
    for i in range(M):
        parts = read_line("", example_lines).split()
        row = []
        for part in parts:
            row.append(float(part))
        matrix.append(row)

    half_m = M // 2
    half_n = N // 2
    for i in range(half_m):
        for j in range(half_n):
            # элемент (i, j) левой верхней четверти соответствует
            # элементу (i + half_m, j + half_n) правой нижней
            i2 = i + half_m
            j2 = j + half_n
            saved_value = matrix[i][j]
            matrix[i][j] = matrix[i2][j2]
            matrix[i2][j2] = saved_value

    print("Результат:")
    for row in matrix:
        for i in range(len(row)):
            if i > 0:
                print(" ", end="")
            print(row[i], end="")
        print()


def task09_sort_rows(example_lines=None):
    # Лабораторная 6, задача 9
    # Дана матрица M x N. Упорядочить строки так, чтобы их первые элементы
    # образовывали возрастающую последовательность.
    # Сортируем строки целиком, сравнивая их по первому элементу (сортировка вставками).

    M = int(read_line("Количество строк M: ", example_lines))
    N = int(read_line("Количество столбцов N: ", example_lines))
    matrix = []
    print(f"Введите {M} строк по {N} чисел через пробел:")
    for i in range(M):
        parts = read_line("", example_lines).split()
        row = []
        for part in parts:
            row.append(float(part))
        matrix.append(row)

    for i in range(1, M):
        current_row = matrix[i]
        j = i - 1
        while j >= 0 and matrix[j][0] > current_row[0]:
            matrix[j + 1] = matrix[j]     # сдвигаем строку вниз
            j -= 1
        matrix[j + 1] = current_row

    print("Результат:")
    for row in matrix:
        for i in range(len(row)):
            if i > 0:
                print(" ", end="")
            print(row[i], end="")
        print()


def task10_diagonal_sums(example_lines=None):
    # Лабораторная 6, задача 10
    # Дана квадратная матрица порядка M. Найти сумму элементов каждой диагонали,
    # параллельной главной (начиная с одноэлементной диагонали).
    # На одной такой диагонали у всех элементов одинаковая разность d = j - i.
    # d меняется от -(M-1) (левый нижний угол) до M-1 (правый верхний угол).

    M = int(read_line("Порядок матрицы M: ", example_lines))
    A = []
    print(f"Введите {M} строк по {M} чисел через пробел:")
    for i in range(M):
        parts = read_line("", example_lines).split()
        row = []
        for part in parts:
            row.append(float(part))
        A.append(row)

    for d in range(-(M - 1), M):
        total = 0
        for i in range(M):
            j = i + d
            if 0 <= j < M:
                total += A[i][j]
        note = ""
        if d == 0:
            note = " (главная)"
        print(f"Диагональ j - i = {d}{note}: сумма = {total}")


TITLES = [
    'Спираль',
    'Сумма и произведение строки',
    'Столбец с минимальным произведением',
    'Элементы выше среднего',
    'Первый столбец из нечётных чисел',
    'Обмен минимума и максимума в строках',
    'Обмен столбцов',
    'Обмен четвертей',
    'Сортировка строк',
    'Суммы диагоналей',
]

EXAMPLES = [
    ['3', '1 2 3', '4 5 6', '7 8 9'],
    ['2', '3', '1 2 3', '4 5 6', '2'],
    ['2', '3', '1 -2 3', '4 5 0'],
    ['3', '2', '1 7', '2 7', '9 7'],
    ['2', '3', '1 3 4', '2 7 9'],
    ['2', '3', '1 8 3', '7 4 2'],
    ['2', '3', '1 9 3', '2 8 -4'],
    ['2', '4', '1 2 3 4', '5 6 7 8'],
    ['3', '2', '3 9', '1 8', '3 7'],
    ['3', '1 2 3', '4 5 6', '7 8 9'],
]


# Подготавливаю входные данные и обычным if выбираю нужную задачу.
def run_task(number, use_example):
    example_lines = None
    if use_example:
        # Копирую пример, потому что read_line забирает использованные строки.
        example_lines = EXAMPLES[number - 1].copy()
    if number == 1:
        task01_spiral(example_lines)
    elif number == 2:
        task02_row_sum_product(example_lines)
    elif number == 3:
        task03_min_product_column(example_lines)
    elif number == 4:
        task04_above_average(example_lines)
    elif number == 5:
        task05_first_odd_column(example_lines)
    elif number == 6:
        task06_swap_min_max_in_rows(example_lines)
    elif number == 7:
        task07_swap_min_max_columns(example_lines)
    elif number == 8:
        task08_swap_quarters(example_lines)
    elif number == 9:
        task09_sort_rows(example_lines)
    elif number == 10:
        task10_diagonal_sums(example_lines)


def main():
    print('Лабораторная работа № 6 «Двумерные массивы»')
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
