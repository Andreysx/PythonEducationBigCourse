# Напишите программу, которая использует модуль logging для вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль.

import logging

logging.basicConfig(level='DEBUG')
logger = logging.getLogger(__name__)

handler_error = logging.FileHandler("error.log", encoding="UTF-8")
handler_error.setLevel(logging.ERROR)
logger.addHandler(handler_error)


def div(a, b):
    return a / b


if __name__ == '__main__':
    try:
        div(5, 0)
    except ZeroDivisionError as e:
        logger.critical(e)
        print(e)