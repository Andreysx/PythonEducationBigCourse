import logging
import os
#
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger("my_logger")
# # logger.setLevel(logging)
# print()
# logging.basicConfig()

#
# import logging
#
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
#
# formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')
#
# file_handler = logging.FileHandler('operations.log', encoding='utf-8')
# file_handler.setFormatter(formatter)
#
# stream_handler = logging.StreamHandler()
# stream_handler.setFormatter(formatter)
#
# logger.addHandler(file_handler)
# logger.addHandler(stream_handler)
#
#
# def division():
#     logger.info("Начало выполнения деления!")
#     try:
#         dividend = float(input("Введите делимое: "))
#         divisor = float(input("Введите делитель: "))
#         result = dividend / divisor
#     except ValueError:
#         logger.exception("Введены не числовые значения")
#     except ZeroDivisionError:
#         logger.exception("Деление на ноль")
#     else:
#         logger.info(f"Получен результат {result} в процессе деления {dividend} на {divisor}")
#         return result
#
#
# res = division()
# print(res)

# logging.info()

s = set().discard()