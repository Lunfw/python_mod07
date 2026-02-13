from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory(CardFactory):
    def __init__(self):
        self.creatures_list = []
        self.spells_list = []
        self.artifacts_list = []

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        creatures_list = ['dragon', 'goblin', 'golem']
        for creature in name_or_power.split(', '):
            if creature in creatures_list:
                self.creatures_list.append(creature)
        return CreatureCard(name_or_power, 5, 'Legendary', 7, 3)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        spells_list = ['fire', 'ice', 'lightning', 'fireball']
        for spell in name_or_power.split(', '):
            if spell in spells_list:
                self.spells_list.append(spell)
        return SpellCard(name_or_power, 4, 'common', 'damage')

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        artifacts_list = ['rings', 'staffs', 'crystals', 'mana_ring']
        for artifact in name_or_power.split(', '):
            if artifact in artifacts_list:
                self.artifacts_list.append(artifact)
        return ArtifactCard(name_or_power, 3, 'Rare', 3, 'boost')

    def create_themed_deck(self, size: int) -> dict:
        pass

    def get_supported_types(self) -> dict:
        return {
            'creatures': self.creatures_list,
            'spells': self.spells_list,
            'artifacts': self.artifacts_list
        }
