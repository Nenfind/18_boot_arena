from random import choice


MIN_DEFENCE_PERCENT = choice(range((1/100), (10/100)))
MIN_LIFE = 1
MIN_ATTACK = 1
NAME_FOR_PERSON_LIST = ['wolf', 'bear', 'dog', 'cat', 'capibara',
             'fox', 'mice', 'elephant', 'giraffe', 'hippopotamus',
            'rhinoceros', 'jackal', 'antelope', 'horse', 'raccoon',
            'fly', 'mosquito', 'spider', 'butterfly', 'mite']
NAME_FOR_THING_LIST = ['ring', 'jacket', 'throusers', 'hat', 'boots']


class GameObject():
    """Class that describes the base game object."""

    def __init__(self, name, defence_percent, life, attack) -> None:
        self.name = name
        self.defence_percent = defence_percent
        self.life = life
        self.attack = attack


class Thing(GameObject):
    """Class that describes the thing."""

    def __init__(self, name, defence_percent, life, attack):
        self.name = name
        self.defence_percent = defence_percent
        self.life = life
        self.attack = attack
        
        
class Person(GameObject):
    """Class that describes the person."""

    def __init__(self, name, defence_percent, life, attack):
        self.name = name
        self.defence_percent = defence_percent
        self.life = life
        self.attack = attack
