from Equipment.Armour import Armour


class Trinket(Armour):

    def __init__(self, name, owner, weight, slotType, statBonus, bodyText, ac, saving):
        super().__init__(name, owner, weight, slotType, statBonus, bodyText, ac, saving)