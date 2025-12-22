from datetime import date
import pprint

# sweet_november = [date(2001, 11, i) for i in range(1, 31)]

# for i in range(1, 31):
#     sweet_november.append(date(2001, 11, i))


# may_days = {date(1945, 5, i): [date(1945, 5, j) for j in range(1, i + 1)] for i in range(1, 32)}
#
# print(may_days)

#
# from datetime import date
# from typing import Optional
#
#
# def find_max_date(dates: list[date]) -> Optional[date]:
#     return max(dates, default=None)

#
# from datetime import date
#
#
# def count_dates_within_interval(start_date: date,
#                                 end_date: date,
#                                 dates: list[date]) -> int:
#     count = 0
#     for date_ in dates:
#         if start_date <= date_ <= end_date or start_date >= date_ >= end_date:
#             count += 1
#     return count
#
#
#     # start_date, end_date = sorted((start_date, end_date))
#     #
#     # return sum(start_date <= date_ <= end_date for date_ in dates)
#
#
# test_dates = [
#     date(2021, 9, 1),
#     date(2021, 9, 2),
#     date(2021, 9, 3),
#     date(2021, 9, 4),
#     date(2021, 9, 5),
#     date(2021, 9, 4),
#     date(2021, 9, 3),
# ]
# assert count_dates_within_interval(
#     date(2021, 9, 1), date(2021, 9, 2), test_dates) == 2
#
# print(count_dates_within_interval(
#     date(2021, 9, 3), date(2021, 9, 1), test_dates))
# assert count_dates_within_interval(
#     date(2021, 9, 1), date(2021, 9, 3), test_dates) == 4
#
# assert count_dates_within_interval(
#     date(2021, 9, 3), date(2021, 9, 1), test_dates) == 4
#
# assert count_dates_within_interval(
#     date(2021, 9, 10), date(2021, 9, 6), test_dates) == 0
#
# assert count_dates_within_interval(
#     date(2021, 9, 10), date(2021, 9, 5), test_dates) == 1
#
# assert count_dates_within_interval(
#     date(2021, 8, 10), date(2021, 8, 20), test_dates) == 0
#
# assert count_dates_within_interval(
#     date(2021, 9, 20), date(2021, 8, 10), test_dates) == 7
#
# print('Good')

# from datetime import datetime
#
# print(datetime.now())


