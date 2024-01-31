# Задание №4
# Функция получает на вход текст вида: “1-й четверг ноября”, “3-
# я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату.


import datetime
from Task3 import logging_decorator


months = {'января': 1, 'февраля': 2, 'марта': 3,
    'апреля': 4, 'мая': 5, 'июня': 6,
    'июля': 7, 'августа': 8, 'сентября': 9,
    'октября': 10, 'ноября': 11, 'декабря': 12}

weekdays = {'понедельник': 0, 'вторник': 1, 'среда': 2, 'четверг': 3,
            'пятница': 4, 'суббота': 5, 'воскресенье': 6}

@logging_decorator
def date_from_text(date):
    day, weekday, month = date.split()
    weeks = int(day.split('-')[0])
    month = months[month]
    weekday = weekdays[weekday]
    date_ = datetime.datetime(year=datetime.datetime.now().year, month=month, day=1)
    while date_.weekday() != weekday:
        date_ += datetime.timedelta(days=1)
    result = date_ + datetime.timedelta(weeks=weeks-1)
    if result.month != month:
        raise ValueError('Такой даты не существует!')
    return result


if __name__ == '__main__':
    print(date_from_text('1-й четверг ноября'))