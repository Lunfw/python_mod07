from ex0.Card import Card
from typing import Dict


class GeneralErrors(Exception):
    pass


class CardErrors(Exception):
    pass


class CreatureCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: str, attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self._attack = attack
        self._health = health
        self.mana = 10

    def play(self, game_state: Dict) -> Dict:
        '''
            #   Play my games.
        '''
        from random import randint
        self.mana = randint(1, 10)
        temp: Dict = {}
        temp = {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Creature summoned to battlefield'
        }
        if (self.mana - self.cost <= 0):
            self.mana = 0
        else:
            self.mana -= self.cost
        return (temp)

    def attack_target(self, target) -> Dict:
        '''
            #   Attacks a target passed down as parameter.
        '''
        temp: Dict = {}
        print(f'\n{self.name} attacks {target.name}:')
        try:
            if (target.name == self.name):
                raise CardErrors(f'{self.name} attacks itself... wtf?')
            if (target.health - self.attack < 0):
                target.health = 0
            else:
                target.health -= self.attack
            temp = {
                'attacker': self.name,
                'target': target.name,
                'damage_dealt': self.attack
            }
            if (target.health > 0):
                temp['combat_resolved'] = False
            temp['combat_resolved'] = True
        except CardErrors as e:
            print(f'Error: {e}')
        print(temp)
        return temp

    @property
    def health(self) -> int:
        '''
            #   HP getter.
        '''
        return (self._health)

    @health.setter
    def health(self, value: int) -> None:
        '''
            #   HP setter.
        '''
        try:
            if (value < 0):
                raise CardErrors('HP cannot be negative')
            self._health = value
        except CardErrors as e:
            print(f'Error: {e}')
            self._health = 10
            return

    @property
    def attack(self) -> int:
        '''
            #   AP getter.
        '''
        return (self._attack)

    @attack.setter
    def attack(self, value: int) -> None:
        '''
            #   AP setter.
        '''
        try:
            if (value < 0):
                raise CardErrors('AP cannot be negative')
            self._attack = value
        except CardErrors as e:
            print(f'Error: {e}')
            self._attack = 5
            return

    @property
    def mana(self) -> int:
        '''
            #   Mana getter.
        '''
        return (self._mana)

    @mana.setter
    def mana(self, value: int) -> None:
        '''
            #   Mana setter.
        '''
        try:
            if (value < 0):
                raise CardErrors('Mana cannot be negative')
            self._mana = value
        except CardErrors as e:
            print(f'Error: {e}')
            self._mana = 10
            return
