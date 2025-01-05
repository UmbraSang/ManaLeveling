import string

from Characters.Player import Player
from Enums.GearSlot import GearSlot


class Gear:

    name: string = None
    owner: Player = None
    weight = 0.0
    equipped = False
    slotType: GearSlot = None
    statBonus = {
        "STR": 0,
        "DEX": 0,
        "CON": 0,
        "INT": 0,
        "WIS": 0,
        "CHA": 0
    }
    bodyText: string = None

    def __init__(self, name, owner, weight, slotType, statBonus, bodyText):
        self.name = name
        self.owner = owner
        self. weight = weight
        self.slotType = slotType
        self.statBonus = statBonus
        self.bodyText = bodyText

    def awardGear(self, player):
        self.owner = player
        player.inventory.append(self)