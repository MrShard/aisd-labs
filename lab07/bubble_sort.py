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
                saved_value = a[i]
                a[i] = a[i + 1]
                a[i + 1] = saved_value
                swapped = True
        if show_steps:
            print(f"Проход {pass_number + 1}: {a}")
        if not swapped:      # обменов не было — массив отсортирован
            break
    return a


if __name__ == "__main__":
    text = input("Введите числа через пробел (Enter — пример): ")
    if text.strip() == "":
        numbers = [5, 1, 4, 2, 8, 3]
    else:
        numbers = []
        for part in text.split():
            numbers.append(int(part))
    print(f"Исходный массив: {numbers}")
    result = bubble_sort(numbers)
    print(f"Отсортированный: {result}")
