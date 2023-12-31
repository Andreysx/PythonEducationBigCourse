# . Создание функции генератора
# Рассмотрим создание генератора не в одну строку, а как отдельную функцию.
# Например нам надо посчитать факториал чисел от одного до n.
# Прежде чем создавать генератор, создадим обычную функцию, которая вернёт
# список чисел.
#
# def factorial(n):
#     number = 1
#     result = []
#     for i in range(1, n + 1):
#         number *= i
#         result.append(number)
#     return result
#
# for i, num in enumerate(factorial(10), start=1):
# print(f'{i}! = {num}')
#
# Внутри функции создали переменную для хранения очередного числа и
# результирующий список. Далее в цикле перебираем числа от одного до n
# включительно. Число number умножается на очередное число, вычисляется
# следующий по порядку факториал. Результат помещается в список. По завершении
# цикла возвращаем список ответов.
# Получив нужное количество значений в цикле выводим факториалы и их значения.
# Код отлично работает, но есть но. Мы не используем все факториалы сразу, а
# последовательно выводим их на печать. Если бы у нас был однострочный listcomp,
# достаточно было бы поменять квадратные скобки на круглы и получить
# генераторное выражение. В нашем примере также заменим функцию на генератор.
#
# Команда yield
# Как вы помните команда return возвращает готовый результат работы функции и
# завершает её работу. Зарезервированное слово yield превращает функцию в
# генератор. Значение после yield возвращается из функции. Сама функция
# запоминает своё состояние: строку, на которой остановилось выполнение, значения
# локальных переменных. Повторный вызов функции продолжает работу с момента
# остановки.
# Изменим функцию для получения факториала чисел, превратив её в генератор.
# def factorial(n):
#     number = 1
#     for i in range(1, n + 1):
#         number *= i
#     yield number
#
# for i, num in enumerate(factorial(10), start=1):
#     print(f'{i}! = {num}')
#
# Теперь внутри функции не создаётся пустой список для результатов. В цикле
# вычисляется факториал очередного числа. Далее команда yield возвращает
# значение. Следующий вызов вернёт функцию к циклу for для вычисления
# очередного числа.
# Как вы помните, если в функции отсутствует команда return Python в конце тела
# функции добавляет return None. Явная или неявная, как в нашем примере, команда
# return завершает работу генератора вызовом исключения StopIteration.
# Функции iter и next для генераторов
# Уже знакомые по сегодняшнему уроку функции iter и next могут работать с
# созданными генераторами. Например так:
# my_iter = iter(factorial(4))
# print(my_iter)
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter)) # StopIteration
# Задание
# Перед вами несколько строк кода. Напишите что по вашему мнению выведет print,
# не запуская код. У вас 3 минуты.
# def gen(a: int, b: int) -> str:
# if a > b:
# a, b = b, a
# for i in range(a, b + 1):
# yield str(i)
# for item in gen(10, 1):
# print(f'{item = }')