#
# from datetime import date
#
#
# class Customer:
#     def __init__(self, name: int, phone: str):
#         self.name = name
#         self.phone = phone
#
#
# class ReservationPeriod:
#     def __init__(self, start_date: date, end_date: date):
#         self.start_date = start_date
#         self.end_date = end_date
#
#
# class Room:
#     def __init__(self, room_number: int):
#         self.room_number = room_number
#         self.reservation_periods = []  # Список периодов бронирования для этой комнаты
#
#     def is_available(self, start_date: date, end_date: date) -> bool:
#         """Проверить доступность комнаты на указанный период."""
#         if not self.reservation_periods:
#             return True
#         elif self.reservation_periods[1] <= start_date or end_date <= self.reservation_periods[0]:
#             return True
#         else:
#             return False
#
#
#     def reserve(self, start_date: date, end_date: date) -> bool:
#         """Забронировать комнату на указанный период, если она доступна"""
#         if self.is_available(start_date, end_date):
#             self.reservation_periods.extend((start_date, end_date))
#             return True
#
#
#     def cancel_reservation(self, start_date: date, end_date: date) -> bool:
#         """Отменить бронирование на указанный период."""
#         self.reservation_periods.remove(start_date)
#         self.reservation_periods.remove(end_date)
#         return True
#
#
# class Hotel:
#     def __init__(self, name: str):
#         self.name = name
#         self.rooms = {}  # Словарь для хранения комнат в отеле
#
#     def add_room(self, room_number):
#         """Добавить комнату в отель."""
#         self.rooms[room_number] = Room(room_number)
#
#     def reserve_room(self, room_number, start_date: date, end_date: date):
#         """Забронировать комнату на указанный период."""
#         if room_number in self.rooms:
#             return self.rooms[room_number].reserve(start_date, end_date)
#         else:
#             return False
#
#     def cancel_reservation(self, room_number, start_date: date, end_date: date):
#         """Отменить бронирование комнаты на указанный период."""
#         if room_number in self.rooms:
#             return self.rooms[room_number].cancel_reservation(start_date, end_date)
#         else:
#             return False
#
#
# class Reservation:
#     def __init__(self, hotel, customer, room_number, start_date: date, end_date: date):
#         self.hotel = hotel
#         self.customer = customer
#         self.room_number = room_number
#         self.start_date = start_date
#         self.end_date = end_date
#
#     def make_reservation(self):
#         """Попытаться забронировать комнату на указанный период."""
#         if self.hotel.reserve_room(self.room_number, self.start_date, self.end_date):
#             return f"Бронирование успешно: {self.customer.name} забронировал комнату {self.room_number} в отеле {self.hotel.name} на период с {self.start_date.strftime('%Y-%m-%d')} по {self.end_date.strftime('%Y-%m-%d')}."
#         else:
#             return f"Извините {self.customer.name}, но комната {self.room_number} в отеле {self.hotel.name} на указанный период недоступна."
#
#     def cancel_reservation(self):
#         """Отменить бронирование комнаты на указанный период."""
#         if self.hotel.cancel_reservation(self.room_number, self.start_date, self.end_date):
#             return f"Бронирование отменено: {self.customer.name} отменил бронирование комнаты {self.room_number} в отеле {self.hotel.name} на период с {self.start_date.strftime('%Y-%m-%d')} по {self.end_date.strftime('%Y-%m-%d')}."
#         else:
#             return f"Ошибка отмены бронирования: комната {self.room_number} в отеле {self.hotel.name} на указанный период не найдена."
#
#
# # Создаем объекты покупателя и отеля
# customer1 = Customer("Иван", "123-456-789")
# customer2 = Customer("Петя", "789-456-123")
# hotel1 = Hotel("Отель 'Летний бриз'")
#
# # Добавляем комнаты в отель
# hotel1.add_room(101)
# hotel1.add_room(102)
# hotel1.add_room(103)
#
# # Создаем заказ и пытаемся забронировать комнату на период
# reservation1 = Reservation(hotel1, customer1, 101, date(2023, 9, 25), date(2023, 9, 28))
# result1 = reservation1.make_reservation()
# # print(reservation1.hotel.rooms)
# print(result1)
#
# # Пытаемся забронировать ту же комнату на тот же период
# result2 = reservation1.make_reservation()
# print(result2)
#
# # Пытаемся забронировать ту же комнату другим покупателем с пересекающимся интервалом
# reservation2 = Reservation(hotel1, customer2, 101, date(2023, 9, 27), date(2023, 9, 30))
# print(reservation2.make_reservation())
#
# # Меняем дату заезда, прежний посетитель в этот день должен выехать из номера
# reservation2.start_date = date(2023, 9, 28)
# print(reservation2.make_reservation())
#
# # Отменяем бронирование
# cancel_result = reservation1.cancel_reservation()
# print(cancel_result)
#
# # Пытаемся забронировать комнату после отмены
# result3 = reservation1.make_reservation()
# print(result3)

# Найдите разницу в секундах между 28 сентября 2012 года в момент времени 12:32:30 и
# 5 мая 2024 года в момент времени 08:00:00
#
# В качестве ответа укажите найденную разницу в секундах в виде положительного числа

# from datetime import datetime
#
# d1 = datetime(2012, 9, 28, 12, 32, 30)
# d2 = datetime(2024, 5, 5, 8)
#
# res = d2 - d1
# print(f"{int(abs(res).total_seconds())}")


