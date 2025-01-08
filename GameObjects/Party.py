import string

from Characters import Character
from Loot import Loot


class Party:

    name: string = None
    leader: Character = None
    members: list[Character] = []
    active = False
    partyLoot: list[Loot] = []

    def __init__(self, name, leader):
        self.name = name
        self.leader = leader
        self.active = True

    def addMember(self, newMember):
        self.members.append(newMember)

    def addLoot(self, loot):
        self.partyLoot.append(loot)