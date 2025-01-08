import json
from Characters.Hunter import Hunter
from Characters.Player import Player
from Enums.HunterClass import HunterClass
from Enums.Rank import Rank
from GameObjects.Party import Party

testPlayer = Player(
    "Shantal",
    [6,6,6,6,6,6],
    {"walking": 30},
    Rank.E,
    [2,0,0,0,0,0],
    {"stealth": 2},
    {},
    {},
    {},
    ["English"],
    HunterClass.TANK)
party = Party("Beasts", testPlayer)

print("The Party "+ party.name +" is lead by "+ party.leader.name +" the "+ party.leader.rank.name +" Rank "+ party.leader.hunterClass.name)
print(party.leader.name +" is level "+ str(party.leader.getLevel()))
print("Add 50000xp")
testPlayer.gainXP(50000)
print(party.leader.name +" is level "+ str(party.leader.getLevel()) +". Her profBonus is now "+ str(party.leader.profBonus) +" and her rank is now "+ party.leader.rank.name)
print(testPlayer.getSpeeds())

### Load from JSON

#with open('hunters.json', 'r') as file:
#    data = json.load(file)