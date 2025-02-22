from random import choice, sample, randint
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
    things_per_fighter = sample(things, k=thing_number_per_figther)
    fighter.set_things(things_per_fighter)
    fighters.append(fighter)

opponents = sample(fighters, k=2)
first_fighter = choice(opponents)
second_fighter = opponents[0] if (first_fighter != opponents[0]) else opponents[1]

print(f'------------- Opponents {first_fighter.name} and {second_fighter.name}')

while (first_fighter.life > 0 and second_fighter.life > 0):
    first_attack_damage = first_fighter.attack
    print(f'first_attack_damage {first_attack_damage}')
    second_fighter.take_damage(first_attack_damage)
    print(f'second_fighter life {second_fighter.life}')
    second_attack_damage = second_fighter.attack
    print(f'second_attack_damage {second_attack_damage}')
    first_fighter.take_damage(second_attack_damage)
    print(f'first_fighter life {first_fighter.life}')

if first_fighter.life <= 0:
    fighters.remove(first_fighter)
    winner = second_fighter
else:
    fighters.remove(first_fighter)
    winner = second_fighter
print(f'------------------Winner is {winner.name}')
print(f'------------------Life of {winner.name}={winner.life}')
