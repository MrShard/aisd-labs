"""Лабораторная работа № 10 «Итеративный бинарный поиск». Объединённый запуск."""


# Лабораторная 10. Бинарный поиск (итеративный).
#
# Алгоритм:
#   1. left = 0, right = последний индекс массива.
#   2. Пока left <= right:
#      a. mid = (left + right) // 2;
#      b. если a[mid] == искомому — возвращаем mid;
#      c. если a[mid] > искомого — right = mid - 1 (ищем в левой половине);
#      d. если a[mid] < искомого — left = mid + 1 (ищем в правой половине).
#   3. Не нашли — возвращаем -1.
# Сложность: O(log n). Массив обязательно должен быть отсортирован.


def binary_search(arr, target, show_steps=True):
    left = 0
    right = len(arr) - 1
    step = 0
    while left <= right:
        step += 1
        mid = (left + right) // 2
        if show_steps:
            print(f"Шаг {step}: left={left}, right={right}, mid={mid}, a[mid]={arr[mid]}")
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def run_task(read_input):
    text = read_input("Введите отсортированные числа через пробел (Enter — пример): ")
    numbers = list(map(int, text.split())) if text.strip() else [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    numbers.sort()   # на случай, если ввели неотсортированный массив
    print(f"Массив: {numbers}")
    target = int(read_input("Что ищем: "))

    index = binary_search(numbers, target)
    if index == -1:
        print("Элемент не найден (-1)")
    else:
        print(f"Элемент {target} найден по индексу {index}")


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
    print('Лабораторная работа № 10 «Итеративный бинарный поиск»')
    run_selected(run_task, ('2 5 8 12 16 23 38 56 72 91', '23'))


if __name__ == "__main__":
    main()
