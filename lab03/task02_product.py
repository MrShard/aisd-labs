# Лабораторная 3, задача 2
# Дано целое N (> 0). Найти произведение 1.1 * 1.2 * 1.3 * ... (N сомножителей).

N = int(input("N = "))

product = 1.0
factor = 1.1
for i in range(N):
    product *= factor
    factor += 0.1

print(f"Произведение = {round(product, 6)}")
