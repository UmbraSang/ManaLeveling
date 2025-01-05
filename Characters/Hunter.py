from Character import Character
from Enums.HunterClass import HunterClass
from GameObjects.Guild import Guild
from GameObjects.Party import Party
from Loot.Loot import Loot


class Hunter(Character):

    hunterClass: HunterClass = None
    guild: Guild = None
    wealth = {}
    currParty: Party = None
    hunterLoot: list[Loot] = []

    def __init__(self, name, stats, speeds, rank, hitDice, skills, damages, weapons, armours, languages, hClass):
        super().__init__(name, stats, speeds, rank, hitDice, skills, damages, weapons, armours, languages)
        self.hunterClass = hClass

    def joinGuild(self, guild):
        self.guild = guild
        guild.addMember(self)

    def getLoot(self, loot):
        self.hunterLoot.append(loot)
