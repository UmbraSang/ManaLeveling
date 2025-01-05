import string

from Characters.Player import Player


class Ability:

    name: string = None
    bodyText: string = None
    players: list[Player] = []

    def __init__(self, name, text):
        self.name = name
        self.bodyText = text

    def awardAbility(self, player):
        self.players.append(player)
        player.abilities.append(self)