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

    
