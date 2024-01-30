import unittest
from module.task1 import task1


class TestTask1(unittest.TestCase):
    def test_1(self):
        self.assertEqual(task1("abc"), "abc")

    def test_2(self):
        self.assertEqual(task1("ABCabc"), 'abcabc')

    def test_3(self):
        self.assertEqual(task1("hello, world!"), 'hello world')

    def test_4(self):
        self.assertEqual(task1("hello Илья"), 'hello ')

    def test_5(self):
        self.assertEqual(task1("Hello, Илья!"), 'hello ')


if __name__ == '__main__':
    unittest.main()