"""Лабораторная работа № 8 «Сортировка вставками». Объединённый запуск."""


# Лабораторная 8. Сортировка вставками.
#
# Алгоритм:
#   1. Считаем первый элемент отсортированной частью массива.
#   2. Для каждого следующего элемента (со второго до последнего):
#      - сохраняем его во временную переменную key;
#      - идём по отсортированной части справа налево;
#      - пока элемент отсортированной части больше key, сдвигаем его на одну позицию вправо;
#      - вставляем key на освободившееся место.
#   3. Повторяем для всех элементов.
# Сложность: O(n^2), но на почти отсортированных массивах работает быстро.


def insertion_sort(arr, show_steps=True):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]              # текущий элемент, который вставляем
        j = i - 1               # последний индекс отсортированной части
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]     # сдвигаем больший элемент вправо
            j -= 1
        a[j + 1] = key          # вставляем на найденную позицию
        if show_steps:
            print(f"Шаг {i}: вставили {key} -> {a[:i + 1]} | {a[i + 1:]}")
    return a


def run_task(read_input):
    text = read_input("Введите числа через пробел (Enter — пример): ")
    numbers = list(map(int, text.split())) if text.strip() else [12, 11, 13, 5, 6]
    print(f"Исходный массив: {numbers}")
    print("(слева от | — отсортированная часть, справа — ещё не обработанная)")
    result = insertion_sort(numbers)
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
    print('Лабораторная работа № 8 «Сортировка вставками»')
    run_selected(run_task, ('4 2 4 1',))


if __name__ == "__main__":
    main()
