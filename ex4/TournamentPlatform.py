from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self):
        self.registered_cards = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        self.registered_cards[card.card_id] = card
        print(f'{card.name} (ID: {card.card_id}):')
        print('  - Interfaces: [Card, Combatable, Rankable]')
        print(f'  - Rating: {card.calculate_rating()}')
        print(f'  - Record: {card.get_rank_info()["record"]}\n')
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self.registered_cards[card1_id]
        card2 = self.registered_cards[card2_id]

        if card1.power >= card2.power:
            winner = card1
            loser = card2
        else:
            winner = card2
            loser = card1

        winner.update_wins(1)
        loser.update_losses(1)

        self.matches_played += 1

        return {
            'winner': winner.card_id,
            'loser': loser.card_id,
            'winner_rating': winner.calculate_rating(),
            'loser_rating': loser.calculate_rating()
        }

    def get_leaderboard(self) -> list:
        leaderboard = []

        for card in self.registered_cards.values():
            leaderboard.append({
                'name': card.name,
                'card_id': card.card_id,
                'rating': card.calculate_rating(),
                'record': card.get_rank_info()['record']
            })

        return leaderboard

    def generate_tournament_report(self) -> dict:
        total_rating = sum(
            c.calculate_rating()
            for c in self.registered_cards.values()
        )
        avg_rating = total_rating // len(self.registered_cards)

        return {
            'total_cards': len(self.registered_cards),
            'matches_played': self.matches_played,
            'avg_rating': avg_rating,
            'platform_status': 'active'
        }
