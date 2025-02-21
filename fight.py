from random import randint
from models import Paladin, Warrior, Thing

def main():
    paladin_count = randint(1, 10)
    warrior_count = 10 - paladin_count
    fighters = {f'fighter{i}': Paladin() for i in range(paladin_count)}
    for i in range(warrior_count):
        fighters[f'fighter{i + paladin_count}'] = Warrior()
    thing_count = randint(10, 40)
    things = {i: Thing() for i in range(thing_count)}

if __name__ == '__main__':
    main()