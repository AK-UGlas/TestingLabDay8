import unittest
from src.customer import Customer
from src.pub import Pub
from src.drink import Drink
from src.food import Food

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Jimmy", 50, 18)
        self.drink = Drink("St Mungo", 5.00, 20)
        self.food = Food("Mars Bar", 1.00, 10)

    def test_customer_has_name(self):
        self.assertEqual("Jimmy", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(50, self.customer.wallet)

    def test_customer_drunkenness(self):
        self.customer.drink(self.drink)
        self.assertEqual(20, self.customer.drunkenness)

    def test_customer_rejuvenated(self):
        self.customer.drunkenness = 20
        self.customer.eat_food(self.food)
        self.assertEqual(10, self.customer.drunkenness)


