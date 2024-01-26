# ✔ Функция принимает на вход три списка одинаковой длины:
#   имена str, ставка int, премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммойпремии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии.

def bonus_calc(names: str, bases: int, bonuses: str):
    res = {}
    for name, base, bonus in zip(names, bases, bonuses):
        res[name] = (base * float(bonus[:-1])/100)
    # for i in range(len(names)):
    #     res[names[i]] = (bases[i] * float(bonuses[i][:-1])/100)
    return res

print(bonus_calc(['ivan', 'maxim'], [3000, 4500], ['10.25%', '12.33%']))

# Другой вариант записи
def bonus_calc1(names: str, bases: int, bonuses: str):
    data = list(zip(names, bases, bonuses))
    return {item[0]: item[1] * float(item[2].replace('%', ''))/100 for item in data}

print(bonus_calc1(['ivan', 'maxim'], [3000, 4500], ['10.25', '12.33%']))