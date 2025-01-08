import string

from Characters import Hunter
from GameObjects import Party
from Loot import Loot


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