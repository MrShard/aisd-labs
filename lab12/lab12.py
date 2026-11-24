"""Лабораторная работа № 12 «Очередь». Объединённый запуск."""


# Лабораторная 12. Очередь (FIFO — First In, First Out: «первым пришёл — первым ушёл»).
#
# Реализуем свою очередь на связном списке, чтобы видеть, как она устроена внутри,
# и сравниваем с готовыми вариантами: collections.deque и queue.Queue.
#
# Операции:
#   put(item)   — добавить элемент в конец очереди
#   get()       — извлечь элемент из начала очереди
#   peek()      — посмотреть первый элемент, не удаляя
#   empty()     — проверка на пустоту
#   size()      — количество элементов
#   contains(x) — есть ли элемент в очереди
#   clear()     — очистить очередь
#   перебор     — for item in q

from collections import deque
import queue


class _QueueNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class MyQueue:
    """Очередь на односвязном списке: head — начало (отсюда забираем), tail — конец (сюда кладём).
    Добавление и извлечение работают за O(1)."""

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def put(self, item):
        node = _QueueNode(item)
        if self.tail is None:          # очередь пуста: новый узел и начало, и конец
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self._size += 1

    def get(self):
        if self.empty():
            raise IndexError("Очередь пуста")
        node = self.head
        self.head = node.next
        if self.head is None:          # забрали последний элемент
            self.tail = None
        self._size -= 1
        return node.value

    def peek(self):
        if self.empty():
            raise IndexError("Очередь пуста")
        return self.head.value

    def empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def contains(self, item):
        for value in self:
            if value == item:
                return True
        return False

    def clear(self):
        self.head = self.tail = None
        self._size = 0

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __str__(self):
        return "начало -> [" + ", ".join(str(v) for v in self) + "] <- конец"


def demo_my_queue():
    print("=== Своя очередь MyQueue ===")
    q = MyQueue()
    print("Пустая?", q.empty())

    for item in [1, 2, 3, 4]:
        q.put(item)
        print(f"put({item}):", q)

    print("Размер:", q.size())
    print("Первый элемент (peek):", q.peek())
    print("get() ->", q.get(), "| теперь:", q)
    print("Есть ли 3?", q.contains(3))
    print("Есть ли 1?", q.contains(1))

    print("Перебор:", end=" ")
    for item in q:
        print(item, end=" ")
    print()

    q.clear()
    print("После clear():", q, "| пустая?", q.empty())

    try:
        q.get()
    except IndexError as e:
        print("Ошибка при get() из пустой очереди:", e)


def demo_deque():
    print("\n=== collections.deque ===")
    dq = deque()
    dq.append(1)
    dq.append(2)
    dq.append(3)
    print("Очередь:", list(dq))
    print("popleft() ->", dq.popleft())
    print("Первый элемент dq[0]:", dq[0])
    print("Пустая?", len(dq) == 0)
    print("Размер:", len(dq))


def demo_queue_module():
    print("\n=== queue.Queue (потокобезопасная) ===")
    q = queue.Queue()
    for item in ["a", "b", "c"]:
        q.put(item)
    print("Размер qsize():", q.qsize())
    # Для просмотра снимаем значения буфера под блокировкой.
    with q.mutex:
        contains_b = "b" in q.queue
    print("Есть ли 'b'?", contains_b)
    print("get() ->", q.get())
    q.task_done()
    with q.mutex:
        remaining_items = list(q.queue)
    print("Перебор:", remaining_items)
    for _ in remaining_items:
        q.get_nowait()
        q.task_done()
    print("После очистки пустая?", q.empty())


def simulate_cashier():
    """Пример использования: очередь покупателей в кассу."""
    print("\n=== Пример: очередь в кассу ===")
    line = MyQueue()
    for name in ["Анна", "Борис", "Вера"]:
        line.put(name)
        print(f"{name} встал(а) в очередь. Очередь: {line}")
    while not line.empty():
        print(f"Обслужен(а): {line.get()}. Осталось: {line.size()}")


def main():
    print('Лабораторная работа № 12 «Очередь»')
    input("Нажмите Enter, чтобы запустить пример: ")
    demo_my_queue()
    demo_deque()
    demo_queue_module()
    simulate_cashier()


if __name__ == "__main__":
    main()
