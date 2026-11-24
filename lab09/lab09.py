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
            saved_value = a[i]
            a[i] = a[min_index]
            a[min_index] = saved_value
        if show_steps:
            ordered = []
            remaining = []
            for index in range(len(a)):
                if index <= i:
                    ordered.append(a[index])
                else:
                    remaining.append(a[index])
            print(f"Шаг {i + 1}: минимум {a[i]} поставлен на позицию {i} -> {ordered} | {remaining}")
    return a


# В ручном режиме читаю строку с клавиатуры. В примере беру первую готовую строку.
def read_line(prompt, example_lines):
    if example_lines is None:
        return input(prompt)

    # pop(0) возвращает первую строку и убирает её из списка этого запуска.
    line = example_lines.pop(0)
    print(prompt + line)
    return line


def run_task(example_lines=None):
    text = read_line("Введите числа через пробел (Enter — пример): ", example_lines)
    if text.strip() == "":
        numbers = [64, 25, 12, 22, 11]
    else:
        numbers = []
        for part in text.split():
            numbers.append(int(part))
    print(f"Исходный массив: {numbers}")
    result = selection_sort(numbers)
    print(f"Отсортированный: {result}")


def main():
    print('Лабораторная работа № 9 «Сортировка выбором»')
    mode = input("Enter — пример, 1 — ручной ввод: ").strip()
    if mode == "":
        run_task(['64 25 12 22 11'])
    elif mode == "1":
        run_task()
    else:
        print("Для примера нажмите Enter, для ручного ввода введите 1.")


if __name__ == "__main__":
    main()
