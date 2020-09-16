import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink_beer = Drink("Beer", 5.00)
        self.drink_wine = Drink("Wine", 6.00)
        self.drink_gnt = Drink("Gin & Tonic", 7.50)
        self.drink_rum = Drink("Rum", 5.50)
        self.drink_coke = Drink("Coke", 0.75)
        self.drink_lemonade = Drink("Lemonade", 0.65)

    def test_drink_has_name_beer(self):
        self.assertEqual("Beer", self.drink_beer.name)

    def test_drink_has_name_wine(self):
        self.assertEqual("Wine", self.drink_wine.name)

    def test_drink_has_name_lemonade(self):
        self.assertEqual("Lemonade", self.drink_lemonade.name)   

    def test_drink_price_beer(self):
        self.assertEqual(5.00, self.drink_beer.price)




    