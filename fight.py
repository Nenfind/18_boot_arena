from random import choice, choices, randint
from models import Paladin, Warrior, Thing


things_number = 5
things = []
for _ in range(things_number):
    thing = Thing()
    things.append(thing)

fighters_number = 10
fighters: list = []
for _ in range(fighters_number):
    paladin = Paladin()
    warrior = Warrior()
    fighter = choice([paladin, warrior])
    thing_number_per_figther = randint(1, 4)
    things_per_fighter = choices(things, k=thing_number_per_figther)
    fighter.set_things(things_per_fighter)
    fighters.append(fighter)
