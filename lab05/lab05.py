"""Лабораторная работа № 5 «Одномерные массивы». Объединённый запуск."""


def task01_odd_numbers(read_input):
    # Лабораторная 5, задача 1
    # Дано целое N (> 0). Сформировать массив из N первых положительных нечётных чисел: 1, 3, 5, ...

    N = int(read_input("N = "))

    arr = []
    for i in range(N):
        arr.append(2 * i + 1)

    print(arr)


def task02_geometric(read_input):
    # Лабораторная 5, задача 2
    # Дано N (> 1), первый член A и знаменатель D геометрической прогрессии.
    # Сформировать массив из N первых членов: A, A*D, A*D^2, ...

    N = int(read_input("N = "))
    A = float(read_input("A = "))
    D = float(read_input("D = "))

    arr = [A]
    for i in range(1, N):
        arr.append(arr[-1] * D)

    print(arr)


def task03_sum_of_previous(read_input):
    # Лабораторная 5, задача 3
    # Даны целые N (> 2), A и B. Сформировать массив размера N:
    # первый элемент A, второй B, каждый следующий — сумма всех предыдущих.

    N = int(read_input("N = "))
    A = int(read_input("A = "))
    B = int(read_input("B = "))

    arr = [A, B]
    total = A + B                 # сумма всех уже добавленных элементов
    for i in range(2, N):
        arr.append(total)
        total += total            # новый элемент тоже входит в сумму

    print(arr)


def task04_zigzag_output(read_input):
    # Лабораторная 5, задача 4
    # Дан массив A размера N. Вывести элементы в порядке: A1, AN, A2, AN-1, A3, AN-2, ...
    # Используем два указателя: left идёт с начала, right — с конца.

    A = list(map(float, read_input("Элементы массива через пробел: ").split()))

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


def task05_odd_then_even(read_input):
    # Лабораторная 5, задача 5
    # Дан массив A размера N. Вывести сначала элементы с нечётными номерами по возрастанию номеров,
    # затем элементы с чётными номерами по убыванию номеров.
    # Номера в задаче начинаются с 1, а индексы в Python — с 0:
    # номер 1 -> индекс 0, номер 2 -> индекс 1 и т. д.

    A = list(map(float, read_input("Элементы массива через пробел: ").split()))
    N = len(A)

    result = []
    # Нечётные номера 1, 3, 5, ... = индексы 0, 2, 4, ...
    for i in range(0, N, 2):
        result.append(A[i])

    # Чётные номера по убыванию: последний чётный номер = N, если N чётное, иначе N-1
    last_even_number = N if N % 2 == 0 else N - 1
    for number in range(last_even_number, 0, -2):
        result.append(A[number - 1])

    print(result)


def task06_average_range(read_input):
    # Лабораторная 5, задача 6
    # Дан массив размера N и числа K, L (1 <= K <= L <= N).
    # Найти среднее арифметическое элементов с номерами от K до L включительно.

    arr = list(map(float, read_input("Элементы массива через пробел: ").split()))
    K = int(read_input("K = "))
    L = int(read_input("L = "))

    if not (1 <= K <= L <= len(arr)):
        print("Неверные K и L")
    else:
        total = 0
        for number in range(K, L + 1):
            total += arr[number - 1]       # номер -> индекс
        print(f"Среднее = {total / (L - K + 1)}")


def task07_arithmetic_check(read_input):
    # Лабораторная 5, задача 7
    # Дан целочисленный массив без одинаковых чисел. Проверить, образуют ли элементы
    # арифметическую прогрессию. Если да — вывести разность, иначе 0.

    arr = list(map(int, read_input("Элементы массива через пробел: ").split()))

    if len(arr) < 2:
        print(0)
    else:
        d = arr[1] - arr[0]
        is_progression = True
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != d:
                is_progression = False
                break

        print(d if is_progression else 0)


def task08_min_even_positions(read_input):
    # Лабораторная 5, задача 8
    # Дан массив A размера N. Найти минимальный из элементов с чётными номерами: A2, A4, A6, ...
    # Чётные номера 2, 4, 6 соответствуют индексам 1, 3, 5.

    A = list(map(float, read_input("Элементы массива через пробел (минимум 2): ").split()))

    minimum = A[1]
    for i in range(3, len(A), 2):
        if A[i] < minimum:
            minimum = A[i]

    print(f"Минимум среди элементов с чётными номерами = {minimum}")


def task09_last_local_max(read_input):
    # Лабораторная 5, задача 9
    # Дан массив размера N. Найти номер его последнего локального максимума
    # (элемента, который больше любого из своих соседей).
    # У крайних элементов только один сосед.

    arr = list(map(float, read_input("Элементы массива через пробел: ").split()))
    N = len(arr)

    answer = 0      # 0 — если локальных максимумов нет
    for i in range(N):
        bigger_than_left = (i == 0) or (arr[i] > arr[i - 1])
        bigger_than_right = (i == N - 1) or (arr[i] > arr[i + 1])
        if bigger_than_left and bigger_than_right:
            answer = i + 1          # запоминаем номер (с 1); в итоге останется последний

    print(f"Номер последнего локального максимума: {answer}")


def task10_find_duplicates(read_input):
    # Лабораторная 5, задача 10
    # Дан целочисленный массив, содержащий ровно два одинаковых элемента.
    # Найти номера одинаковых элементов и вывести их по возрастанию.

    arr = list(map(int, read_input("Элементы массива через пробел: ").split()))
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
    '1': ('Первые нечётные числа', task01_odd_numbers, ('4',)),
    '2': ('Геометрическая прогрессия', task02_geometric, ('4', '2', '-3')),
    '3': ('Сумма предыдущих', task03_sum_of_previous, ('6', '1', '2')),
    '4': ('Обход от краёв к центру', task04_zigzag_output, ('1 2 3 4 5',)),
    '5': ('Нечётные и чётные места', task05_odd_then_even, ('1 2 3 4 5',)),
    '6': ('Среднее на участке', task06_average_range, ('1 2 3 4', '2', '4')),
    '7': ('Проверка прогрессии', task07_arithmetic_check, ('7 5 3 1',)),
    '8': ('Минимум на чётных местах', task08_min_even_positions, ('0 5 0 3 -4',)),
    '9': ('Последний локальный максимум', task09_last_local_max, ('4 1 3 2 5',)),
    '10': ('Пара одинаковых элементов', task10_find_duplicates, ('8 2 3 2',)),
}


def main():
    print('Лабораторная работа № 5 «Одномерные массивы»')
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
