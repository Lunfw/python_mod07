from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GeneralErrors(Exception):
    pass


class GameEngine:
    def __init__(self):
        self.deck: dict = {
            'creature': [],
            'spell': [],
            'artifact': []
        }
        self.factory: CardFactory = None
        self.strategy: GameStrategy = None

    def configure_engine(self, factory: CardFactory = None,
                         strategy: GameStrategy = None) -> None:
        print('\nConfiguring Fantasy Card Game...')
        self.factory = factory
        self.strategy = strategy
        print('Factory:', self.factory.__class__.__name__)
        print('Strategy:', self.strategy.__class__.__name__)
        print(f'Available types: {self.factory.get_supported_types()}')

    def simulate_turn(self) -> dict:
        temp: tuple = (
            self.factory.create_creature('Fire dragon'),
            self.factory.create_creature('Goblin'),
            self.factory.create_spell('Lightning Bolt')
        )
        for i in temp:
            if ('creature' in i.__class__.__name__.lower()):
                self.deck['creature'].append(i)
            elif ('spell' in i.__class__.__name__.lower()):
                self.deck['spell'].append(i)
            elif ('artifact' in i.__class__.__name__.lower()):
                self.deck['artifact'].append(i)
        return (self.deck)

    def get_engine_status(self) -> dict:
        pass
