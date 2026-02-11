from abc import ABC, abstractmethod


class Combatable(ABC):
    @abstractmethod
    def attack(self, target) -> dict:
        '''
            #   Attack the target.
        '''
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        '''
            #   Defend against incoming damage.
        '''
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict:
        '''
            #   Get combat stats.
        '''
        pass
