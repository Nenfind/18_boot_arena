from random import choice, uniform, randint


MIN_DEFENCE_PERCENT = uniform(0, 0.1)
MIN_LIFE = 1
MIN_ATTACK = 1
NAME_FOR_PERSON_LIST = ['wolf', 'bear', 'dog', 'cat', 'capibara',
                        'fox', 'mice', 'elephant', 'giraffe', 'hippopotamus',
                        'rhinoceros', 'jackal', 'antelope', 'horse', 'raccoon',
                        'fly', 'mosquito', 'spider', 'butterfly', 'mite']
NAME_FOR_THING_LIST = ['ring', 'jacket', 'throusers', 'hat', 'boots']
MAX_COUNT_OF_THINGS = 4


class GameObject():
    """Class that describes the base Game Object."""

    def __init__(self) -> None:
        self.name = None
        self.defence_percent = None
        self.life = self.give_life()
        self.attack = self.give_attack()

    def give_life(self):
        return randint(1, 100)

    def give_attack(self):
        return randint(1, 100)


class Thing(GameObject):
    """Class that describes the Thing."""

    def __init__(self):
        super().__init__()
        self.name = self.give_name()
        self.defence_percent = self.give_defence()

    def give_name(self):
        return choice(NAME_FOR_THING_LIST)

    def give_defence(self):
        percent = uniform(0, 0.1)
        round_percent = round(percent, 2)
        return round_percent


class Person(GameObject):
    """Class that describes the Person."""

    def __init__(self):
        super().__init__()
        self.name = self.give_name()
        self.defence_percent = self.give_defence()
        self.thing_list = []
        self.attacker = None

    def give_name(self):
        return choice(NAME_FOR_PERSON_LIST)

    def give_defence(self):
        percent = uniform(0, 0.3)
        round_percent = round(percent, 2)
        return round_percent

    def set_things(self, things):
        self.thing_list = things
        thing_defence = 0
        thing_attack = 0
        thing_life = 0
        for thing in things:
            thing_defence += thing.defence_percent
            thing_attack += thing.attack
            thing_life += thing.life
        self.defence_percent = self.defence_percent + thing_defence
        self.life = self.life + thing_life
        self.attack = self.attack + thing_life

    def take_damage(self, attack_damage):
        damage = attack_damage - attack_damage * self.defence_percent
        self.life = self.life - damage


class Paladin(Person):
    """Class that describes the Paladin."""

    def __init__(self):
        super().__init__()
        self.defence_percent = 2 * self.defence_percent
        self.life = 2 * self.life


class Warrior(Person):
    """Class that describes the Warrior."""

    def __init__(self):
        super().__init__()
        self.attack = 2 * self.attack
