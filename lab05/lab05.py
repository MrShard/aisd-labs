"""Лабораторная работа № 5 «Одномерные массивы». Объединённый запуск."""


# В ручном режиме читаю строку с клавиатуры. В примере беру первую готовую строку.
def read_line(prompt, example_lines):
    if example_lines is None:
        return input(prompt)

    # pop(0) возвращает первую строку и убирает её из списка этого запуска.
    line = example_lines.pop(0)
    print(prompt + line)
    return line


def task01_odd_numbers(example_lines=None):
    # Лабораторная 5, задача 1
    # Дано целое N (> 0). Сформировать массив из N первых положительных нечётных чисел: 1, 3, 5, ...

    N = int(read_line("N = ", example_lines))

    arr = []
    for i in range(N):
        arr.append(2 * i + 1)

    print(arr)


def task02_geometric(example_lines=None):
    # Лабораторная 5, задача 2
    # Дано N (> 1), первый член A и знаменатель D геометрической прогрессии.
    # Сформировать массив из N первых членов: A, A*D, A*D^2, ...

    N = int(read_line("N = ", example_lines))
    A = float(read_line("A = ", example_lines))
    D = float(read_line("D = ", example_lines))

    arr = [A]
    for i in range(1, N):
        arr.append(arr[i - 1] * D)

    print(arr)


def task03_sum_of_previous(example_lines=None):
    # Лабораторная 5, задача 3
    # Даны целые N (> 2), A и B. Сформировать массив размера N:
    # первый элемент A, второй B, каждый следующий — сумма всех предыдущих.

    N = int(read_line("N = ", example_lines))
    A = int(read_line("A = ", example_lines))
    B = int(read_line("B = ", example_lines))

    arr = [A, B]
    total = A + B                 # сумма всех уже добавленных элементов
    for i in range(2, N):
        arr.append(total)
        total += total            # новый элемент тоже входит в сумму

    print(arr)


def task04_zigzag_output(example_lines=None):
    # Лабораторная 5, задача 4
    # Дан массив A размера N. Вывести элементы в порядке: A1, AN, A2, AN-1, A3, AN-2, ...
    # Используем два указателя: left идёт с начала, right — с конца.

    parts = read_line("Элементы массива через пробел: ", example_lines).split()
    A = []
    for part in parts:
        A.append(float(part))

    result = []
    left = 0
    right = len(A) - 1
    while left <= right:
        result.append(A[left])
        if left != right:          # чтобы не вывести средний элемент дважды
            result.append(A[right])
        left += 1
        right -= 1

    print(result)


def task05_odd_then_even(example_lines=None):
    # Лабораторная 5, задача 5
    # Дан массив A размера N. Вывести сначала элементы с нечётными номерами по возрастанию номеров,
    # затем элементы с чётными номерами по убыванию номеров.
    # Номера в задаче начинаются с 1, а индексы в Python — с 0:
    # номер 1 -> индекс 0, номер 2 -> индекс 1 и т. д.

    parts = read_line("Элементы массива через пробел: ", example_lines).split()
    A = []
    for part in parts:
        A.append(float(part))
    N = len(A)

    result = []
    # Нечётные номера 1, 3, 5, ... = индексы 0, 2, 4, ...
    for i in range(0, N, 2):
        result.append(A[i])

    last_even_number = N
    if N % 2 != 0:
        last_even_number = N - 1
    for number in range(last_even_number, 0, -2):
        result.append(A[number - 1])

    print(result)


def task06_average_range(example_lines=None):
    # Лабораторная 5, задача 6
    # Дан массив размера N и числа K, L (1 <= K <= L <= N).
    # Найти среднее арифметическое элементов с номерами от K до L включительно.

    parts = read_line("Элементы массива через пробел: ", example_lines).split()
    arr = []
    for part in parts:
        arr.append(float(part))
    K = int(read_line("K = ", example_lines))
    L = int(read_line("L = ", example_lines))

    if not (1 <= K <= L <= len(arr)):
        print("Неверные K и L")
    else:
        total = 0
        for number in range(K, L + 1):
            total += arr[number - 1]       # номер -> индекс
        print(f"Среднее = {total / (L - K + 1)}")


