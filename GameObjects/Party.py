import string

from Characters.Hunter import Hunter
from Loot.Loot import Loot


class Party:

    name: string = None
    leader: Hunter = None
    members: list[Hunter] = []
    active = False
    partyLoot: list[Loot] = []

    def __init__(self, name, leader):
        self.name = name
        self.leader = leader
        self.active = True

    def addMember(self, player):
        self.members.append(player)

    def addLoot(self, loot):
        self.partyLoot.append(loot)