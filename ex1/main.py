from sys import exit
from ex0 import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex1.Deck import Deck


def card_lib() -> list:
    '''
        #   Lib for cards.
        #   Creating a Card:
            #   Card(name, cost, rarity)
            #   CreatureCard(name, cost, rarity, ap, hp)
            #   ArtifactCard(name, cost, rarity, durability, effect)
            #   SpellCard(name, cost, rarity, effect_type)
    '''
    temp: list = [
        ArtifactCard('aura monster card', 2, 'cool asl', 10, 'is op asf'),
        SpellCard('celestial sight', 3, 'Epic', 'straight up kills you'),
        CreatureCard('megalodaunt', 1, 'kinda op', 1, 1)
    ]
    return (temp)


def main_exec() -> None:
    '''
        #   Runs mandatory tests. (example output)
    '''
    deck: Deck = Deck()
    deck.cards = card_lib()
    print('\nBuilding deck with different card types...')
    print(f'Deck stats: {deck.get_deck_stats()}')

    print('\nDrawing and playing cards:\n')
    for card in deck.cards:
        temp: str = card.__class__.__name__[:-4]
        print(f'Drew: {card.name} ({temp})')
        print(f'Play result: {card.play({})}\n')


def main() -> None:
    print('\n=== DataDeck Deck Builder ===')
    main_exec()
    print('Polymorphism in action: Same interface, different card behaviors!')
    exit(1)


if (__name__ == "__main__"):
    main()
