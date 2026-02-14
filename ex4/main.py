from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main_exec():
    '''
        #   Main execution program.
    '''
    print('Registering Tournament Cards...\n')
    platform: TournamentPlatform = TournamentPlatform()
    dragon: TournamentCard = TournamentCard(
        'dragon_001',
        'Fire Dragon',
        'Creature',
        5,
        8,
        'Rare')
    wizard: TournamentCard = TournamentCard(
        'wizard_001',
        'Ice Wizard',
        'Creature',
        4,
        7,
        'Rare')
    wizard.base_rating = 1150
    platform.register_card(dragon)
    platform.register_card(wizard)

    print('Creating tournament match...\n')
    match_result = platform.create_match('dragon_001', 'wizard_001')
    print(
        f'Match result: {{"winner": "{match_result["winner"]}", '
        f'"loser": "{match_result["loser"]}"}}\n'
    )
    print(
        f'{{"winner_rating": {match_result["winner_rating"]}, '
        f'"loser_rating": {match_result["loser_rating"]}}}\n'
    )
    print('Tournament Leaderboard:')
    for entry in platform.get_leaderboard():
        print(
            f'{entry["name"]}. {entry["card_id"]} - '
            f'Rating: {entry["rating"]} ({entry["record"]})'
        )

    print('\nPlatform Report:')
    print(platform.generate_tournament_report())
    print('\n=== Tournament Platform Successfully Deployed! ===')


def main():
    '''
        #   Small main program.
    '''
    print('\n=== DataDeck Tournament Platform ===\n')
    main_exec()
    print('All abstract patterns working together harmoniously!')


if (__name__ == '__main__'):
    main()
