from random import randint, choice
from models import Paladin, Warrior, Thing

def main():
    paladin_count = randint(1, 10)
    warrior_count = 10 - paladin_count
    fighters = {f'fighter{i}': Paladin() for i in range(paladin_count)}
    for i in range(warrior_count):
        fighters[f'fighter{i + paladin_count}'] = Warrior()
    for fighter in fighters.values():
        things = [Thing() for i in range(randint(1, 4))]
        fighter.set_things(things)
    while fighters:
        attacker = choice(list(fighters.values()))
        defender = choice(list(fighters.values()))
        while attacker == defender:
            defender = choice(list(fighters.values()))
        defender.take_damage(attacker.attack())
        if defender.life >= 0:
            fighters.pop(defender)


if __name__ == '__main__':
    main()