#
# Задача 4Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой функции.

from functools import wraps


def decorator(num):
    def dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            counter = num
            while counter != 0:
                result = func(*args, **kwargs)
                counter -= 1
            return result
        return wrapper
    return dec

@decorator(5)
def print_sum(a, b):
    print(a + b)

if __name__ == '__main__':
    print_sum(1, 2)