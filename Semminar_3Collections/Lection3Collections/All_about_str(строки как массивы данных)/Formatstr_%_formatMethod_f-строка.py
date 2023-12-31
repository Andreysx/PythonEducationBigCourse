# Форматирование строк
# Опытные программисты могут назвать 5-7 способов форматирования строк.
# Разбирать их все нет смысла. Рассмотрим три “главных” на примерах.
# 20
# Форматирование через %
# Форматирование с использованием символа % является старым способом указания
# формата. Его вы можете встретить в коде, который писали очень давно. В
# настоящее время он используется лишь в некоторых модулях для задания формата
# вывода данных.
# name = 'Alex'
# age = 12
# text = 'Меня зовут %s и мне %d лет' % (name, age)
# print(text)
# В строке текста используется знак % с символом типа после него. s — строка, d —
# число и т.п. После строки указывается символ % и перечисляются переменные. Если
# переменных больше одной, они заключаются в круглые скобки и разделяются
# запятой — передаётся кортеж.
# 🔥 Важно! Подробнее про используемы литеры вы можете прочитать по
# ссылке в материалах лекции. Пока же договоримся не использовать данный
# стиль форматирования, если это не обязывает конкретный модуль.
# Метод format
# Метод формат является строковым методом и позволяет соединять заранее
# заготовленный текст с переменными. Долгое время был основным способом
# форматирования. До версии Python 3.6, если быть точным.
# name = 'Alex'
# age = 12
# text = 'Меня зовут {} и мне {} лет'.format(name, age)
# print(text)
# В строке используются фигурные скобки как место для подстановки значений.
# Далее для строки вызывается метод format. В качестве аргументов метод получает
# нужное количество переменных.
# 21
# f-строка
# Начиная с Python 3.7 для форматирования текста используют f-строки. Они
# работают быстрее, чем старые способы форматирования. А некоторые
# разработчики языка предлагают сделать их строками по умолчанию в одном из
# будущих релизов.
# f-строки похожи на более короткую и читаемую запись метода формат.
# name = 'Alex'
# age = 12
# text = f'Меня зовут {name} и мне {age} лет'
# print(text)
# Перед открывающей кавычкой пишут f — указатель на отформатированную строку.
# Текст внутри фигурных скобок воспринимается как переменная и на печать
# выводятся из значения.
# 🔥 Важно! Для печати фигурных скобок используется две фигурные скобки
# слитно.
# print(f'{{Фигурные скобки}} и {{name}}')
# Помимо вывода содержимого переменной можно указать дополнительные
# символы, влияющие на представление.
# Уточнение формата
# Существую различные способы уточнения способа вывода значения переменной.
# pi = 3.1415
# print(f'Число Пи с точностью два знака: {pi:.2f}')
# data = [3254, 4364314532, 43465474, 2342, 462256, 1747]
# for item in data:
# print(f'{item:>10}')
# 22
# num = 2 * pi * data[1]
# print(f'{num = :_}')
# После указания имени переменной в фигурных скобках ставится двоеточие —
# указатель на символы задания формата далее.
# ● :.2f — число пи выводим с точность два знака после запятой
# ● :>10 — элементы списка выводятся с выравниванием по правому краю и
# общей шириной вывода в 10 символов
# ● = — выводим имя переменной, знак равенства с пробелами до и после него и
# только потом значение.
# ● :_ — число разделяется символом подчёркивания для деления на блоки по 3
# цифры.
# Про эти и другие способы форматирования можно почитать в официальной
# документации. Ссылка в материалах.
