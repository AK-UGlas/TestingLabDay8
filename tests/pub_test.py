import unittest
from src.pub import *
from src.customer import Customer
from src.drink import Drink

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Black Bull", 200)
        self.customer = Customer("Jimmy", 50)

    def test_pub_has_name(self):
        self.assertEqual("The Black Bull", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(200, self.pub.till)