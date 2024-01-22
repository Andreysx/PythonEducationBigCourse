# Задание №5
# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.
#
# Задание №6
# Доработайте задачу 5.
# Вынесите общие свойства и методы классов в класс
# Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.
#
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def is_animal(self):
#         return 'This is animal'
#
#     def eat(self):
#         return f'{self.name} is eating'
#
#
# class Fish(Animal):
#     def __init__(self, name, max_depth):
#         super().__init__(name)
#         self.max_depth = max_depth
#
#     def spec(self):
#         return self.max_depth
#
#
# class Bird(Animal):
#     def __init__(self, name, wingspan):
#         super().__init__(name)
#         self.wingspan = wingspan
#
#     def spec(self):
#         return self.wingspan
#
#
# class Cat(Animal):
#     def __init__(self, name, jump_height):
#         super().__init__(name)
#         self.jump_height = jump_height
#
#     def spec(self):
#         return self.jump_height
#
#
# if __name__ == '__main__':
# nemo = Fish('Nemo', 500)
# pat = Bird('pat', 250)
# cat = Cat('Murazik', 200)
#
# print(nemo.eat())

