from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self,
                 card_id: str,
                 name: str,
                 card_type: str,
                 cost: int,
                 power: int,
                 rarity: str = 'Common'):
        super().__init__(name, cost, rarity)

        self.card_id = card_id
        self.card_type = card_type
        self.power = power
        self.health = 100
        self.wins = 0
        self.losses = 0
        self.base_rating = 1200

    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Creature summoned'
        }

    def attack(self, target) -> dict:
        target.health -= self.power
        return {
            'attacker': self.name,
            'target': target.name,
            'damage': self.power
        }

    def defend(self, incoming_damage: int) -> dict:
        self.health -= incoming_damage
        return {
            'defender': self.name,
            'damage_taken': incoming_damage,
            'health_remaining': max(0, self.health)
        }

    def get_combat_stats(self) -> dict:
        return {
            'name': self.name,
            'power': self.power,
            'health': self.health
        }

    def calculate_rating(self) -> int:
        return self.base_rating + (self.wins * 16) - (self.losses * 16)

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> dict:
        return {
            'wins': self.wins,
            'losses': self.losses,
            'rating': self.calculate_rating(),
            'record': f'{self.wins}-{self.losses}'
        }
