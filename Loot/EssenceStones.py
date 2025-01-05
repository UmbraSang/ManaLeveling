from Enums.Rank import Rank
from Loot.Loot import Loot


class EssenceStones(Loot):

    rank: Rank = None

    def __init__(self, cash, count, gold, rank):
        super().__init__(cash, count, gold)
        self.rank = rank