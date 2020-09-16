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

    #def number_of_available_drinks(self):




    