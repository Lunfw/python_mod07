from ex2.EliteCard import EliteCard
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex0.Card import Card


def card_lib() -> tuple:
    '''
        #   Card Library
        #   Creating an EliteCard:
            #   EliteCard(name, cost, rarity, def, atk, hp)
    '''
    temp: tuple = (
        EliteCard('Arcane Warrior', 3, 'Rare', 2, 5, 20),
    )
    return (temp)


def get_funcs(type: (Card or Combatable or Magical)) -> list:
    '''
        #   Returns the methods of a class, excluding:
            #   __init__, property + getter/setter
    '''
    temp: list = []
    exclude: tuple = (
        '__init__',
        'cost',
        'name',
        'rarity'
    )
    for i in dir(type):
        if (i.startswith('_') or i.endswith('_') or i in exclude):
            continue
        temp.append(i)
    return (temp)


def main_exec() -> None:
    '''
        #   Main Execution Program
    '''
    cards = card_lib()
    print('EliteCard capabilities:')
    print(f'- Card: {get_funcs(Card)}')
    print(f'- Combatable: {get_funcs(Combatable)}')
    print(f'- Magical: {get_funcs(Magical)}\n')

    for i in cards:
        trim: str = i.__class__.__name__[:-4]
        temp: tuple = (
            i.play({})[0]['atk'],
            i.play({})[0]['def'],
            i.play({})[1]['spell'],
            i.play({})[1]['mana']
        )
        print(f'\nPlaying {i.name} ({trim} Card)')
        print('\nCombat phase:')
        print(f'Attack result: {temp[0]}')
        print(f'Defense result: {temp[1]}')
        print('\nMagic phase:')
        print(f'Spell cast: {temp[2]}')
        print(f'Mana channel: {temp[3]}')


def main() -> None:
    '''
        #   Small main program.
    '''
    print('\n=== DataDeck Ability System ===\n')
    main_exec()
    print('\nMultiple interface implementation successful!')


if (__name__ == "__main__"):
    main()
