# Доработаем задачу 2. Сохраняйте в лог файл раздельно:
# уровень логирования, дату события, имя функции (не декоратора), аргументы вызова, результат.

import logging
from logging.handlers import RotatingFileHandler
from functools import wraps
from filter import InfoFilter

# https://docs.python.org/3/library/logging.html?ref=pylenin.com#logrecord-attributes

ERROR_LOG_FILE_NAME = "log/errors.log"
INFO_LOG_FILE_NAME = "log/info.log"
FORMAT = "%(levelname)s: %(asctime)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT)
logger = logging.getLogger(__name__)

error_file_handler = RotatingFileHandler(ERROR_LOG_FILE_NAME, encoding="UTF-8", maxBytes=10000, backupCount=3)
error_file_handler.setFormatter(logging.Formatter(FORMAT))
error_file_handler.setLevel(logging.WARNING)
logger.addHandler(error_file_handler)

info_file_handler = RotatingFileHandler(INFO_LOG_FILE_NAME, encoding="UTF-8", maxBytes=10000, backupCount=3)
info_file_handler.setFormatter(logging.Formatter(FORMAT))
info_file_handler.addFilter(InfoFilter(logging.INFO))
logger.addHandler(info_file_handler)


def logging_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            logger.critical(f"Результатом выполнения функции {func.__name__} с атрибутами {args} было {e}")
            raise e
        else:
            logger.info(f"Результатом выполнения функции {func.__name__} с атрибутами {args} было {result}")
        return result

    return wrapper


@logging_decorator
def div(a, b):
    return a / b

# from logging import Filter

#
# class InfoFilter(Filter):
#     def __init__(self, level):
#         super().__init__()
#         self.__level = level
#
#     def filter(self, log_record):
#         return log_record.levelno == self.__level

