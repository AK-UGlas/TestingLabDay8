class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def add_money_to_till(self, amount):
        self.till += amount

    def add_drink_to_stock(self, drink):
        self.drinks.append(drink)    

    def sell_drink_to_customer(self, customer, drink):
        if customer.age >= 18:
            # take money from customer
            customer.buy_drink(drink)
            # add money to the pub till
            self.add_money_to_till(drink.price)

