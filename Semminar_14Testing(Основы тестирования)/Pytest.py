# 3. Основы тестирования с pytest
# Финальный модуль для создания тестов — pytest. Он не входит в стандартную
# библиотеку Python, поэтому должен быть установлен перед использованием.
# pip install pytest
# 🔥 Важно! Версия Python должна быть 3.7 или выше.
# Команда assert
# В Python есть зарезервированное слово assert. После работы с unittest вы
# догадываетесь о её назначении. assert делает утверждение. Если оно возвращает
# истину, программа продолжает работать. А если утверждение ложно, поднимается
# ошибка AssertionError.
# Для простоты можно представить assert как особую конструкцию if.
# ● “асерт”
# assert утверждение, "Утверждение не подтвердилось"
# ● “иф”
#
# if утверждение:
#     pass
# else:
#     raise AssertionError("Утверждение не подтвердилось")
# Модуль pytest формирует свою работу вокруг встроенной команды assert. Но в
# отличии от примера с if даёт подробную информацию об ошибках, если тесты не
# проходят.
#
#
# Общие моменты работы с pytest
# Рассмотрим простой пример тестирования работы функции, которая складывает
# два числа.
# import pytest
#
# def sum_two_num(a, b):
#     return a + b
# # return f'{a}{b}'
# def test_sum():
#     assert sum_two_num(2, 3) == 5, 'Математика покинула чат'
#
# if __name__ == '__main__':
#     pytest.main()
# Импорт модуля нужен только для запуска тестов из файла. Для создания
# простейших тестов модуль pytest не нужен.
# Функция sum_two_num наш подопытный. Она принимает пару числе и возвращает
# их сумму.
# Для создания кейса просто определяем функцию, которая начинается со слова test.
# Внутри используем assert для проверки утверждения. В простейшем случае это
# сравнение вызова функции с ожидаемым результатом. Более сложные ассерты
# рассмотрим далее. Дополнительно можно указать сообщение, которое будет
# выведено в случае провала теста.
# Количество функций в файле может быть любым. pytest найдёт и запустит их все на
# основе сопоставления имён. При этом превращать функции в методы класса как в
# unittest не нужно. А если очень хочется объединить кейсы внутри класса, создайте
# класс начинающийся с Test.
# Чтобы запустить тест из файла, вызываем функцию main из модуля pytest.
# 🔥 Внимание! Команда для запуска тестов из командной строки выглядит
# аналогично запуску doctest и unittest. Ключ с одиночным или двойным v
# указывает на уровень детализации. Кроме того можно вызывать pytest
# напрямую.
# $ python3 -m pytest tests.py -vv
# $ pytest tests_pt.py
# 23
# Сравнение тестов pytest с doctest и unittest
# Ещё раз возьмём функцию проверки числа на простоту и реализуем написанные
# ранее тесты используя pytest.
# Файл prime.py не изменился
#
# def is_prime(p: int) -> bool:
#     if not isinstance(p, int):
#         raise TypeError('The number P must be an integer type')
#     elif p < 2:
#         raise ValueError('The number P must be greater than one')
#     elif p > 100_000_000:
#         print('If the number P is prime, the check may take a long time. Working...')
#     for i in range(2, p):
#         if p % i == 0:
#             return False
#         return True
#
# Файл test_prime_pt.py с кейсами pytest
#
# import pytest
# from prime import is_prime
#
#
# def test_is_prime():
#     assert not is_prime(42), '42 - составное число'
#     assert is_prime(73), '73 - простое число'
# def test_type():
#     with pytest.raises(TypeError):
#         is_prime(3.14)
# def test_value():
#     with pytest.raises(ValueError):
#         is_prime(-100)
# def test_value_with_text():
#     with pytest.raises(ValueError, match=r'The number P must be greater than 1'):
#         is_prime(1)
# def test_warning_false(capfd):
#     is_prime(100_000_001)
#     captured = capfd.readouterr()
#     assert captured.out == 'If the number P is prime, the check may take a long time. Working...\n'
# def test_warning_true(capfd):
#     is_prime(100_000_007)
#     captured = capfd.readouterr()
#     assert captured.out == 'If the number P is prime, the check may take a long time. Working...\n'
#
# if __name__ == '__main__':
# pytest.main(['-v'])
#
# Начало с импортом и конец с запуском тестов стандартные для Python. Разберём
# каждый из кейсов.
#
# ➢ Кейс test_is_prime
# Проверяем базовую работу функции. Утверждение assert not ожидает получить
# ложь в качестве результата вызова функции. Второй assert ожидает получить
# истину.
# 🔥 Важно! Если первая строка провалит тест, второй assert не будет вызван
# для проверки. Обычно внутри кейса пишут одно утверждения. В нашем случае
# можно разделить проверки на два отдельных кейса.
# ➢ Кейс test_type
# Используем менеджер контекста pytest.raises который ожидает получить ошибку
# TypeError при вызове is_prime с вещественным число в качестве аргумента.
# Наличие ошибки проходит тест, а её отсутствие - роняет. Строка, которая должна
# поднять ошибку - последняя строка внутри менеджера контекста. Дальнейший код
# не будет выполняться.
# ➢ Кейс test_value
# Тест работает аналогично проверки типа, но мы указали другую ошибку в
# менеджере и передали другое значение в функцию.
# ➢ Кейс test_value_with_text
# Более сложный подход к тестированию. Помимо ошибки в параметр match
# передаётся регулярное выражение. Если оно совпадёт с текстом ошибки, тест будет
# пройден.
# ➢ Кейсы test_warning_false и test_warning_true
# Внимание! Оба примера выходят за рамки основ pytest. Это скорее пример на
# будущее для самых любознательных.
# Кейс получает фикстуру capfd в качестве аргумента. capfd (capture file descriptors)
# является одной из встроенных в pytest фикстур, которая позволяет перехватывать
# потоки вывода и ошибок. Внутри кейса вызываем тестируемую функцию. Далее
# используем метод readouterr() для получение потоков в переменную captured. В
# финале сравниваем результат captured.out (потока вывода) с ожидаемым текстом
# сообщения.
# Запуск тестов doctest и unittest
# Для запуска тестов, написанных другими инструментами можно воспользоваться
# следующими командами в консоли ОС:
# $ pytest --doctest-modules prime.py -v
# $ pytest tests_ut.py
# В случае с doctest необходимо указать флаг --doctest-modules. Для unittest ничего
# указывать не надо. Практически все кейс из unittest можно запускать в pytest.
# Модуль понимает синтаксис, способен собрать тесты из классов и проверить их.
#
#
#
#
# Фикстуры pytest как замены unittest setUp и
# tearDown
# Если вам необходимо выполнить однотипные действия для подготовки нескольких
# тестов, можно создать собственные фикстуры. Рассмотрим простой пример из
# главы о unittest.
# import pytest
#
# @pytest.fixture
# def data():
#     return [2, 3, 5, 7]
#
# def test_append(data):
#     data.append(11)
#     assert data == [2, 3, 5, 7, 11]
#
# def test_remove(data):
#     data.remove(5)
#     assert data == [2, 3, 7]
#
# def test_pop(data):
#     data.pop()
#     assert data == [2, 3, 5]
#
#
# if __name__ == '__main__':
# pytest.main(['-v'])
# Функция data превращается в фикстуру добавлением декоратора @pytest.fixture.
# Чтобы использовать фикстуру внутри кейса, необходимо передать её в качестве
# аргумента. Выбранный разработчика pythest подход к фикстурам удобен тем, что
# позволяет любые вариации с кейсами.
# ● можно иметь множество фикстур и разные кейсы могут использовать разные
# фикстуры.
# ● в кейс можно передать любое количество фикстур.
# ● фикстура может принимать в качестве аргумента другую фикстуру.
#
#
# Ещё немного о фикстурах
# Рассмотрим пример посложнее.
# import pytest
#
# @pytest.fixture
# def get_file(tmp_path):
#     f_name = tmp_path / 'test_file.txt'
#     print(f'Создаю файл {f_name}') # принтим в учебных целях
#     with open(f_name, 'w+', encoding='utf-8') as f:
#         yield f
#     print(f'Закрываю файл {f_name}') # принтим в учебных целях
#
# @pytest.fixture
# def set_num(get_file):
#     print(f'Заполняю файл {get_file.name} цифрами') # принтим в учебных целях
#     for i in range(10):
#         get_file.write(f'{i:05}')
#     get_file.seek(0)
#
# @pytest.fixture
# def set_char(get_file):
#     print(f'Заполняю файл {get_file.name} буквами') # принтим в учебных целях
#     for i in range(65, 91):
#         get_file.write(f'{chr(i)}')
#     get_file.seek(0)
#     return get_file
#
# def test_first_num(get_file, set_num):
#     first = get_file.read(5)
#     assert first == '00000'
#
# def test_first_char(set_char):
#     first = set_char.read(5)
#     assert first == 'ABCD' # специально провалим тест
#
# if __name__ == '__main__':
#      pytest.main(['-v'])
#
# Кейсов всего два: test_first_num и test_first_chr. И каждый из них использует свои
# фикстуры. Но давайте обо всём сверху вниз.
# ➢ Фикстура get_file
# Фикстура принимает на вход аргумент tmp_path. Это встроенная фикстура, которая
# возвращает временный путь - объект pathlib.Path. При использовании выводим не
# печать информацию о создании файла и о его удалении. Отследим когда
# срабатывает фикстура.
# Внутри менеджера контекста создаём файл и через команду yield возвращаем
# указатель на него. Если бы мы использовали команду return, менеджер контекста
# вызвал бы f.close() после возврата указания и файл стал бы нечитаемым.
# Используя yield мы превратили функцию в генератор. Теперь внутри фикстуры есть
# “сетап” создающий файл и “тирдаун”, закрывающий его после использования.
# Внимание! Мы явно не удаляем временные файлы. Фикстура tmp_path сохраняет
# три последних временных каталога, удаляя старые при очередном запуске.
# ➢ Фикстура set_num
# Используя файловый дескриптор get_file записываем строку из цифр и возвращаем
# указатель на начало файла. Фикстура ничего не возвращает.
# ➢ Фикстура set_char
# Снова используем файловый дескриптор get_file, но получаем уже другой файл. Имя
# совпадает, но каталоги разные. Заполняем его буквами, сбрасываем позицию в
# ноль и возвращаем get_file - файловый дескриптор.
# ➢ Кейс test_first_num
# Перед началом теста срабатывают фикстуры, создающие временный файл и
# заполняющие его цифрами. Далее обращаемся к get_file чтобы прочитать пять
# первых символов и сравниваем их со строкой текста.
# ➢ Кейс test_first_char
# Кейс получает всего одну фикстуру set_char. Но так как она самостоятельно
# вызывает фикстуру get_file и возвращает её, мы можем обращаться к файловому
# дескриптору по имени set_char.
# Рассмотренный пример даёт представление о гибкости кейсов pytest.
# Субъективное мнение автора курса, но pytest является лучшим из трёх
# рассмотренных инструментов тестирования. Попробуйте все три, составьте своё.
#
#
#
# Задание
# Перед вами несколько строк кода. Напишите что должна делать программа, чтобы
# пройти тесты. У вас 3 минуты.
# import pytest
# from main import func
#
#
# def test_1():
#     assert func(4) == 0
# def test_2():
#     assert func(4, -4) == (1, 0)
# def test_3():
#     assert func(4, -10, -50) == (5, -2.5)
# def test_4():
#     assert func(1, 1, 1) is None
#
# if __name__ == '__main__':
#     pytest.main(['-v'])
# Вывод
# На этой лекции мы:
# 1. Разобрались с написанием тестов в Python
# 2. Изучили возможности doctest
# 3. Узнали о пакете для тестирования unittest
# 4. Разобрались с тестированием через pytest
