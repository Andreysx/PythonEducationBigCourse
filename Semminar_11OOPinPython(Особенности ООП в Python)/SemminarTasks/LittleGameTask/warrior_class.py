# Контекст: Вы разработчик игры. Ваша задача - реализовать симуляцию боя между двумя персонажами, названными "Воин".
#
# Требования к задаче:
#
# Инициализация Персонажей: Создайте два объекта "Воин", каждый с начальным здоровьем в 100 очков.
#
# Механика Боя: Воины атакуют друг друга в случайном порядке. При этом, воин, который атакует, не теряет здоровья.
#
# Потери от Удара: Когда воин атакует, здоровье противника уменьшается на случайно от 10 до 15 очков за каждый удар.
#
# Отображение Информации: После каждой атаки выводите сообщение с указанием, кто атаковал и сколько здоровья осталось у атакованного воина.
#
# Конец Боя: Бой заканчивается, когда здоровье одного из воинов достигает нуля или меньше. При этом должно быть выведено сообщение о победителе.
#
# Цель: Реализуйте программу на Python, которая моделирует описанный сценарий боя, соответствуя всем вышеуказанным требованиям.


from random import randint, choice


class Warrior:
    __START_HP = 100

    def __init__(self, name):
        self.name = name
        self.hp = self.__START_HP
        self.min_damage = 10
        self.max_damage = 15

    def __str__(self):
        return f"{self.name}[{self.hp}]"

    def attack(self, other):
        if isinstance(other, Warrior):
            damage = randint(self.min_damage, self.max_damage)
            other.hp -= damage
            print(f"{self} ударил на {damage} -> {other}")
        else:
            raise TypeError("Не работает с этим типом")


def fight(list_warriors: list[Warrior]):
    if len(list_warriors) < 2:
        return -1
    while True:
        if len(list_warriors) <= 1:
            return list_warriors
        random_attacker = choice(list_warriors)
        random_defender = choice([war for war in list_warriors if war != random_attacker])
        random_attacker.attack(random_defender)
        if random_defender.hp <= 0:
            list_warriors.remove(random_defender)


if __name__ == '__main__':
    w1, w2, w3, w4, w5 = Warrior("1"), Warrior("2"), Warrior("3"), Warrior("4"), Warrior("5")
    print(*fight([w1, w2, w3, w4, w5]))
