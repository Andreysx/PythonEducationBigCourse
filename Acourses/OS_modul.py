# import os.path
#
# print(os.path.join('home', 'user', 'egoroff'))
# paths = ('one', 'two', 'three')
# print(os.path.join(*paths))

# print(__file__)
# Эту информацию легко получить, зная о существовании служебного атрибута __file__  — это специальная переменная, которая содержит путь к скрипту, который был запущен.
# Значение, которое хранится в переменной __file__, будет зависеть от версии интерпретатора, который вы используете.
# Если у вас версия python от 3.9, в __file__ будет храниться абсолютное значение пути, в более старых версиях - относительный путь. Более подробно можно прочитать


# import os
#
#
# def get_only_dirs(path):
#     # Получаем список всех элементов в указанной директории
#     items = os.listdir(path)
#
#     # Фильтруем только папки (исключаем файлы)
#     dirs = [item for item in items if os.path.isdir(os.path.join(path, item))]
#
#     # Сортируем папки в алфавитном порядке
#     dirs.sort()
#
#     # Выводим каждую папку на отдельной строке
#     for dir_name in dirs:
#         print(dir_name)
#
#     # Выводим количество папок
#     print(len(dirs))
#
# # Пример использования:
# # get_only_dirs('./www/user/hobbit')


# import os
# import time
#
# print('File         :', __file__)
# print('Access time  :', time.ctime(os.path.getatime(__file__)))
# print('Modified time:', time.ctime(os.path.getmtime(__file__)))
# print('Change time  :', time.ctime(os.path.getctime(__file__)))
# print('возвращает размер файла в байтах', os.path.getsize(__file__))


# import os
# import stat
#
# def get_permissions(path: str) -> str:
#     mode = os.stat(path).st_mode
#     return stat.filemode(mode)[1:]


# d={0:"---", #   Все запрещено
#    1:"--x", # 	Только выполнение
#    2:"-w-", # 	Только запись
#    3:"-wx", #   Запись и выполнение
#    4:"r--", #   Только чтение
#    5:"r-x", #   Чтение и выполнение
#    6:"rw-", #   Чтение и запись
#    7:"rwx"  # 	Чтение и запись и выполнение
#   }


# print(int('733', 8))
import os
# os.makedirs('data/value/site')


# import os
# import calendar
#
# #
# # for i in range(1,11):
# #     # print(i)
# #     os.mkdir('report'+str(i))
# m = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
#      'December']
#
# for i in range(2018, 2026):
#     os.mkdir('sales_' + str(i))
#     os.chdir('sales_' + str(i))
#     for j in range(len(sorted(m))):
#         os.mkdir(m[j] + '_' + str(i)[2:])
#     os.chdir('../')
