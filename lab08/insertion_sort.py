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
            ordered = []
            remaining = []
            for index in range(len(a)):
                if index <= i:
                    ordered.append(a[index])
                else:
                    remaining.append(a[index])
            print(f"Шаг {i}: вставили {key} -> {ordered} | {remaining}")
    return a


if __name__ == "__main__":
    text = input("Введите числа через пробел (Enter — пример): ")
    if text.strip() == "":
        numbers = [12, 11, 13, 5, 6]
    else:
        numbers = []
        for part in text.split():
            numbers.append(int(part))
    print(f"Исходный массив: {numbers}")
    print("(слева от | — отсортированная часть, справа — ещё не обработанная)")
    result = insertion_sort(numbers)
    print(f"Отсортированный: {result}")
