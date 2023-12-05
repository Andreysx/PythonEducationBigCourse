import decimal

# Напишите программу банкомат.
# ● Начальная сумма равна нулю
# ● Допустимые действия: пополнить, снять, выйти
# ● Сумма пополнения и снятия кратны 50 у.е.
# ● Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ● После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ● Нельзя снять больше, чем на счёте
# ● При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# ● Любое действие выводит сумму денег


def tax():
    global money_in_atm
    if money_in_atm > 5_000_000:
        money_in_atm *= decimal.Decimal(0.9)
        print("Налог 10% при сумме более 5_000_000 у.е.")


def is_multiple_of_50(value):
    return value % 50 == 0


def count_increase():
    global count_operation
    count_operation += 1
    if not count_operation % 3:
        global money_in_atm
        money_in_atm *= decimal.Decimal(1.03)
        print("Начисление 3%")


def put_money(value):
    tax()
    global money_in_atm
    if is_multiple_of_50(value):
        money_in_atm += value
        count_increase()
        return f"Счет пополнен на {value} у.е."
    else:
        return "Можно пополнять на сумму кратную 50"


def take_money(value):
    tax()
    TAXFORTAKEMONEY = 1.5
    global money_in_atm
    if is_multiple_of_50(value):
        if money_in_atm > value:
                comisia = decimal.Decimal(value * 0.015)
                if comisia < 30:
                    comisia = 30
                else:
                    comisia = 600
# t = value / 100 * TAXFORTAKEMONEY
                    money_in_atm -= decimal.Decimal(value + comisia)
                    count_increase()
                    return f"Вы сняли {value} у.е. Налог на снятие {comisia:.2f}"

# return "Вы можете снять в пределах 30..600"
        else:
            return "На Вашем счету не достаточно средств"
    else:
        return "Можно снять сумму кратную 50"


def task6():

    while True:
        print(f"На Вашем счету {money_in_atm:.2f} у.е.")
        print("Введите от 1 до 3")
        print("1 - Пополнить счет")
        print("2 - Снять со счета")
        print("3 - Выйти")
        choice = input()
        match choice:
            case "1":
                print(put_money(int(input("Введите сумму на которую вы хотите пополнить счет: "))))
            case "2":
                print(take_money(int(input("Введите сумму снятия: "))))
            case "3":
                break
            case _:
                print("Введено не верное значение")

task6()