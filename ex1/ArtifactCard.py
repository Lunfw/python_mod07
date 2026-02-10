from ex0 import Card


class ArtifactCard(Card):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 durability: int,
                 effect: str):
        super().__init__(name, cost, rarity)
        self._durability = durability
        self._effect = effect

    @property
    def name(self) -> str:
        return (self._name)

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def cost(self) -> int:
        return (self._cost)

    @cost.setter
    def cost(self, value: int):
        self._cost = value

    @property
    def rarity(self) -> str:
        return (self._rarity)

    @rarity.setter
    def rarity(self, value: str):
        self._rarity = value

    @property
    def durability(self) -> int:
        return (self._durability)

    @durability.setter
    def durability(self, value: int):
        self._durability = value

    @property
    def effect(self) -> str:
        return (self._effect)

    @effect.setter
    def effect(self, value: str):
        self._effect = value

    def play(self, game_state: dict) -> dict:
        '''
            #   Displays outcomes of a card being played.
        '''
        game_state: dict = {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': self.effect
        }
        return (game_state)

    def activate_ability(self) -> dict:
        return (self.effect)
