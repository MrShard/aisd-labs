"""Лабораторная работа № 6 «Двумерные массивы». Объединённый запуск."""


def task01_spiral(read_input):
    # Лабораторная 6, задача 1
    # Дана квадратная матрица порядка M (M нечётное). Начиная с A[1][1], двигаясь против
    # часовой стрелки, вывести элементы по спирали: первый столбец (вниз), последняя строка
    # (вправо), последний столбец (вверх), первая строка (влево), затем следующий «виток»...
    # Последним выводится центральный элемент.

    M = int(read_input("Порядок матрицы M (нечётное): "))
    A = []
    print(f"Введите {M} строк по {M} чисел через пробел:")
    for i in range(M):
        A.append(list(map(int, read_input().split())))

    result = []
    top, bottom, left, right = 0, M - 1, 0, M - 1   # границы текущего витка

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

    print(*result)


def task02_row_sum_product(read_input):
    # Лабораторная 6, задача 2
    # Дана матрица M x N и число K (1 <= K <= M). Найти сумму и произведение элементов K-й строки.

    M = int(read_input("Количество строк M: "))
    N = int(read_input("Количество столбцов N: "))
    matrix = []
    print(f"Введите {M} строк по {N} чисел через пробел:")
    for i in range(M):
        matrix.append(list(map(float, read_input().split())))

    K = int(read_input(f"K (1..{M}): "))

    row = matrix[K - 1]       # строка с номером K имеет индекс K-1
    total = 0
    product = 1
    for x in row:
        total += x
        product *= x

    print(f"Сумма = {total}, произведение = {product}")


def task03_min_product_column(read_input):
    # Лабораторная 6, задача 3
    # Дана матрица M x N. Найти номер столбца с наименьшим произведением элементов
    # и вывести этот номер и само произведение.

    M = int(read_input("Количество строк M: "))
    N = int(read_input("Количество столбцов N: "))
    matrix = []
    print(f"Введите {M} строк по {N} чисел через пробел:")
    for i in range(M):
        matrix.append(list(map(float, read_input().split())))

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


def task04_above_average(read_input):
    # Лабораторная 6, задача 4
    # Дана матрица M x N. В каждом столбце найти количество элементов,
    # больших среднего арифметического этого столбца.

    M = int(read_input("Количество строк M: "))
    N = int(read_input("Количество столбцов N: "))
    matrix = []
    print(f"Введите {M} строк по {N} чисел через пробел:")
    for i in range(M):
        matrix.append(list(map(float, read_input().split())))

    for j in range(N):
        column = [matrix[i][j] for i in range(M)]
        average = sum(column) / M
        count = 0
        for x in column:
            if x > average:
                count += 1
        print(f"Столбец {j + 1}: среднее = {average:.2f}, больше среднего: {count}")


def task05_first_odd_column(read_input):
    # Лабораторная 6, задача 5
    # Дана целочисленная матрица M x N. Найти номер первого столбца, содержащего
    # только нечётные числа. Если таких нет — вывести 0.

    M = int(read_input("Количество строк M: "))
    N = int(read_input("Количество столбцов N: "))
    matrix = []
    print(f"Введите {M} строк по {N} целых чисел через пробел:")
    for i in range(M):
        matrix.append(list(map(int, read_input().split())))

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


def task06_swap_min_max_in_rows(read_input):
    # Лабораторная 6, задача 6
    # Дана матрица M x N. В каждой строке поменять местами минимальный и максимальный элементы.

    M = int(read_input("Количество строк M: "))
    N = int(read_input("Количество столбцов N: "))
    matrix = []
    print(f"Введите {M} строк по {N} чисел через пробел:")
    for i in range(M):
        matrix.append(list(map(float, read_input().split())))

    for row in matrix:
        min_index = 0
        max_index = 0
        for j in range(N):
            if row[j] < row[min_index]:
                min_index = j
            if row[j] > row[max_index]:
                max_index = j
        row[min_index], row[max_index] = row[max_index], row[min_index]

    print("Результат:")
    for row in matrix:
        print(*row)


def task07_swap_min_max_columns(read_input):
    # Лабораторная 6, задача 7
    # Дана матрица M x N. Поменять местами столбцы, содержащие минимальный
    # и максимальный элементы всей матрицы.

    M = int(read_input("Количество строк M: "))
    N = int(read_input("Количество столбцов N: "))
    matrix = []
    print(f"Введите {M} строк по {N} чисел через пробел:")
    for i in range(M):
        matrix.append(list(map(float, read_input().split())))

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
        matrix[i][min_col], matrix[i][max_col] = matrix[i][max_col], matrix[i][min_col]

    print(f"Минимум в столбце {min_col + 1}, максимум в столбце {max_col + 1}")
    if min_col == max_col:
        print("Это один и тот же столбец — матрица не меняется")
    print("Результат:")
    for row in matrix:
        print(*row)


