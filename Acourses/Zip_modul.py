# from collections import Counter
#
#
# # print(len('a4b3c1') < len('aaaabbbc'))
#


# Сжатие строки
# def compress_string(s):
#     """
#     Сжимает строку, заменяя повторяющиеся символы на символ и количество повторений
#     """
#     if not s:
#         return s
#
#     # Приводим всю строку к нижнему регистру для регистронезависимости
#     s_lower = s.lower()
#
#     compressed = []
#     count = 1
#     current_char = s_lower[0]
#
#     # Проходим по строке, начиная со второго символа
#     for i in range(1, len(s_lower)):
#         if s_lower[i] == current_char:
#             count += 1
#         else:
#             # Добавляем предыдущий символ и его количество
#             compressed.append(current_char)
#             compressed.append(str(count))
#             # Начинаем считать новый символ
#             current_char = s_lower[i]
#             count = 1
#
#     # Добавляем последний символ
#     compressed.append(current_char)
#     compressed.append(str(count))
#
#     # Преобразуем список в строку
#     compressed_str = ''.join(compressed)
#
#     # Проверяем, стала ли строка короче
#     if len(compressed_str) < len(s):
#         return compressed_str
#     else:
#         return s
#
# # Сжатие строки
# def compress_string_v2(s):
#     if len(s) <= 1:
#         return s
#
#     s_lower = s.lower()
#     compressed = []
#     count = 1
#
#     for i in range(1, len(s_lower)):
#         if s_lower[i] == s_lower[i - 1]:
#             count += 1
#         else:
#             compressed.append(s_lower[i - 1] + str(count))
#             count = 1
#
#     # Добавляем последний символ тк мы накопили знаечение для последнего элемента в count, но вышли из цикла ты и не добабитв его
#     compressed.append(s_lower[-1] + str(count))
#
#     compressed_str = ''.join(compressed)
#
#     return compressed_str if len(compressed_str) < len(s) else s
# # Тестовые случаи с корректными входными данными
# print(compress_string("aaaAbbCaa"))
# assert compress_string("aaaabbbc") == "a4b3c1"
# assert compress_string("abbbbbd") == "a1b5d1"
# assert compress_string("wwwwwww") == "w7"
# assert compress_string("") == ""
#
# # Тестовые случаи с входными данными, которые не нуждаются в сжатии
# assert compress_string("abcd") == "abcd"
# assert compress_string("xyz") == "xyz"
# assert compress_string("aabbccddeeffgghh") == "aabbccddeeffgghh"
#
# # Тестовые случаи с регистронезависимостью
# assert compress_string("aaAAaa") == "a6"
# assert compress_string("aAaAA") == "a5"
# assert compress_string("AaBbCc") == "AaBbCc"
# assert compress_string("aaaAbbCaa") == "a4b2c1a2"
# assert compress_string("AAAABBBCC") == "a4b3c2"
#
# # Тестовые случаи с длинной строки
# assert compress_string("a" * 1000000) == "a1000000"
# assert compress_string("a" * 1000000 + 'b' * 500) == "a1000000b500"
# assert compress_string("abcdefghijk" + "w" * 10000) == "a1b1c1d1e1f1g1h1i1j1k1w10000"


# Декомпрессия строки


# def decompress_string(compressed: str) -> str:
#     if compressed.isalpha():
#         return compressed.lower()
#     else:
#         return ''.join([i[0] * int(i[1]) for i in [tuple(compressed[i:i + 2]) for i in range(0, len(compressed), 2)]])
#
#
# print(decompress_string("a4b3c1"))
# assert decompress_string("a4b3c1") == "aaaabbbc"
# assert decompress_string("a1b5d1") == "abbbbbd"
# assert decompress_string("w7") == "wwwwwww"
# assert decompress_string("") == ""
# assert decompress_string("aabbccddeeffgghh") == "aabbccddeeffgghh"
# assert decompress_string("abcd") == "abcd"
# assert decompress_string("xyz") == "xyz"
#
# assert decompress_string("a6") == "aaaaaa"
# assert decompress_string("a5") == "aaaaa"
#
# assert decompress_string("AaBbCc") == "aabbcc"
# assert decompress_string("a4b2c1a2") == "aaaabbcaa"
# assert decompress_string("a4b3c2") == "aaaabbbcc"
# assert decompress_string("a1000000") == "a" * 1000000
# assert decompress_string("a1000000b500") == "a" * 1000000 + 'b' * 500
# assert decompress_string("a1b1c1d1e1f1g1h1i1j1k1w10000") == "abcdefghijk" + "w" * 10000

