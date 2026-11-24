"""Лабораторная работа № 11 «Бинарное дерево поиска». Объединённый запуск."""


# Лабораторная 11. Бинарное дерево поиска и его обходы.
#
# Бинарное дерево поиска (BST): у каждого узла не больше двух детей;
# всё, что в левом поддереве, меньше значения узла, всё, что в правом — больше или равно.
#
# Обходы в глубину (рекурсивные):
#   - прямой (pre-order):     узел -> левое поддерево -> правое поддерево
#   - симметричный (in-order): левое -> узел -> правое  (для BST даёт значения по возрастанию)
#   - обратный (post-order):  левое -> правое -> узел
# Обход в ширину (level-order): по уровням сверху вниз, слева направо, с помощью очереди.

from collections import deque


class Node:
    """Узел бинарного дерева."""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    """Вставка значения в дерево. Возвращает корень."""
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root


def search(root, value):
    """Поиск узла по значению. Возвращает узел или None."""
    if root is None or root.value == value:
        return root
    if value > root.value:
        return search(root.right, value)
    return search(root.left, value)


def preorder(root, result):
    if root:
        result.append(root.value)
        preorder(root.left, result)
        preorder(root.right, result)
    return result


def inorder(root, result):
    if root:
        inorder(root.left, result)
        result.append(root.value)
        inorder(root.right, result)
    return result


def postorder(root, result):
    if root:
        postorder(root.left, result)
        postorder(root.right, result)
        result.append(root.value)
    return result


def level_order(root):
    """Обход в ширину: берём узел из начала очереди, его детей кладём в конец."""
    result = []
    if root is None:
        return result
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


def print_tree(node, prefix="", is_left=None):
    """Печать дерева «боком»: правое поддерево сверху, левое снизу."""
    if node is None:
        return
    print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
    connector = "" if is_left is None else ("└── " if is_left else "┌── ")
    print(prefix + connector + str(node.value))
    print_tree(node.left, prefix + ("    " if is_left or is_left is None else "│   "), True)


def run_task(read_input):
    text = read_input("Введите числа для дерева через пробел (Enter — пример): ")
    values = list(map(int, text.split())) if text.strip() else [50, 30, 20, 40, 70, 60, 80]

    tree = None
    for v in values:
        tree = insert(tree, v)

    print("\nДерево:")
    print_tree(tree)

    print("\nПрямой обход (pre-order):       ", preorder(tree, []))
    print("Симметричный обход (in-order):  ", inorder(tree, []))
    print("Обратный обход (post-order):    ", postorder(tree, []))
    print("Обход в ширину (level-order):   ", level_order(tree))

    target = int(read_input("\nКакое значение найти? "))
    print("Элемент найден" if search(tree, target) else "Элемент не найден")


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
    print('Лабораторная работа № 11 «Бинарное дерево поиска»')
    run_selected(run_task, ('50 30 20 40 70 60 80', '60'))


if __name__ == "__main__":
    main()
