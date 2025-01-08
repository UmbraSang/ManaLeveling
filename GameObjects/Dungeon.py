import string

from Characters.Monster import Monster
from Enums.Rank import Rank
from GameObjects.Party import Party
from Loot.Loot import Loot


class Dungeon:

    name: string = None
    rank: Rank = None
    boss: Monster = None
    encounters: list[Party] = []
    loot: list[Loot] = []

    def __init__(self, rank: Rank, boss: Monster, name = "",):
        if name == "":
            self.name = rank.name + "-Rank Dungeon"
        else:
            self.name = name
        self.rank = rank
        self.boss = boss