# Вам доступны следующие файлы
# SecretAgentManual.txt
# ChocolateCake_Recipe.pdf
# PirateTreasureMap.jpg
# Данные файлы располагаются в той же папке, где и будет запускаться проверка на сайте stepik.
# Ваша задача — создать архив secrets.zip и добавить в него все эти файлы. Выводить ничего не нужно
# from zipfile import ZipFile
#
# with ZipFile("secrets.zip", mode="a") as archive:
#       archive.write("SecretAgentManual.txt")
#       archive.write("ChocolateCake_Recipe.pdf")
#       archive.write("PirateTreasureMap.jpg")
#


# Одноклассник попросил Валеру скинуть архивом XXX.zip файлы из списка files
# Но вот проблема, часть из них Валера удалил, и их теперь нет на компьютере.
# Одноклассник расстроился, конечно, и попросил отправить то, что есть. Валера решил написать программу, но сам не справился. Просит вас помочь.
# Там, говорит, делов-то на пять минут.
# Пройтись по всем файлам и добавить в архив XXX.zip только существующие на диске.
# Все файлы до удаления находились в одной папке с вашей будущей программой.
# Ваша задача — создать архив XXX.zip и добавить в него все эти файлы. Выводить ничего не нужно.
# from zipfile import ZipFile
# import os
#
#
# files = ["BananaPeel_Slippery.doc", "DiscoDancingUnicorn.mp3", "SneezingPanda.gif", "InvisibleCloak.exe",
#          "PizzaDelivery_Drone.txt", "LaserCat_Visualization.pdf", "AlienCookbook.txt",
#          "ZombieApocalypseSurvivalGuide.docx", "TalkingPotato.mp4", "DancingBroccoli.jpg"]
#
# with ZipFile('XXX.zip', 'a') as archive:
#     for file in files:
#         if os.path.exists(file):
#             archive.write(file)


# Создайте zip-архив numbers.zip. Он должен содержать 10 файлов. Имена файлов и их содержимое должны быть следующими:
#
# number_0.txt с содержимым This is number 0
# number_1.txt с содержимым This is number 1
# number_2.txt с содержимым This is number 2
# ....
# number_9.txt с содержимым This is number 9
# Ваша задача — создать только архив, выводить ничего не нужно.
#
# from zipfile import ZipFile
# import os
#
# # ZipFile - поддерживает протокол менеджера контекста
#
# with ZipFile('numbers.zip', mode='a') as archive:
#     for i in range(10):
#         path = 'number_' + str(i) + '.txt'
#         file = open(file=path, encoding='utf-8', mode='w')
#         file.write('This is number ' + str(i))
#         file.close()
#         archive.write(filename=file.name)

#
# from dataclasses import dataclass
# from zipfile import ZipFile
# import os
#
#
# @dataclass
# class FastAndTheFurious:
#     name: str
#     description: str
#
#
# movies = [
#     FastAndTheFurious(
#         name="The Fast and the Furious",
#         description="Street racer Brian O'Conner is recruited by the police to infiltrate a criminal gang."),
#     FastAndTheFurious(
#         name="2 Fast 2 Furious",
#         description="Brian O'Conner teams up with an ex-con to bring down a Miami drug lord."),
#     FastAndTheFurious(
#         name="The Fast and the Furious: Tokyo Drift",
#         description="A high school student gets involved in the Tokyo drift racing scene."),
#     FastAndTheFurious(
#         name="Fast & Furious",
#         description="Dominic Toretto and Brian O'Conner join forces to take down a heroin importer."),
#     FastAndTheFurious(
#         name="Fast Five",
#         description="Dominic Toretto and his crew plan a massive heist to buy their freedom."),
#     FastAndTheFurious(
#         name="Fast & Furious 6",
#         description="Dominic Toretto and his team help the government take down a skilled mercenary group."),
#     FastAndTheFurious(
#         name="Furious 7",
#         description="Dominic Toretto and his crew face off against a terrorist who seeks revenge."),
#     FastAndTheFurious(
#         name="The Fate of the Furious",
#         description="Dominic Toretto turns against his team when he is blackmailed by a cyberterrorist."),
#     FastAndTheFurious(
#         name="F9",
#         description="Dominic Toretto and his family face off against Dom's younger brother, who is working with a dangerous technology."),
# ]
#
# # ZipFile - поддерживает протокол менеджера контекста
# #
# with ZipFile('FastAndTheFurious.zip', mode='a') as archive:
#     for inst in range(len(movies)):
#         # path = 'number_' + str(i) + '.txt'
#         file = open(file=movies[inst].name + '.txt', encoding='utf-8', mode='w')
#         file.write(movies[inst].description)
#         file.close()
#         archive.write(filename=file.name)


#
# from zipfile import ZipFile
#
# whole_size = 0
# with ZipFile('files.zip', mode='r') as archive:
#     for info in archive.infolist():
#         if info.filename.endswith('.json'):
#             whole_size += info.file_size
# print(whole_size)



