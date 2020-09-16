import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer_1 = Customer("David", 50.00)
        self.drink_beer = Drink("Beer", 5.00)

    def test_customer_has_name(self):
        self.assertEqual("David", self.customer_1.name)

    def test_customer_wallet_amount(self):
        self.assertEqual(50.00, self.customer_1.wallet)

    def test_customer_age(self):
        self.assertEqual(20, self.customer_1.age)
        
    def test_number_of_drinks_customer_has_in_hand__isnone(self):
        self.assertEqual(0, len(self.customer_1.drinks_in_hand))

    def test_number_of_drinks_customer_has_in_hand__added_drink(self):
        self.customer_1.add_drink_to_customer_hand(self.drink_beer)
        self.assertEqual(1, len(self.customer_1.drinks_in_hand))

    def test_customer_has_paid_for_drink(self):
        self.customer_1.alter_customer_wallet_amount(self.drink_beer.price)
        self.assertEqual(45, self.customer_1.wallet)


