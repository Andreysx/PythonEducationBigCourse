# Цикл с нумерацией элементов, функция
# enumerate()
# В финале рассмотрим ещё одну функцию, enumerate(). Она позволяет добавить
# порядковый номер к элементам итерируемой последовательности. Доработаем
# пример с животными. Будем выводить порядковый номер перед указанием
# животного.
animals = ['cat', 'dog', 'wolf', 'rat', 'dragon']
for i, animal in enumerate(animals, start=1):
    print(i, animal)
# Что изменилось?
# ● После for указано две переменные через запятую. В i будет помещаться
# порядковый номер. В animal очередное животное из списка.
# ● Функция enumerate() получила в качестве первого аргумента список
# животных. Второй аргумент — стартовое значение счётчика, т.е. первое
# значение, которое попадёт в i.
# Если второй аргумент не передать, нумерация начнётся с нуля.
# 🔥 Важно! Функция enumerate позволяет перебирать только целые числа в
# порядке возрастания с шагом один.
