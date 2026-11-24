# Лабораторная 4, задача 4
# Рекурсивно проверить, является ли строка палиндромом.
# Идея: строка — палиндром, если первый и последний символы равны
# и середина (без них) тоже палиндром. Пустая строка и строка из 1 символа — палиндромы.

def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])


text = input("Введите строку: ")
cleaned = ""
for character in text:
    if character.isalnum():
        cleaned += character.lower()

if is_palindrome(cleaned):
    print("Это палиндром")
else:
    print("Это не палиндром")
