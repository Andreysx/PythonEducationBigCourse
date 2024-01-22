 # Задача 5 Объедините функции из прошлых задач.
# Функцию угадайку задекорируйте декораторами для сохранения параметров,
# декоратором контроля значений и декоратором для многократного запуска.
# Выберите верный порядок декораторов.


from random import randint


def d2(num):
    def dec(func):
        def wrapper(*args, **kwargs):
            counter = num
            for _ in range(counter):
                result = func(*args, **kwargs)
            return result

            wrapper.__name__ = func.__name__
            wrapper.__doc__ = func.__doc__
        return wrapper

    return dec


def d1(func):
    def inner(guess, amount_of_tries, *args, **kwargs):
        if guess < 1 or guess > 100:
            guess = randint(1, 100)
        if amount_of_tries < 1 or amount_of_tries > 10:
            amount_of_tries = randint(1, 10)
        return func(guess, amount_of_tries)

    return inner


@d2(5)
@d1
def task6(num1, num2):
    print(f"У вас {num2} попыток, чтобы отгадать число в пределах (1, 100)")
    for i in range(1, num2 + 1):
        print(f"Попытка №{i}")
        temp = int(input("Введите ваш вариант: "))
        if temp == num1:
            return f"Вы победили. Попытка #{i}"

    return f"Загаданое число = {num1}"


if __name__ == '__main__':
    print(task6(2, 5))