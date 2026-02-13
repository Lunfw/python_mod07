from ex0.CreatureCard import CreatureCard
from ex0.Card import Card
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory
from sys import exit, stderr


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        try:
            return (CreatureCard(name_or_power, 2, 'Epic', 5, 10))
        except ValueError as e:
            print(f"Error creating creature card: {e}", file=stderr)
            exit(1)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        try:
            return (SpellCard(name_or_power, 3, "Epic", "Fire"))
        except ValueError as e:
            print(f"Error creating spell card: {e}", file=stderr)
            exit(1)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        try:
            return (ArtifactCard(name_or_power, 3, "Rare", 4, "Artifact"))
        except ValueError as e:
            print(f"Error creating artifact card: {e}", file=stderr)
            exit(1)

    def create_theme_deck(self, size: int) -> dict:
        try:
            for i in range(size):
                pass
        except ValueError as e:
            print(f"Error creating theme deck: {e}", file=stderr)
            exit(1)

    def get_supported_types(self) -> dict:
        return (
            {
                'creatures': ['dragon', 'goblin'],
                'spells': ['fireball'],
                'artifacts': ['mana_ring']
            }
        )
