# Запись и добавление в файл
# С режимами записи мы уже познакомились.
# ➢ w — создаём новый пустой файл для записи. Если файл существует,
# открываем его для записи и удаляем данные, которые в нём хранились.
# ➢ x — создаём новый пустой файл для записи. Если файл существует, вызываем
# ошибку.
# ➢ a — открываем существующий файл для записи в конец, добавления данных.
# Если файл не существует, создаём новый файл и записываем в него.
#
# ● Запись методом write
# Метод write принимает на вход строку или набор байт в зависимости от того как вы
# открыли файл. После записи метод возвращает количество записанной
# информации.
#
# text = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.'
# with open('new_data.txt', 'a', encoding='utf-8') as f:
#     res = f.write(text)
#     print(f'{res = }\n{len(text) = }')
#
# Метод не добавляет символ перехода на новую строку. Если произвести несколько
# записей, они “склеиваются” в файле.
#
# text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
# 'Consequatur debitis explicabo laboriosam sint suscipit  temporibus veniam?',
# 'Accusantium alias amet fugit iste neque non odit quiasaepe totam velit?', ]
# with open('new_data.txt', 'a', encoding='utf-8') as f:
#     for line in text:
#         res = f.write(line)
#         print(f'{res = }\n{len(line) = }')
#
# Если каждая строка должна сохранятся в файле с новой строки, необходимо
# самостоятельно добавить символ переноса - \n
#
# text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
# 'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
# 'Accusantium alias amet fugit iste neque non odit quiasaepe totam velit?', ]
# with open('new_data.txt', 'a', encoding='utf-8') as f:
#     for line in text:
#         res = f.write(f'{line}\n')
#         print(f'{res = }\n{len(line) = }')
#
#
# ● Запись методом writelines
# Метод writelines принимает в качестве аргумента последовательность и записывает
# каждый элемент в файл. Элементы последовательности должны быть строками или
# байтами в зависимости от режима записи.
# В отличии от write этот метод ничего не возвращает.
#
# text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
# 'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
# 'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]
# with open('new_data.txt', 'a', encoding='utf-8') as f:
#     f.writelines('\n'.join(text))
#
# Для того чтобы каждый элемент списка text сохранялся в файле с новой строки
# воспользовались строковым методом join. writelines не добавляет переноса между
# элементами последовательности.
#
#
# ● print в файл
# Функция print по умолчанию выводит информацию в поток вывода. Обычно это
# консоль. Но можно явно передать файловый объект для печати в файл. Для этого
# надо воспользоваться ключевым параметром file.
#
# text = ['Lorem ipsum dolor sit amet, consectetur adipisicingelit.',
# 'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
# 'Accusantium alias amet fugit iste neque non odit quiasaepe totam velit?', ]
# with open('new_data.txt', 'a', encoding='utf-8') as f:
#     for line in text:
#         print(line, file=f)
#
# В отличии от методов записи в файл, функция print добавляет перенос строки.
# Кроме того ничто не мешает явно изменить параметр end функции.
#
# text = ['Lorem ipsum dolor sit amet, consectetur adipisicingelit.',
# 'Consequatur debitis explicabo laboriosam sint suscipittemporibus veniam?',
# 'Accusantium alias amet fugit iste neque non odit quiasaepe totam velit?', ]
# with open('new_data.txt', 'a', encoding='utf-8') as f:
#     for line in text:
#         print(line, end='***\n##', file=f)
