# Лабораторная 3, задача 1
# Дана цена 1 кг конфет. Вывести стоимость 0.1, 0.2, ..., 1 кг конфет.

price = float(input("Цена 1 кг конфет: "))

for i in range(1, 11):
    weight = i / 10   # 0.1, 0.2, ..., 1.0
    cost = weight * price
    print(f"{weight:.1f} кг — {cost:.2f}")
