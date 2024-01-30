# Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
# ● возврат строки без изменений
# ● возврат строки с преобразованием регистра без потери символов
# ● возврат строки с удалением знаков пунктуации
# ● возврат строки с удалением букв других алфавитов
# ● возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
#
# from string import ascii_letters
# import doctest
#
#
# def task1(text: str):
#     """
#     Delete every character except space and latin alphabet and returns lowercase result.
#
#     >>> task1("abc")
#     'abc'
#     >>> task1("ABCabc")
#     'abcabc'
#     >>> task1("hello, world!")
#     'hello world'
#     >>> task1("hello Илья")
#     'hello '
#     >>> task1("Hello, Илья!")
#     'hello '
#     """
#     return "".join(c for c in text if c in ascii_letters or c == " ").lower()
#
#
# if __name__ == '__main__':
#     doctest.testmod(verbose=True)