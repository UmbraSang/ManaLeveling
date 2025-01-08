import math
from Enums.Rank import Rank
from GameObjects.Title import Title
from Characters.Hunter import Hunter


class Player(Hunter):

    exp: int = 0
    level: int = 0
    rankUpArr: list[int] = [1,3,6,11,16,21,30,41]

    spentStatPoints:int = 0
    totalStatPoints: int = 0
    statPointsPerLevel: int = 2
    statPointInterval: int = 2
    statPointIncrement: int = 1

    gold: int = 0

    titles = [] ###: list[Title] = []
    activeTitle: Title = None
    job = None

    quests = [] ###: list[Quest] = []
    activeQuest= None ###: Quest = None
    levelUpArray = []

    def __init__(self, name, stats, speeds, rank, hitDice, skills, damages, weapons, armours, languages, hClass):
        super().__init__(name, stats, speeds, rank, hitDice, skills, damages, weapons, armours, languages, hClass)
        standardLevelUpArr: list[int] = [0, 300, 900, 2700, 6500, 14000, 23000, 34000, 48000, 64000, 85000, 100000, 120000, 140000, 165000, 195000, 225000, 265000, 305000, 355000, 415000, 475000, 545000, 615000, 695000, 775000, 865000, 955000, 1050000, 1140000, 1240000, 1340000, 1450000, 1560000, 1680000, 1800000, 1930000, 2060000, 2200000, 2340000, 2490000, 2640000, 2800000, 2960000, 3130000, 3300000,3480000, 3660000, 3850000, 4040000]
        self.levelUpArray = standardLevelUpArr

    def levelUpCheck(self):
        if self.exp > self.levelUpArray[self.level]:
            for x in self.levelUpArray:
                if self.exp > x:
                    continue
                else:
                    self.level = self.levelUpArray.index(x)
                    self.levelUp()
                    break

    def getLevel(self):
        return self.level

    def gainXP(self, xpGained):
        self.exp += xpGained
        self.levelUpCheck()

    def gainStats(self, statGained):
        self.exp += statGained

    def gainGold(self, goldGained):
        self.gold += goldGained

    def calculateStatPoints(self):
        self.totalStatPoints = (self.level+1)*self.statPointsPerLevel

    def incrementStats(self):
        for x in self.stats:
            x += self.statPointIncrement

    def rankUP(self):
        rankNum = math.floor((math.sqrt(1+8*self.level)-1)/2)
        if rankNum > 8:
            rankNum = 8
        self.rank = Rank(rankNum)
        self.updateProfBonus()

    def levelUp(self):
        self.updateHP() ### set new HP
        self.calculateStatPoints() ### see if we add more statPoints
        self.incrementStats() ### add to all stat scores
        self.rankUP() ### update rank

    def getSpeeds(self):
        for x in self.Speed:
            print(x +": "+ str(self.Speed[x]))