def task07_arithmetic_check(example_lines=None):
    # Лабораторная 5, задача 7
    # Дан целочисленный массив без одинаковых чисел. Проверить, образуют ли элементы
    # арифметическую прогрессию. Если да — вывести разность, иначе 0.

    parts = read_line("Элементы массива через пробел: ", example_lines).split()
    arr = []
    for part in parts:
        arr.append(int(part))

    if len(arr) < 2:
        print(0)
    else:
        d = arr[1] - arr[0]
        is_progression = True
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != d:
                is_progression = False
                break

        if is_progression:
            print(d)
        else:
            print(0)


def task08_min_even_positions(example_lines=None):
    # Лабораторная 5, задача 8
    # Дан массив A размера N. Найти минимальный из элементов с чётными номерами: A2, A4, A6, ...
    # Чётные номера 2, 4, 6 соответствуют индексам 1, 3, 5.

    parts = read_line("Элементы массива через пробел (минимум 2): ", example_lines).split()
    A = []
    for part in parts:
        A.append(float(part))

    minimum = A[1]
    for i in range(3, len(A), 2):
        if A[i] < minimum:
            minimum = A[i]

    print(f"Минимум среди элементов с чётными номерами = {minimum}")


def task09_last_local_max(example_lines=None):
    # Лабораторная 5, задача 9
    # Дан массив размера N. Найти номер его последнего локального максимума
    # (элемента, который больше любого из своих соседей).
    # У крайних элементов только один сосед.

    parts = read_line("Элементы массива через пробел: ", example_lines).split()
    arr = []
    for part in parts:
        arr.append(float(part))
    N = len(arr)

    answer = 0      # 0 — если локальных максимумов нет
    for i in range(N):
        bigger_than_left = True
        bigger_than_right = True
        if i > 0:
            bigger_than_left = arr[i] > arr[i - 1]
        if i < N - 1:
            bigger_than_right = arr[i] > arr[i + 1]
        if bigger_than_left and bigger_than_right:
            answer = i + 1          # запоминаем номер (с 1); в итоге останется последний

    print(f"Номер последнего локального максимума: {answer}")


def task10_find_duplicates(example_lines=None):
    # Лабораторная 5, задача 10
    # Дан целочисленный массив, содержащий ровно два одинаковых элемента.
    # Найти номера одинаковых элементов и вывести их по возрастанию.

    parts = read_line("Элементы массива через пробел: ", example_lines).split()
    arr = []
    for part in parts:
        arr.append(int(part))
    N = len(arr)

    found = False
    for i in range(N):
        for j in range(i + 1, N):          # сравниваем каждую пару (i < j) один раз
            if arr[i] == arr[j]:
                print(f"Номера одинаковых элементов: {i + 1} {j + 1}")
                found = True
                break
        if found:
            break

    if not found:
        print("Одинаковых элементов нет")


TITLES = [
    'Первые нечётные числа',
    'Геометрическая прогрессия',
    'Сумма предыдущих',
    'Обход от краёв к центру',
    'Нечётные и чётные места',
    'Среднее на участке',
    'Проверка прогрессии',
    'Минимум на чётных местах',
    'Последний локальный максимум',
    'Пара одинаковых элементов',
]

EXAMPLES = [
    ['4'],
    ['4', '2', '-3'],
    ['6', '1', '2'],
    ['1 2 3 4 5'],
    ['1 2 3 4 5'],
    ['1 2 3 4', '2', '4'],
    ['7 5 3 1'],
    ['0 5 0 3 -4'],
    ['4 1 3 2 5'],
    ['8 2 3 2'],
]


# Подготавливаю входные данные и обычным if выбираю нужную задачу.
def run_task(number, use_example):
    example_lines = None
    if use_example:
        # Копирую пример, потому что read_line забирает использованные строки.
        example_lines = EXAMPLES[number - 1].copy()
    if number == 1:
        task01_odd_numbers(example_lines)
    elif number == 2:
        task02_geometric(example_lines)
    elif number == 3:
        task03_sum_of_previous(example_lines)
    elif number == 4:
        task04_zigzag_output(example_lines)
    elif number == 5:
        task05_odd_then_even(example_lines)
    elif number == 6:
        task06_average_range(example_lines)
    elif number == 7:
        task07_arithmetic_check(example_lines)
    elif number == 8:
        task08_min_even_positions(example_lines)
    elif number == 9:
        task09_last_local_max(example_lines)
    elif number == 10:
        task10_find_duplicates(example_lines)


def main():
    print('Лабораторная работа № 5 «Одномерные массивы»')
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
