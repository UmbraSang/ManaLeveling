from Enums import DamageType
from Equipment import Gear


class Weapon(Gear):

    atkMod: int = 0
    dmgMod: int = 0
    dmgDice: list[int] = [0,0,0,0,0,0]
    dmgType: DamageType = None
    twoHanded = False

    def __init__(self, name, owner, weight, slotType, statBonus, bodyText, atkMod, dmgMod, dmgDice, dmgType, twohanded):
        super().__init__(self, name, owner, weight, slotType, statBonus, bodyText)
        self.atkMod = atkMod
        self.dmgMod = dmgMod
        self.dmgDice = dmgDice
        self.dmgType = dmgType
        self.twoHanded = twohanded