from Equipment.Gear import Gear


class Consumable(Gear):

    uses: int = 0
    duration: int = 0

    def __init__(self, name, owner, weight, slotType, statBonus, bodyText, uses, duration):
        super().__init__( name, owner, weight, slotType, statBonus, bodyText)
        self.uses = uses
        self.duration = duration