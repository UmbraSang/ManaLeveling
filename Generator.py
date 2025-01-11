import math
import random

from Characters.Hunter import Hunter
from Enums.HunterClass import HunterClass
from Enums.Rank import Rank
from GameObjects.Party import Party


def roll3d4drop1():
    score = []
    for x in range(3):
        score.append(random.randint(1,4))
    score.remove(min(score))
    return sum(score)


def genSpeedArray(rank):
    speedMod = 1
    if rank.value < 3:
        speedMod = 1
    elif rank.value < 5:
        speedMod = 2
    elif rank.value < 7:
        speedMod = 4
    elif rank.value < 9:
        speedMod = 6
    minSpeed = 0
    maxSpeed = speedMod*20
    tempArray = {
        "Walking": random.randint(minSpeed, maxSpeed),
        "Swimming": random.randint(minSpeed, maxSpeed),
        "Climbing": random.randint(minSpeed, maxSpeed),
        "Dig": random.randint(minSpeed, maxSpeed),
    }
    if rank.value>5:
        tempArray.update({"Fly": random.randint(minSpeed, maxSpeed)})
    return tempArray


def genStatArray(rank):
    tempArray = []
    for x in range(6):
        tempArray.append(roll3d4drop1()*rank.value)
    return tempArray


def genHitDice(rank):
    tempArray = [0,0,0,0,0,0]
    for x in range(math.ceil(rank.value*(rank.value+1)/2)):
        tempArray[random.randint(0,5)] += 1
    return tempArray


def genSkills():
    pass


class Generator:

    def genHunter(self, gender, rank):
        pass

    def genMonster(self):
        pass

    def genHunterParty(self, num, minRank: Rank, maxRank: Rank):
        squad = []

        for x in num:
            tempRank = Rank(random.randint(minRank.value, maxRank.value))
            tempClass = HunterClass(random.randint(1,6))
            squad.append(Hunter(self.humanName(), genStatArray(tempRank), genSpeedArray(tempRank), tempRank, genHitDice(tempRank), genSkills(), genDamageMods(), genWeapons(), genArmour(), ["English"], ))
            pass
        return Party(self.partyName(), )

    def genMonsterParty(self, num):
        pass

    def genDungeon(self):
        pass

    def humanName(self):
        pass

    def partyName(self):
        pass

    def monsterName(self):
        pass

