# Лабораторная 3, задача 9
# Начальный вклад 1000 руб. Каждый месяц вклад растёт на P процентов (0 < P < 25).
# Определить, через сколько месяцев K вклад превысит 1100 руб., и итоговую сумму S.

from decimal import Decimal, localcontext

P = Decimal(input("Процент P (0 < P < 25): "))

if not P.is_finite() or not 0 < P < 25:
    print("Процент должен удовлетворять условию 0 < P < 25")
else:
    with localcontext() as context:
        # Учитываем значащие цифры P, чтобы при малой ставке множитель отличался от 1.
        context.prec = max(28, len(P.as_tuple().digits) - min(P.adjusted(), 0) + 24)
        factor = 1 + P / 100
        initial_balance = Decimal(1000)
        target_balance = Decimal(1100)
        S = initial_balance
        K = 0

        if P < Decimal("0.01"):
            # Ищем первый целый месяц после достижения порога по формуле сложных процентов.
            threshold_month = (target_balance / initial_balance).ln() / factor.ln()
            K = int(threshold_month) + 1
            S = initial_balance * factor ** K
            while S <= target_balance:
                K += 1
                S *= factor
            while K > 1 and S / factor > target_balance:
                K -= 1
                S /= factor
        else:
            while S <= target_balance:
                S *= factor
                K += 1

        print(f"K = {K} мес., S = {S:.2f} руб.")
