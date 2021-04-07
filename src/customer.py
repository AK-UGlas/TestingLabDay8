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

    def eat_food(self, food):
        if self.drunkenness < food.rejuvenation_lvl:
            self.drunkenness = 0
        else:
            self.drunkenness -= food.rejuvenation_lvl

    def buy_food(self, food):
        self.wallet -= food.price
        