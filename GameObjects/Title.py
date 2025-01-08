import string

from Characters import Player


class Title:

    name: string = None
    bodyText: string = None
    players: list[Player]

    def __init__(self, name, text):
        self.name = name
        self.bodyText = text

    def awardTitle(self, player):
        self.players.append(player)
        player.titles.append(self)