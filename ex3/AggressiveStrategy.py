from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        return {
            'cards_played': [hand[1][0], hand[2][0]],
            'mana_used': hand[1][1] + hand[2][1],
            'targets_attacked': [battlefield[0][0]],
            'damage_dealt': hand[0][1] + hand[2][1]
        }

    def get_strategy_name(self) -> str:
        return 'AggressiveStrategy'

    def prioritize_targets(self, available_targets: list) -> list:
        sorted_hand = sorted(available_targets, key=lambda x: x[1])
        return sorted_hand
