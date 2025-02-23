from random import choice, sample, randint
from models import Paladin, Warrior, Thing


def main():
    things_number = 5
    things = []
    for _ in range(things_number):
        thing = Thing()
        things.append(thing)

    fighters_number = 10
    fighters = []
    fighters_set = set()
    for _ in range(fighters_number):
        paladin = Paladin()
        warrior = Warrior()
        fighter = choice([paladin, warrior])
        thing_number_per_figther = randint(1, 4)
        things_per_fighter = sample(things, k=thing_number_per_figther)
        fighter.set_things(things_per_fighter)
        fighters_set.add(fighter.name)
        if fighter.name in fighters_set:
            fighters.append(fighter)

    while len(fighters) > 1:
        opponents = sample(fighters, k=2)
        first_fighter = choice(opponents)
        second_fighter = opponents[0] if (first_fighter != opponents[0]) else opponents[1]

        print(f'------------- Opponents {first_fighter.name} and {second_fighter.name}')

        while (first_fighter.life > 0 and second_fighter.life > 0):
            first_attack_damage = first_fighter.attack
            print(f'{first_fighter.name} damage {first_attack_damage}')
            second_fighter.take_damage(first_attack_damage)
            print(f'{second_fighter.name} life {second_fighter.life}')
            if second_fighter.life <= 0:
                break
            second_attack_damage = second_fighter.attack
            print(f'{second_fighter.name} damage {second_attack_damage}')
            first_fighter.take_damage(second_attack_damage)
            print(f'{first_fighter.name} life {first_fighter.life}')
            if first_fighter.life <= 0:
                break

        if first_fighter.life < second_fighter.life:
            winner = second_fighter
            fighters.remove(first_fighter)
        else:
            winner = first_fighter
            fighters.remove(second_fighter)

        print(f'------------------Winner is {winner.name}')
        print(f'------------------Life of {winner.name}={winner.life}')
        print(f'------------------- Number of fightres {len(fighters)}')


if __name__ == '__main__':
    main()
