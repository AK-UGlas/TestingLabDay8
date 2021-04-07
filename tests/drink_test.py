import unittest
from src.drink import *
from src.customer import Customer
from src.pub import Pub

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Jimmy's Lager", 1.50, 20)
        
    def test_drink_has_name(self):
        self.assertEqual("Jimmy's Lager", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(1.50, self.drink.price)