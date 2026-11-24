# Лабораторная 4, задача 9
# Рекурсивное решение головоломки «Ханойская башня».
# Чтобы перенести n дисков со стержня source на target:
#   1) перенести n-1 дисков на вспомогательный стержень helper;
#   2) перенести самый большой диск на target;
#   3) перенести n-1 дисков с helper на target.
# Всего ходов: 2^n - 1.

def hanoi(n, source, target, helper, moves=0):
    if n == 0:
        return moves

    moves = hanoi(n - 1, source, helper, target, moves)

    moves += 1
    print(f"Ход {moves}: диск {n} со стержня {source} на стержень {target}")

    return hanoi(n - 1, helper, target, source, moves)


n = int(input("Количество дисков: "))
moves = hanoi(n, "A", "C", "B")
print(f"Всего ходов: {moves}")