# from datetime import datetime
#
# def get_diff_dates_in_days(dt1: datetime, dt2: datetime) -> int:
#     res = dt2 - dt1
#     return abs(res.days)
#
#
#
# date3 = datetime(2023, 1, 3, 18, 30, 0)  # 3 января 2023 года, 18:30:00
# date4 = datetime(2023, 1, 1, 12, 0, 0)  # 1 января 2023 года, 12:00:00
# print(get_diff_dates_in_days(date3, date4))


#
#
# from collections import Counter
#
#
# def calculate_sales(*sales_dicts) -> Counter:
#     result = Counter()
#     for i in range(len(sales_dicts)):
#         result += sales_dicts[i]
#     return result
# # def calculate_sales(*sales_dicts) -> Counter:
# #     return reduce(lambda a, b: a + b, map(Counter, sales_dicts))
#
#
# # Пример использования функции
# sales_1 = {'John': 10, 'Mary': 5, 'Bob': 3, 'Alice': 7}
# sales_2 = {'John': 5, 'Mary': 8, 'Bob': 6, 'Alice': 2}
# sales_3 = {'John': 3, 'Mary': 4, 'Bob': 2, 'Alice': 9}
# sales_4 = {'John': 8, 'Alice': 5, 'Henry': 10}
#
# assert calculate_sales(sales_1, sales_2, sales_3) == Counter({'John': 18, 'Alice': 18, 'Mary': 17, 'Bob': 11})
# assert calculate_sales(sales_1, sales_2) == Counter({'John': 15, 'Mary': 13, 'Bob': 9, 'Alice': 9})
# assert calculate_sales(sales_3, sales_2) == Counter({'Mary': 12, 'Alice': 11, 'John': 8, 'Bob': 8})
# assert calculate_sales(sales_4, sales_2, sales_1) == Counter({'John': 23, 'Alice': 14, 'Mary': 13, 'Henry': 10, 'Bob': 9})


from collections import Counter


def count_min_goals(statistics):
    player_goals = Counter()

    for year_data in statistics.values():
        for player, goals in year_data.items():
            if player not in player_goals:
                player_goals[player] = goals
            else:
                if goals < player_goals[player]:
                    player_goals[player] = goals

    return player_goals


statistics = {
    2020: {'Messi': 20, 'Neymar': 30, 'Ronaldo': 25},
    2021: {'Neymar': 23, 'Griezmann': 47, 'Messi': 29},
    2022: {'Griezmann': 35, 'Messi': 34, 'Ronaldo': 34}
}

print(count_min_goals(statistics))
assert count_min_goals(statistics) == Counter({'Griezmann': 35, 'Ronaldo': 25, 'Neymar': 23, 'Messi': 20})

statistics = {
    2015: {'Benzema': 32, 'Griezmann': 43, 'Messi': 52, 'Neymar': 39, 'Ronaldo': 51},
    2016: {'Benzema': 26, 'Griezmann': 37, 'Messi': 36, 'Neymar': 35, 'Ronaldo': 42},
    2017: {'Benzema': 27, 'Griezmann': 51, 'Messi': 42, 'Neymar': 49, 'Ronaldo': 30},
    2018: {'Benzema': 32, 'Griezmann': 41, 'Messi': 45, 'Neymar': 30, 'Ronaldo': 43},
    2019: {'Benzema': 29, 'Griezmann': 39, 'Messi': 51, 'Neymar': 31, 'Ronaldo': 48},
    2020: {'Benzema': 33, 'Griezmann': 41, 'Messi': 36, 'Neymar': 30, 'Ronaldo': 25},
    2021: {'Benzema': 54, 'Griezmann': 47, 'Messi': 29, 'Neymar': 36, 'Ronaldo': 21},
    2022: {'Benzema': 29, 'Griezmann': 35, 'Messi': 34, 'Neymar': 36, 'Ronaldo': 34}
}
assert count_min_goals(statistics) == Counter(
    {'Griezmann': 35, 'Neymar': 30, 'Messi': 29, 'Benzema': 26, 'Ronaldo': 21})
