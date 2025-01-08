from Equipment.Gear import Gear


class Loadout:
    owner = None ###: Player = None
    numAllowedHead: int = 1
    numAllowedNeck: int = 1
    numAllowedChest: int = 1
    numAllowedShoulder: int = 2
    numAllowedArm: int = 2
    numAllowedHand: int = 2
    numAllowedLegs: int = 1
    numAllowedBoots: int = 1
    numAllowedBelt: int = 1
    numAllowedRing: int = 10
    numAllowed: list[int] = []

    equipped: list[Gear] = []

    def __init__(self, player):
        self.owner = player
        player.loadout.append(self)
        self.numAllowed = [1,1,1,2,2,2,1,1,1,10]

    def editLoadout(self, newGear: list[Gear]):
        slotCount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for x in newGear:
            slotCount[x.slotType] +=1
        for (a, b) in zip(slotCount, self.numAllowed):
            if a > b:
                return 1
        self.equipped = newGear
        return 0