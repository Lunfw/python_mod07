from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def card_lib() -> FantasyCardFactory:
    '''
        #   Card library.
    '''
    factory = FantasyCardFactory()
    factory.create_creature('dragon, goblin')
    factory.create_spell('fireball')
    factory.create_artifact('mana_ring')
    return (factory)


def output(data: list[tuple[str, int]]) -> str:
    formatted = ', '.join(f'{name} ({value})'
                          for name, value in data)
    return (formatted)


def main_exec():
    '''
        #   Main execution program.
    '''
    factory: FantasyCardFactory = card_lib()
    strategy: AggressiveStrategy = AggressiveStrategy()
    card_lib()
    print(f'Configuring Fantasy Card Game...')
    print(f'Factory: {factory.__class__.__name__}')
    print(f'Strategy: {strategy.__class__.__name__}')
    print(f'Available types: {factory.get_supported_types()}\n')

    print('Simulating aggressive turn...')
    strategy = AggressiveStrategy()
    data_aggressive = [
        ('Fire Dragon', 5),
        ('Goblin Warrior', 2),
        ('Lightning Bolt', 3),
    ]
    sort_aggressive = strategy.prioritize_targets(data_aggressive)
    formatted = output(sort_aggressive)
    print(f'Hand: [{formatted}]\n')

    print('Turn execution:')
    print(f'Strategy: {strategy.get_strategy_name()}')

    battlefield = [
        ('Enemy Player', 20)
    ]
    execute = strategy.execute_turn(data_aggressive, battlefield)
    print(f'Actions: {execute}\n')
    engine = GameEngine()
    engine.configure_engine(factory, strategy)
    engine.simulate_turn(data_aggressive, battlefield)
    report = engine.get_engine_status()
    print(f'Game Report:\n{report}\n')


def main():
    '''
        #   Small main program.
    '''
    print('\n=== DataDeck Game Engine ===\n')
    main_exec()
    print('Abstract Factory + Strategy Pattern: Maximum flexibility achieved!')


main()
