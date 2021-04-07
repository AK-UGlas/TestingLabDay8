import unittest
from src.customer import Customer
from src.pub import Pub
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Jimmy", 50)
        # self.pub = Pub("The Drunken Clam", 100.00)
        # self.drink1 = Drink("Guinness", 4.00)
        # self.drink2 = Drink("St Mungo", 5.00)
        # self.drink3 = Drink("Tennants", 1.50)
        # self.pub.drinks.append(drink1)
        # self.pub.drinks.append(drink2)
        # self.pub.drinks.append(drink3)

    def test_customer_has_name(self):
        self.assertEqual("Jimmy", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(50, self.customer.wallet)

    # def test_buy_drink(self):
    #     self.customer.buy_drink(self.pub, self.drink1)
    #     self.assertEqual(self.pub.till, 104)
    #     self.assertEqual(self.customer.wallet, 46)

