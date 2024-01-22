# Задание №1
# Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.

def random_num(arg1, arg2 ):
    def inner():
        for i in range(arg2):
            temp = int(input("Введите ваш вариант: "))
            if temp == arg1:
                print("Вы победили: ")
                print("Попытка #", i+1)
        return f"Попытки закончились"
    return inner



num1 = int(input("Введите от 1 до 100: "))
num2 = int(input("Введите кол-во попыток от 1 до 10: "))

result = random_num(num1, num2)
result()

# OR
def secret_num(secur_num, attempts):
    def guess():
        nonlocal attempts
        while attempts > 0:
            user_num = int(input('Угадайте число от 1 до 100: '))
            if secur_num != user_num:
                attempts -= 1
                print(f'Вы не угадали, осталось попыток: {attempts}')
            else:
                print('Вы угадали')
            break
    return guess

if __name__ == '__main__':
    new_func = secret_num(10, 5)
    new_func()
