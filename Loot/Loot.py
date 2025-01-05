class Loot:

    moneyValue = 0.0
    amount: int = 0
    shopValue: int = 0

    def __init__(self, cash, count, gold):
        self.moneyValue = cash
        self.amount = count
        self.shopValue = gold