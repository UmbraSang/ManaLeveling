from GameObjects.Ability import Ability
from Loot.Loot import Loot


class RuneStones(Loot):
    skill: Ability = None

    def __init__(self, cash, count, gold, skill):
        super().__init__(cash, count, gold)
        self.skill = skill