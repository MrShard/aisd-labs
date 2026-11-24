# Лабораторная 3, задача 9
# Начальный вклад 1000 руб. Каждый месяц вклад растёт на P процентов (0 < P < 25).
# Определить, через сколько месяцев K вклад превысит 1100 руб., и итоговую сумму S.

from decimal import Decimal, localcontext

P = Decimal(input("Процент P (0 < P < 25): "))

if not P.is_finite() or P <= 0 or P >= 25:
    print("Процент должен удовлетворять условию 0 < P < 25")
else:
    with localcontext() as context:
        digits = len(P.as_tuple().digits)
        places = -P.adjusted()
        if places < 0:
            places = 0
        context.prec = digits + places + 28

        factor = 1 + P / 100
        initial_balance = Decimal(1000)
        target = Decimal(1100)

        if P >= Decimal("0.01"):
            K = 0
            S = initial_balance
            while S <= target:
                S *= factor
                K += 1
        else:
            low = 0
            high = 1
            while initial_balance * factor ** high <= target:
                low = high
                high *= 2

            while high - low > 1:
                month = (low + high) // 2
                balance = initial_balance * factor ** month
                if balance > target:
                    high = month
                else:
                    low = month

            K = high
            S = initial_balance * factor ** K

        print(f"K = {K} мес., S = {S:.2f} руб.")
