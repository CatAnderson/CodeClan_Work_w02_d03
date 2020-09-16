import unittest
from src.pub import Pub
from src.drinks import Drinks
from src.customer import Customer

class TestDrinks(unittest.TestCase):
    def setUp(self):
        self.drinks_beer = Drinks("Beer", 5.00)
        self.drinks_wine = Drinks("Wine", 6.00)
        self.drinks_gnt = Drinks("Gin & Tonic", 7.50)
        self.drinks_rum = Drinks("Rum", 5.50)
        self.drinks_coke = Drinks("Coke", 0.75)
        self.drinks_lemonade = Drinks("Lemonade", 0.65)

    def number_of_available_drinks(self):
        



    