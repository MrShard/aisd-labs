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
    """Обход в ширину по списку ожидающих узлов."""
    result = []
    if root is None:
        return result
    pending = [root]
    index = 0
    while index < len(pending):
        node = pending[index]
        index += 1
        result.append(node.value)
        if node.left:
            pending.append(node.left)
        if node.right:
            pending.append(node.right)
    return result


def print_tree(node, prefix="", is_left=None):
    """Печать дерева «боком»: правое поддерево сверху, левое снизу."""
    if node is None:
        return
    right_prefix = prefix + "    "
    if is_left:
        right_prefix = prefix + "│   "
    print_tree(node.right, right_prefix, False)

    connector = ""
    if is_left is not None:
        if is_left:
            connector = "└── "
        else:
            connector = "┌── "
    print(prefix + connector + str(node.value))

    left_prefix = prefix + "    "
    if is_left is not None and not is_left:
        left_prefix = prefix + "│   "
    print_tree(node.left, left_prefix, True)


# В ручном режиме читаю строку с клавиатуры. В примере беру первую готовую строку.
def read_line(prompt, example_lines):
    if example_lines is None:
        return input(prompt)

    # pop(0) возвращает первую строку и убирает её из списка этого запуска.
    line = example_lines.pop(0)
    print(prompt + line)
    return line


def run_task(example_lines=None):
    text = read_line("Введите числа для дерева через пробел (Enter — пример): ", example_lines)
    if text.strip() == "":
        values = [50, 30, 20, 40, 70, 60, 80]
    else:
        values = []
        for part in text.split():
            values.append(int(part))

    tree = None
    for v in values:
        tree = insert(tree, v)

    print("\nДерево:")
    print_tree(tree)

    print("\nПрямой обход (pre-order):       ", preorder(tree, []))
    print("Симметричный обход (in-order):  ", inorder(tree, []))
    print("Обратный обход (post-order):    ", postorder(tree, []))
    print("Обход в ширину (level-order):   ", level_order(tree))

    target = int(read_line("\nКакое значение найти? ", example_lines))
    found_node = search(tree, target)
    if found_node is None:
        print("Элемент не найден")
    else:
        print("Элемент найден")


def main():
    print('Лабораторная работа № 11 «Бинарное дерево поиска»')
    mode = input("Enter — пример, 1 — ручной ввод: ").strip()
    if mode == "":
        run_task(['50 30 20 40 70 60 80', '60'])
    elif mode == "1":
        run_task()
    else:
        print("Для примера нажмите Enter, для ручного ввода введите 1.")


if __name__ == "__main__":
    main()
