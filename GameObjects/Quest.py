import string

from Characters.Player import Player
from Enums.Rank import Rank


class Quest:

    name: string = None
    rank: Rank = None
    bodyText: string = None
    currCount: int = 0
    goalCount: int = 0
    expValue: int = 0
    statReward: int = 0
    goldReward: int = 0
    players: list[Player] = []

    def __init__(self, name, rank, text, goal, xp, statReward, gold):
        self.name = name
        self.rank = rank
        self.bodyText = text
        self.goalCount = goal
        self.expValue = xp
        self.statReward = statReward
        self.goldReward = gold

    def giveQuest(self, player):
        self.players.append(player)
        player.quests.append(self)

    def completeQuest(self, players):
        for curr in players:
            curr.gainXP(self.expValue)
            curr.gainStats(self.statReward)
            curr.gainGold(self.goldReward)
            self.players.remove(curr)
