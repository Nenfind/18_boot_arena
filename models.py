from random import choice, uniform


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
    """Class that describes the base game object."""

    def __init__(self, name, defence_percent, life, attack) -> None:
        self.name = name
        self.defence_percent = defence_percent
        self.life = life
        self.attack = attack


class Thing(GameObject):
    """Class that describes the thing."""

    def __init__(self, name, defence_percent=MIN_DEFENCE_PERCENT, life, attack):
        self.name = name
        self.defence_percent = defence_percent
        self.life = life
        self.attack = attack
        
        
class Person(GameObject):
    """Class that describes the person."""

    def __init__(self, name, defence_percent, life, attack, thing_list):
        self.name = name
        self.defence_percent = defence_percent
        self.life = life
        self.attack = attack
        self.thing_list = []

    def set_things(self, things):
        self.thing_list = things
        for thing in things:
            thing_defence += thing.defence_percent
            thing_attack += thing.attack
            thing_life += thing.life
        self.defence_percent = self.defence_percent + thing_defence 
        self.life = self.life + thing_life 
        self.attack = self.attack + thing_life

    def take_damage(self):
        damage = attack_damage - attack_damage * final_protection
        self.life = hit_points - damage