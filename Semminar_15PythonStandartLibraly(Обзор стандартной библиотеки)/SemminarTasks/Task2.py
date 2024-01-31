# На семинаре про декораторы был создан логирующих декоратор.
# Он сохранял аргументы функции и результат её работы в файл.
# Напишите аналогичный декоратор, но внутри используйте модуль logging.

from functools import wraps
import logging

# logging.basicConfig(level='DEBUG')
logger = logging.getLogger(__name__)

handler_error = logging.FileHandler("error.log", encoding="UTF-8")
handler_error.setLevel(logging.ERROR)
logger.addHandler(handler_error)


def logging_decorator(func):
     @wraps(func)
     def wrap(*args, **kwargs):
         try:
             result = func(*args, **kwargs)
         except Exception as e:
             logger.critical(e)
             raise e
         return result
     return wrap


@logging_decorator
def div(a, b):
    return a / b


if __name__ == '__main__':
    try:
        print(div(5, 0))
    except ZeroDivisionError as e:
        print(e)