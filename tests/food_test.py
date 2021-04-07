import unittest
from src.food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food("Pork Scratchings", 1.00, 10)

    def test_food_has_name(self):
        self.assertEqual("Pork Scratchings", self.food.name)

    def test_food_has_price(self):
        self.assertEqual(1.00, self.food.price)

    def test_food_has_rejuvenation_lvl(self):
        self.assertEqual(10, self.food.rejuvenation_lvl)

