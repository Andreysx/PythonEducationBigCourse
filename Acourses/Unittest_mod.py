# import unittest
#
#
# def is_prime(number: int) -> bool:
#     if number < 2:
#         return False
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             return False
#     return True
#
#
# class PrimeNumberTestCase(unittest.TestCase):
#     def test_prime_numbers(self):
#         prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
#         for number in prime_numbers:
#             self.assertTrue(is_prime(number))
#
#     def test_non_prime_numbers(self):
#         non_prime_numbers = [4, 6, 8, 10, 12, 15, 14, 16, 18, 20, 22, 24, 25, 26]
#         for number in non_prime_numbers:
#             self.assertFalse(is_prime(number))
import unittest

# # all()
# import unittest
#
#
# def linear_search(lst, target):
#     for i, element in enumerate(lst):
#         if element == target:
#             return i
#     return -1
#
#
# class TestLinearSearchFunction(unittest.TestCase):
#     def test_empty_list(self):
#         self.assertEqual(linear_search([], 5), -1)
#
#     def test_positive_numbers_list(self):
#         self.assertEqual(linear_search([1, 2, 3, 4, 5, 6, 7, 0], 5), 4)
#
#     def test_negative_numbers_list(self):
#         self.assertEqual(linear_search([-1, -2, -3, -4, -5, -6, -7], -1), 0)
#
#     def test_mixed_numbers_list(self):
#         self.assertEqual(linear_search([1, -2, 3, -4, 5, -6, 7], 5), 4)
#
#     def test_list_without_desired_value(self):
#         self.assertEqual(linear_search([1, -2, 3, -4, 5, -6, 7], 0), -1)
#
#     def test_list_with_string(self):
#         self.assertEqual(linear_search(list('ABCDabcd'), 'd'), 7)


#
# # Сами функции располагаются в другом модуле check_list
# def is_sorted_ascending(lst: list) -> bool:
#     return all(lst[i] < lst[i + 1] for i in range(len(lst) - 1))
#
#
# def is_sorted_descending(lst: list) -> bool:
#     return all(lst[i] > lst[i + 1] for i in range(len(lst) - 1))


# Обычно функция, для которой пишут тесты, определена совершенно в другом модуле.
# В файлике, где выполняется тестирование,
# импортируют модуль и обращаются к интересующей функции.

# В теории мы находимся в файле для тестов(test.py)
# имитация импортирования
# import unittest
# from check_list import is_sorted_ascending, is_sorted_descending


# class TestSortedList(unittest.TestCase):
#     def test_01_is_sorted_ascending(self):
#         data = [1, 2, 3, 4, 5, 6, 7]
#         result = is_sorted_ascending(data)
#         self.assertTrue(result, msg='Список не возрастающий')
#
#     def test_02_is_sorted_ascending(self):
#         data = [1, 2, 3, 4, 5, 6, 7]
#         result = is_sorted_ascending(data)
#         self.assertIsInstance(result, bool, msg='Результат не логический тип данных')
#
#     def test_03_is_sorted_descending(self):
#         data = [7, 6, 5, 4, 3, 2, 1]
#         result = is_sorted_descending(data)
#         self.assertTrue(result, msg='Список не нисходящий')
#
#     def test_04_is_sorted_descending(self):
#         data = [7, 6, 5, 4, 3, 2, 1]
#         result = is_sorted_descending(data)
#         self.assertIsInstance(result, bool, msg='Результат не логический тип данных')


# if __name__ == '__main__':
#     unittest.main()


# Тестируем функцию написание тестов для функции
# Перед вами функция divide_numbers

# def divide_numbers(a, b):
#     if b == 0:
#         raise ValueError("Division by zero is not allowed")
#     elif a < 0 or b < 0:
#         raise ValueError("Both numbers must be non-negative")
#     elif a % b != 0:
#         raise ValueError("Numbers must be divisible without remainder")
#     else:
#         return a // b
#
#


# # Ваша задача - определить все возможные варианты входных значений
# # для данной функции и для каждого варианта написать тестовый случай
#
# import unittest
#
#
# class CheckDivideOptions(unittest.TestCase):
#     def test_01(self):
#         with self.assertRaisesRegex(expected_exception=ValueError, expected_regex="Division by zero is not allowed"):
#             divide_numbers(10, 0)
#
#     def test_02(self):
#         a, b = -1, -1
#         with self.assertRaisesRegex(expected_exception=ValueError,expected_regex="Both numbers must be non-negative"):
#             divide_numbers(a, b)
#
#     def test_03(self):
#         a, b = 5, 3
#
#         with self.assertRaisesRegex(expected_exception=ValueError,
#                                      expected_regex='Numbers must be divisible without remainder'):
#             divide_numbers(a, b)
#
#     def test_4(self):
#         with self.assertRaises(TypeError, msg='Входные данные должны быть типом int'):
#             divide_numbers('123', 5)
#
#     def test_05(self):
#         self.assertEqual(divide_numbers(10, 5), 2)
#
#
# if __name__ == '__main__':
#     unittest.main()


# Написание тестов для класса ниже
import unittest


#
# class Book:
#     def __init__(self, title, author, pages, price):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.price = price
#
#     def __str__(self):
#         return f"{self.title} by {self.author}"
#
#     def get_reading_time(self):
#         return f"{self.pages * 1.5} minutes"
#
#     def apply_discount(self, discount):
#         if not isinstance(discount, float):
#             raise ValueError('Discount must be float number')
#         if 0 <= discount <= 1:
#             discounted_price = self.price - (discount * self.price)
#             return f"${discounted_price}"
#         raise ValueError('Discount must be float number between 0 and 1')
#
#
# book = Book('Metro 2033', 'Глуховский', 200, 3000)
#
#
# class TestBookClass(unittest.TestCase):
#     def test_01_init_method(self):
#         self.assertIsInstance(book.title, str, msg='Неверный тип данных для поля title')
#         self.assertIsInstance(book.author, str, msg='Неверный тип данных для поля author')
#         self.assertIsInstance(book.pages, int, msg='Неверный тип данных для поля pages')
#         self.assertIsInstance(book.price, (int | float), msg='Неверный тип данных для поля price')
#         # self.assertIsInstance(book.price, float, msg='Неверный тип данных для поля price')
#
#     def test_02_str__method(self):
#         self.assertEqual(book.__str__(), 'Metro 2033 by Глуховский', msg='Неверный формат вывода')
#
#     def test_03_get_reading_time(self):
#         self.assertEqual(book.get_reading_time(), '300.0 minutes', msg='Неправильные вычисления')
#
#     def test_04_apply_discount_not_float(self):
#         with self.assertRaisesRegex(ValueError, expected_regex='Discount must be float number'):
#             book.apply_discount(25)
#
#     def test_05_apply_discount_more_than_1(self):
#         with self.assertRaises(ValueError):
#             book.apply_discount(2)
#
#     def test_06_apply_discount_less_than_0(self):
#         with self.assertRaises(ValueError):
#             book.apply_discount(-1)
#
#     def test_07_apply_discount_good_case(self):
#         self.assertEqual(book.apply_discount(0.25), '$2250.0')


def summ(a, b):
    return a + b


class SummTest(unittest.TestCase):

    def test_01(self):
        # result =
        self.assertEqual(summ(3, 3), 6, msg='Bad')


if __name__ == 'main':
    unittest.main()
