from Card import Card
from CreatureCard import CreatureCard
from typing import Dict, List


class MiniDB:
    db: List

    def __init__(self):
        self.db = []

    def add_card(self, card: Card):
        self.db.append(card)


def db_exec() -> MiniDB:
    '''
        #   DB exec. Initializes the DB as the output example.
    '''
    temp: tuple = (
        CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5),
    )
    data = MiniDB()
    for i in temp:
        data.add_card(i)
    return (data)


def card_info(L: List or Card) -> Dict or int:
    '''
        #   Info about the cards in the MiniDB.
    '''
    for i in L:
        print(i.get_card_info()[i.name])


def main_exec() -> None:
    '''
        #   Runs mandatory tests.
        #   CreatureCard -> (name, cost, rarity, attack, health)
    '''
    data: MiniDB = db_exec()
    gw: CreatureCard = CreatureCard('Goblin Warrior', 2, 'Common', 3, 5)
    print('Testing Abstract Base Class Design:')
    card_info(data.db)
    for i in data.db:
        i.play({})
    i.attack_target(gw)
    print(f'\nTesting insufficient mana ({i.mana} available):')
    for i in data.db:
        print(f'Playable: {i.is_playable(i.mana)}')
    return (1)


def main():
    print('\n=== DataDeck Card Foundation ===\n')
    if (not main_exec()):
        print('\n# Program ended due to an error.')
    print('\nAbstract pattern successfuly demonstrated!')


if (__name__ == '__main__'):
    main()