def task08_swap_quarters(read_input):
    # Лабораторная 6, задача 8
    # Дана матрица M x N (M и N чётные). Поменять местами левую верхнюю
    # и правую нижнюю четверти матрицы.

    M = int(read_input("Количество строк M (чётное): "))
    N = int(read_input("Количество столбцов N (чётное): "))
    matrix = []
    print(f"Введите {M} строк по {N} чисел через пробел:")
    for i in range(M):
        matrix.append(list(map(float, read_input().split())))

    half_m = M // 2
    half_n = N // 2
    for i in range(half_m):
        for j in range(half_n):
            # элемент (i, j) левой верхней четверти соответствует
            # элементу (i + half_m, j + half_n) правой нижней
            i2 = i + half_m
            j2 = j + half_n
            matrix[i][j], matrix[i2][j2] = matrix[i2][j2], matrix[i][j]

    print("Результат:")
    for row in matrix:
        print(*row)


def task09_sort_rows(read_input):
    # Лабораторная 6, задача 9
    # Дана матрица M x N. Упорядочить строки так, чтобы их первые элементы
    # образовывали возрастающую последовательность.
    # Сортируем строки целиком, сравнивая их по первому элементу (сортировка вставками).

    M = int(read_input("Количество строк M: "))
    N = int(read_input("Количество столбцов N: "))
    matrix = []
    print(f"Введите {M} строк по {N} чисел через пробел:")
    for i in range(M):
        matrix.append(list(map(float, read_input().split())))

    for i in range(1, M):
        current_row = matrix[i]
        j = i - 1
        while j >= 0 and matrix[j][0] > current_row[0]:
            matrix[j + 1] = matrix[j]     # сдвигаем строку вниз
            j -= 1
        matrix[j + 1] = current_row

    print("Результат:")
    for row in matrix:
        print(*row)


def task10_diagonal_sums(read_input):
    # Лабораторная 6, задача 10
    # Дана квадратная матрица порядка M. Найти сумму элементов каждой диагонали,
    # параллельной главной (начиная с одноэлементной диагонали).
    # На одной такой диагонали у всех элементов одинаковая разность d = j - i.
    # d меняется от -(M-1) (левый нижний угол) до M-1 (правый верхний угол).

    M = int(read_input("Порядок матрицы M: "))
    A = []
    print(f"Введите {M} строк по {M} чисел через пробел:")
    for i in range(M):
        A.append(list(map(float, read_input().split())))

    for d in range(-(M - 1), M):
        total = 0
        for i in range(M):
            j = i + d
            if 0 <= j < M:
                total += A[i][j]
        note = " (главная)" if d == 0 else ""
        print(f"Диагональ j - i = {d}{note}: сумма = {total}")


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
    '1': ('Спираль', task01_spiral, ('3', '1 2 3', '4 5 6', '7 8 9')),
    '2': ('Сумма и произведение строки', task02_row_sum_product, ('2', '3', '1 2 3', '4 5 6', '2')),
    '3': ('Столбец с минимальным произведением', task03_min_product_column, ('2', '3', '1 -2 3', '4 5 0')),
    '4': ('Элементы выше среднего', task04_above_average, ('3', '2', '1 7', '2 7', '9 7')),
    '5': ('Первый столбец из нечётных чисел', task05_first_odd_column, ('2', '3', '1 3 4', '2 7 9')),
    '6': ('Обмен минимума и максимума в строках', task06_swap_min_max_in_rows, ('2', '3', '1 8 3', '7 4 2')),
    '7': ('Обмен столбцов', task07_swap_min_max_columns, ('2', '3', '1 9 3', '2 8 -4')),
    '8': ('Обмен четвертей', task08_swap_quarters, ('2', '4', '1 2 3 4', '5 6 7 8')),
    '9': ('Сортировка строк', task09_sort_rows, ('3', '2', '3 9', '1 8', '3 7')),
    '10': ('Суммы диагоналей', task10_diagonal_sums, ('3', '1 2 3', '4 5 6', '7 8 9')),
}


def main():
    print('Лабораторная работа № 6 «Двумерные массивы»')
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
