import string

from Characters.Hunter import Hunter
from GameObjects.Party import Party
from Loot.Loot import Loot


class Guild:

    name: string = None
    leader: Hunter = None
    viceLeader: Hunter = None
    strikeTeam: Party = None
    guildMembers: Party = None
    GuildLoot: list[Loot] = []
    guildMoney = 0.0

    def __init__(self, name, lead, vice):
        self.name = name
        self.leader = lead
        self.viceLeader = vice

    def addMember(self, hunter):
        self.guildMembers.addMember(hunter)