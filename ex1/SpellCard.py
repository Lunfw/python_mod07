from ex0 import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        '''
            #   Creates a spell card type.
        '''
        super().__init__(name, cost, rarity)
        self._effect_type = effect_type

    @property
    def effect_type(self) -> str:
        '''
            #   Effect type getter.
        '''
        return (self._effect_type)

    @effect_type.setter
    def effect_type(self, value: str):
        '''
            #   Effect type setter.
        '''
        self._effect_type = value

    def play(self, game_state: dict) -> dict:
        '''
            #   Displays outcomes of a card being played.
        '''
        game_state: dict = {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': self.effect_type
        }
        return (game_state)

    def resolve_effect(self, targets: list) -> dict:
        return (self.effect_type)
