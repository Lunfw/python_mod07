from abc import ABC, abstractmethod


class Magical(ABC):
    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        '''
            #   Cast my spell bro.
        '''
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        '''
            #   Channels mana.
        '''
        pass

    @abstractmethod
    def get_magic_stats(self) -> dict:
        '''
            #   Returns magic stats.
        '''
        pass
