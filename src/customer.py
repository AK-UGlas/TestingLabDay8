class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = 0

    def buy_drink(self, drink):
        self.wallet -= drink.price

    def drink(self, drink):
        self.drunkenness += drink.alcohol_lvl
        