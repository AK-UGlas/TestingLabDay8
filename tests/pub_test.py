import unittest
from src.pub import *
from src.customer import Customer
from src.drink import Drink

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Black Bull", 200)
        self.customer = Customer("Jimmy", 50, 18)
        self.customer_2 = Customer("Paula", 100, 16)
        self.drink = Drink("Jimmy's Lager", 1.50, 20)
        self.drink_2 = Drink("Pineapple Juice", 2, 0)

    def test_pub_has_name(self):
        self.assertEqual("The Black Bull", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(200, self.pub.till)

    def test_sell_drink_to_customer(self):
        self.pub.sell_drink_to_customer(self.customer, self.drink)
        self.assertEqual(self.pub.till, 201.50)
        self.assertEqual(self.customer.wallet, 48.5)

    def test_check_customer_age(self):
        self.pub.sell_drink_to_customer(self.customer_2, self.drink)
        self.assertEqual(self.pub.till, 200.00)
        self.assertEqual(self.customer_2.wallet, 100)

    def test_reject_customer(self):
        self.customer.drunkenness = 90
        self.assertEqual(self.pub.reject_customer(self.customer), False)
    
    def test_add_drink_to_pub(self):
        self.pub.add_drink_to_stock(self.drink, 5)
        self.assertEqual(len(self.pub.drinks), 1)
        self.assertEqual(5, self.pub.stock[self.drink.name])

    def test_stock_value(self):
        self.pub.add_drink_to_stock(self.drink_2, 10)
        self.pub.add_drink_to_stock(self.drink, 5)
        self.assertEqual(self.pub.stock_value(), 27.5)
    
