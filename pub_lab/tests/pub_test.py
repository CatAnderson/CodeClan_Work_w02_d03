import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Ox", 100.00)
        self.drink_beer = Drink("Beer", 5.00)
        self.drink_wine = Drink("Wine", 6.00)
        self.drink_gnt = Drink("Gin & Tonic", 7.50)
        self.drink_rum = Drink("Rum", 5.50)
        self.drink_coke = Drink("Coke", 0.75)
        self.drink_lemonade = Drink("Lemonade", 0.65)
        self.pub.menu_of_drinks = [
            self.drink_beer,
            # put the other menu items in here
        ]


    def test_pub_has_name(self):
        self.assertEqual("Ox", self.pub.name)

    def test_pub_has_cash_in_till(self):
        self.assertEqual(100.00, self.pub.cash)
    
    def test_till_transaction__add(self):
        self.pub.till_transaction(5)
        self.assertEqual(105.00, self.pub.cash)

    def test_drink_has_been_added_to_menu(self):
        self.pub.add_drink(self.drink_beer)
        self.assertEqual(2, self.pub.drink_count())

    def test_drink_has_been_removed_from_menu(self):
        self.pub.remove_drink(self.drink_beer)
        self.assertEqual(0, self.pub.drink_count())

    def test_sell_drink_to_customer(self):
        self.customer_1 = Customer("David", 50.00)
        self.customer_1.add_drink_to_customer_hand(self.drink_beer)
        self.customer_1.alter_customer_wallet_amount(self.drink_beer.price)
        self.pub.till_transaction(self.drink_beer.price)
        self.pub.remove_drink(self.drink_beer)
        self.assertEqual(1, len(self.customer_1.drinks_in_hand))
        self.assertEqual(45, self.customer_1.wallet)
        self.assertEqual(105.00, self.pub.cash)
        self.assertEqual(0, self.pub.drink_count())
        





    # def test_drink_menu_length(self):
    #      self.assertEqual(6, len(self.drink.menu_of_drinks))
