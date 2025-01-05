from Characters.Character import Character


class Monster(Character):

    expValue: int = 0
    goldValue: int = 0

    def __init__(self, xpValue, goldValue, name, stats, speeds, rank, hitDice, skills, damages, weapons, armours, languages):
        super().__init__(name, stats, speeds, rank, hitDice, skills, damages, weapons, armours, languages)
        self.expValue = xpValue
        self.goldValue = goldValue