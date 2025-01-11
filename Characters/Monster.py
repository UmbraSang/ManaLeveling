import string

from Characters.Character import Character
from Enums.MonsterType import MonsterType


class Monster(Character):

    expValue: int = 0
    goldValue: int = 0
    tags: list[string] = []
    monsterType: MonsterType = None

    def __init__(self, xpValue, goldValue, name, stats, speeds, rank, hitDice, skills, damages, weapons, armours, languages, tags, typing):
        super().__init__(name, stats, speeds, rank, hitDice, skills, damages, weapons, armours, languages)
        self.expValue = xpValue
        self.goldValue = goldValue
        self.tags = tags
        self.monsterType = typing