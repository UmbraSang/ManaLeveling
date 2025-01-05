from Characters.Monster import Monster
from Loot.Loot import Loot


class MonsterCorpses(Loot):
    corpses: list[Monster] = []

    def __init__(self, cash, count, gold, monster):
        super().__init__(cash, count, gold)
        self.corpses.append(monster)