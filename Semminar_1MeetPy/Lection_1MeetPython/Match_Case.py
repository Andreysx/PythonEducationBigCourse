# В Python версии 3.10, т.е. совсем недавно появилась новая возможность
# множественного сравнения. Это конструкция match и case. После match указываем
# переменную для сравнения. Далее идёт блок из множества case с вариантами
# сравнения. Рассмотрим работу кода на примере.
# 🔥 Важно! Если у вас стоит Python версии 3.9 и ниже, код не будет работать.
# color = input('Твой любимый цвет: ')
# match color:
#   case 'красный' | 'оранжевый':
#       print('Любитель яркого')
#   case 'зелёный':
#       print('Ты не охотник?')
#   case 'синий' | 'голубой':
#        print('Ха, классика!')
#    case _:
#        print('Тебя не понять')