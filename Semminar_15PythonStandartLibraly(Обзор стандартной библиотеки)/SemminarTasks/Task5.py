# # Дорабатываем задачу 4. Добавьте возможность запуска из командной строки.
# # При этом значение любого параметра можно опустить.
# # В этом случае берётся первый в месяце день недели, текущий день недели и/или текущий месяц.
# # *Научите функцию распознавать не только текстовое названия дня недели и месяца, но и числовые, т.е не мая, а 5.
#
# import datetime
# from task3 import logging_decorator
# import argparse
#
#
# months = {'января': 1, 'февраля': 2, 'марта': 3,
# 'апреля': 4, 'мая': 5, 'июня': 6,
# 'июля': 7, 'августа': 8, 'сентября': 9,
# 'октября': 10, 'ноября': 11, 'декабря': 12}
#
# weekdays = {'понедельник': 0, 'вторник': 1, 'среда': 2, 'четверг': 3,
# 'пятница': 4, 'суббота': 5, 'воскресенье': 6}
#
# @logging_decorator
# def date_from_text(date):
# day, weekday, month = date.split()
# weeks = int(day.split('-')[0])
# month = months[month]
# weekday = weekdays[weekday]
# date_ = datetime.datetime(year=datetime.datetime.now().year, month=month, day=1)
# while date_.weekday() != weekday:
# date_ += datetime.timedelta(days=1)
# result = date_ + datetime.timedelta(weeks=weeks-1)
# if result.month != month:
# raise ValueError('Такой даты не существует!')
# return result
#
#
# def out_parser():
# parser = argparse.ArgumentParser(description='My first argument parser')
# parser.add_argument('-d', '--date', nargs='*')
# return parser.parse_args()
#
#
# if __name__ == '__main__':
# out = out_parser()
# out = ' '.join(out.date)
# print(date_from_text(out))