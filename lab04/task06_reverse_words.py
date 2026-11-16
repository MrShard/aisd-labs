# Лабораторная 4, задача 6
# Рекурсивно поменять порядок слов в строке на обратный.
# Идея: reverse(["a", "b", "c"]) = reverse(["b", "c"]) + ["a"]

def reverse_words(words):
    if len(words) <= 1:
        return words
    return reverse_words(words[1:]) + [words[0]]


text = input("Введите строку: ")
words = text.split()
print(" ".join(reverse_words(words)))
