from ex0 import Card, CreatureCard, CardErrors
from ex1 import ArtifactCard, SpellCard


class Deck:
    cards: list[Card]

    def __init__(self):
        '''
            #   Create a new Deck.
        '''
        self.cards = []

    def add_card(self, card: Card) -> None:
        '''
            #   Add a card to the deck.
        '''
        self.cards.append(card)

    def remove_card(self, card_name: str) -> None:
        '''
            #   Remove a card from the deck.
        '''
        try:
            if (card_name not in self.cards):
                raise CardErrors('Card not found')
            self.cards.remove(card_name)
        except CardErrors as e:
            print(f'Error: {e}')

    def shuffle(self) -> None:
        from random import shuffle
        shuffle(self.cards)

    def draw_card(self) -> Card:
        card: Card = self.cards.pop(0)
        return (card)

    def get_deck_stats(self) -> dict:
        '''
            #   Get deck stats, literally.
        '''
        d: dict = {
            'total_cards': 0,
            'creatures': 0,
            'spells': 0,
            'artifacts': 0,
            'avg_cost': 0.0
        }

        for i in self.cards:
            d['total_cards'] += 1
            if isinstance(i, CreatureCard):
                d['creatures'] += 1
            elif isinstance(i, SpellCard):
                d['spells'] += 1
            elif isinstance(i, ArtifactCard):
                d['artifacts'] += 1
            d['avg_cost'] += i.cost

        try:
            d['avg_cost'] /= d['total_cards']
        except ZeroDivisionError:
            d['avg_cost'] = 0
        return (d)
