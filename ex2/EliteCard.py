from ex0.Card import Card
from ex2.Magical import Magical
from ex2.Combatable import Combatable


class EliteCard(Card, Combatable, Magical):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 atkp: int,
                 defp: int,
                 hp: int) -> None:
        '''
            #   Create an EliteCard.
        '''
        super().__init__(name, cost, rarity)
        self.atkp = atkp
        self.defp = defp
        self.hp = hp
        self.mana = 10

    @property
    def atkp(self):
        '''
            #   Atk getter.
        '''
        return (self._atkp)

    @atkp.setter
    def atkp(self, value):
        '''
            #   Atk setter.
        '''
        self._atkp = value

    @property
    def defp(self):
        '''
            #   Def getter.
        '''
        return (self._defp)

    @defp.setter
    def defp(self, value):
        '''
            #   Def setter.
        '''
        self._defp = value

    @property
    def hp(self):
        '''
            #   Hp getter.
        '''
        return (self._hp)

    @hp.setter
    def hp(self, value):
        '''
            #   Hp setter.
        '''
        self._hp = value

    @property
    def mana(self):
        '''
            #   Mana getter.
        '''
        return (self._mana)

    @mana.setter
    def mana(self, value):
        '''
            #   Mana setter.
        '''
        self._mana = value

    def attack(self, target) -> dict:
        '''
            #   Attacks a target.
        '''
        from random import randint
        return ({
            'attacker': self._name,
            'target': target,
            'damage': randint(1, self.atkp),
            'combat_type': 'melee'
        })

    def defend(self, incoming_damage: int) -> dict:
        '''
            #   Reduce incoming damage.
        '''
        return ({
            'defender': self._name,
            'damage_taken': incoming_damage,
            'damage_blocked': (a := incoming_damage - self.defp),
            'still_alive': (self.hp - a > 0)
        })

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        '''
            #   Cast a spell on targets.
        '''
        from random import randint
        used: int = randint(1, 10)
        self.mana -= used
        return ({
            'caster': self._name,
            'spell': spell_name,
            'targets': targets,
            'mana_used': used
        })

    def channel_mana(self, amount: int) -> dict:
        '''
            #   Channel mana.
        '''
        self.mana += amount
        return {
            'channeled': amount,
            'total_mana': self.mana
        }

    def play(self, game_state: dict) -> dict:
        '''
            #   Play the card.
        '''
        temp: tuple = (self.get_combat_stats(), self.get_magic_stats())
        return (temp)

    def get_combat_stats(self) -> dict:
        '''
            #   Get combat stats.
        '''
        return ({
            'atk': self.attack('Enemy'),
            'def': self.defend(2)
        })

    def get_magic_stats(self) -> dict:
        '''
            #   Get magic stats.
        '''
        return ({
            'spell': self.cast_spell('Fireball', ['Enemy1', 'Enemy2']),
            'mana': self.channel_mana(3)
        })
