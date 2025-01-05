from Loot.Loot import Loot


class ManaCrystals(Loot):

    manaValue = 0.0

    def __init__(self, cash, count, gold, mana):
        super().__init__(cash, count, gold)
        self.manaValue = mana