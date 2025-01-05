from Equipment.Weapon import Weapon


class Melee(Weapon):

    reach: int = 0

    def __init__(self, name, owner, weight, slotType, statBonus, bodyText, atkMod, dmgMod, dmgDice, dmgType, twohanded, reach):
        super().__init__(name, owner, weight, slotType, statBonus, bodyText, atkMod, dmgMod, dmgDice, dmgType, twohanded)
        self.reach = reach
