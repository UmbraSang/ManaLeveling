import math
import string
from typing import Dict

from Enums.DamageMods import DamageMods
from Enums.Rank import Rank
from GameObjects.Ability import Ability


class Character:

    name: string = None
    stats = [0,0,0,0,0,0]
    abilities: list[Ability] = []
    currHealth: int = 0
    maxHealth: int = 0
    currMana: int = 0
    maxMana: int = 0
    AC: int = 0
    Speed = {} ###{"walk":0, "swim": 0, "climb": 0, "fly": 0, "dig":0}
    Initiative:int = 0
    profBonus: int = 0
    rank: Rank = None
    hitDice = [0,0,0,0,0,0]
    hitHP = [3,4,5,6,7,11]
    savingThrows = [0,0,0,0,0,0]
    skills = {}
    incomingDamageMods = {}
    weaponProf = {}
    armourProf = {}
    languages = []
    inventory = [] ###: Gear = []
    loadout =[] ###: list[Loadout] = []


    def __init__(self, name, stats, speeds, rank, hitDice, skills, damages, weapons, armours, languages):
        self.name = name
        self.stats = stats
        self.hitDice = hitDice
        self.updateHP()
        self.Speed = speeds
        self.rank = rank
        self.updateProfBonus()
        self.skills = skills
        self.incomingDamageMods = damages
        self.weaponProf = weapons
        self.armourProf = armours
        self.languages = languages


    def updateHP(self):
        y = 0
        z = 0
        for (a, b) in zip(self.hitDice, self.hitHP):
            y += a*b
            z += a
        self.maxHealth = y + z*self.stats[2]

    def updateProfBonus(self):
        if self.rank == Rank.E:
            self.profBonus = 1
        elif self.rank == Rank.D:
            self.profBonus = 2
        elif self.rank == Rank.C:
            self.profBonus = 3
        elif self.rank == Rank.B:
            self.profBonus = 5
        elif self.rank == Rank.A:
            self.profBonus = 6
        elif self.rank == Rank.S:
            self.profBonus = 8
        elif self.rank == Rank.NATIONAL:
            self.profBonus = 10
        elif self.rank == Rank.CELESTIAL:
            self.profBonus = 12

    def longRest(self):
        self.currMana = self.maxMana
        self.currHealth = self.maxHealth

    def addDamageMod(self, dmgType, mod):
        if mod == DamageMods.IMMUNE:
            self.incomingDamageMods.update({dmgType:mod})
        elif mod == DamageMods.RESISTANT:
            if self.incomingDamageMods[dmgType] == DamageMods.VULNERABLE:
                self.incomingDamageMods.pop(dmgType)
        elif mod == DamageMods.VULNERABLE:
            if self.incomingDamageMods[dmgType] == DamageMods.RESISTANT:
                self.incomingDamageMods.pop(dmgType)
