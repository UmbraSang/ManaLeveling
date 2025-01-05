from Equipment.Gear import Gear


class Armour(Gear):

    ACMod: int = 0
    savingThrowMod: list[int] = [0,0,0,0,0,0]

    def __init__(self, name, owner, weight, slotType, statBonus, bodyText, ac, saving):
        super().__init__(name, owner, weight, slotType, statBonus, bodyText)
        self.ACMod = ac
        self.savingThrowMod = saving