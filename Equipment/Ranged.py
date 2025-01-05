from Equipment.Weapon import Weapon


class Ranged(Weapon):

    thrown = False
    distClose:int = 0
    distFar:int = 0

    def __init__(self, name, owner, weight, slotType, statBonus, bodyText, atkMod, dmgMod, dmgDice, dmgType, twohanded, thrown, dist1, dist2):
        super().__init__(name, owner, weight, slotType, statBonus, bodyText, atkMod, dmgMod, dmgDice, dmgType, twohanded)
        self.thrown = thrown
        self.distClose = dist1
        self.distFar = dist2