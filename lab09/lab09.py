"""Лабораторная работа № 9 «Сортировка выбором». Объединённый запуск."""


# Лабораторная 9. Сортировка выбором.
#
# Алгоритм (по возрастанию):
#   1. Перебираем массив от первого элемента до предпоследнего (индекс i).
#   2. Считаем текущий элемент a[i] наименьшим (запоминаем его индекс min_index).
#   3. Проходим по оставшейся неотсортированной части, начиная с i + 1.
#   4. Если нашли элемент меньше, обновляем min_index.
#   5. После внутреннего цикла меняем местами a[i] и a[min_index], если они различаются.
#   6. Повторяем для следующего i.
# Сложность: O(n^2).


def selection_sort(arr, show_steps=True):
    a = arr.copy()
    n = len(a)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j
        if min_index != i:
            a[i], a[min_index] = a[min_index], a[i]
        if show_steps:
            print(f"Шаг {i + 1}: минимум {a[i]} поставлен на позицию {i} -> "
                  f"{a[:i + 1]} | {a[i + 1:]}")
    return a


def run_task(read_input):
    text = read_input("Введите числа через пробел (Enter — пример): ")
    numbers = list(map(int, text.split())) if text.strip() else [64, 25, 12, 22, 11]
    print(f"Исходный массив: {numbers}")
    result = selection_sort(numbers)
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
    print('Лабораторная работа № 9 «Сортировка выбором»')
    run_selected(run_task, ('64 25 12 22 11',))


if __name__ == "__main__":
    main()
