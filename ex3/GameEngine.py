from ex3.AggressiveStrategy import AggressiveStrategy


class GameEngine():
    def __init__(self):
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0
        self.factory = None
        self.strategy = None

    def configure_engine(self, factory, strategy) -> None:
        self.factory = factory
        self.strategy = strategy
        self.strategy_used = strategy.get_strategy_name()

    def simulate_turn(self, hand_data: list, battlefield_data: list) -> dict:
        self.turns_simulated += 1
        self.cards_created = len(hand_data)
        actions = self.strategy.execute_turn(hand_data, battlefield_data)
        self.total_damage = sum(value for _, value in hand_data)
        return {
            'turn': self.turns_simulated,
            'actions': actions,
            'cards_used': self.cards_created,
            'damage_dealt': self.total_damage
        }

    def get_engine_status(self) -> dict:
        aggressive = AggressiveStrategy()
        return {
            'turns_simulated': self.turns_simulated,
            'strategy_used': aggressive.get_strategy_name(),
            'total_damage': self.total_damage,
            'cards_created': self.cards_created
        }
