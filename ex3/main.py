from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from random import randint


def main_exec() -> None:
    '''
        #   Main execution program.
    '''
    game_engine: GameEngine = GameEngine()
    game_engine.configure_engine(FantasyCardFactory(), AggressiveStrategy())
    print('\nSimulating aggressive turn...')
    d = game_engine.simulate_turn()
    hand: list[str] = []
    for i in d:
        for j in d[i]:
            hand.append(j.name)
    print(f'Hand: {hand}\n')
    print('Turn execution:')
    print(f'Strategy: {game_engine.strategy.__class__.__name__}')
    print(f'Actions: ')

def main() -> None:
    '''
        #   Small main program.
    '''
    print('\n=== DataDeck Game Engine ===')
    main_exec()


if (__name__ == "__main__"):
    main()
