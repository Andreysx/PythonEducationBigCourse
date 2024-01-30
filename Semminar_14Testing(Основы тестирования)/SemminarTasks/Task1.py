# Задание №1
# Создайте функцию, которая удаляет из текста все символы
# кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.

import string
# string.ascii_letters - Все символы латинского алфавита
# def task1():
#     return "".join(c for c in text if c in ascii_letters or c == " ").lower() - однострочник

def clear_text(text):
    result = ''
    chars = string.ascii_letters + ' '
    for c in text:
        if c in chars:
            result += c
    return result.lower()


if __name__ == '__main__':
    print(clear_text('ASDфыв23434 dfsg PPP 45892'))
