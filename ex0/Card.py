from abc import ABC, abstractmethod
from typing import Dict


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str):
        '''
            #   Creates a card entity.
        '''
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @property
    def name(self):
        '''
            #   Name getter.
        '''
        return (self._name)

    @name.setter
    def name(self, value):
        '''
            #   Name setter.
        '''
        self._name = value

    @property
    def cost(self):
        '''
            #   Cost getter.
        '''
        return (self._cost)

    @cost.setter
    def cost(self, value):
        '''
            #   Cost setter.
        '''
        self._cost = value

    @property
    def rarity(self):
        '''
            #   Rarity getter.
        '''
        return (self._rarity)

    @rarity.setter
    def rarity(self, value):
        '''
            #   Rarity setter.
        '''
        self._rarity = value

    @abstractmethod
    def play(self, game_state: Dict) -> Dict:
        '''
            #   Play my games.
        '''
        pass

    def get_card_info(self) -> Dict:
        '''
            #   Literally get the card's info.
        '''
        print('\nCreatureCard Info:')
        temp: Dict[Dict] = {}
        try:
            temp[self.name] = {
                'name': self.name,
                'cost': self.cost,
                'rarity': self.rarity,
                'type': 'Creature',
                'attack': self.attack,
                'health': self.health
            }
        except AttributeError:
            print('# An error happened in the code.')
            return (0)
        return (temp)

    def is_playable(self, available_mana: int) -> bool:
        '''
            #   Checks whether the current card can be played.
        '''
        return (self.mana > 3 and self.health >= 3)
