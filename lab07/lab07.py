"""Лабораторная работа № 7 «Сортировка пузырьком». Объединённый запуск."""


# Лабораторная 7. Сортировка пузырьком.
#
# Алгоритм:
#   1. Проходим по массиву от начала до конца.
#   2. Сравниваем каждую пару соседних элементов.
#   3. Если текущий элемент больше следующего — меняем их местами.
#   4. Доходим до конца массива: наибольший элемент «всплыл» на последнее место.
#   5. Повторяем проходы, пока массив не отсортирован.
# Сложность: O(n^2).
#
# Улучшения:
#   - после каждого прохода последний элемент уже на месте,
#     поэтому следующий проход на 1 короче;
#   - если за проход не было ни одного обмена, массив уже отсортирован и можно остановиться.


def bubble_sort(arr, show_steps=True):
    a = arr.copy()
    n = len(a)
    for pass_number in range(n - 1):
        swapped = False
        # после pass_number проходов последние pass_number элементов уже на местах
        for i in range(n - 1 - pass_number):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
        if show_steps:
            print(f"Проход {pass_number + 1}: {a}")
        if not swapped:      # обменов не было — массив отсортирован
            break
    return a


def run_task(read_input):
    text = read_input("Введите числа через пробел (Enter — пример): ")
    numbers = list(map(int, text.split())) if text.strip() else [5, 1, 4, 2, 8, 3]
    print(f"Исходный массив: {numbers}")
    result = bubble_sort(numbers)
    print(f"Отсортированный: {result}")


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


def main():
    print('Лабораторная работа № 7 «Сортировка пузырьком»')
    run_selected(run_task, ('5 1 4 2',))


if __name__ == "__main__":
    main()
