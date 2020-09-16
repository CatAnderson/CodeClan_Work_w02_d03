import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer_1 = Customer("David", 50.00)

    def test_customer_has_name(self):
        self.assertEqual("David", self.customer_1.name)

    def test_customer_wallet_amount(self):
        self.assertEqual(50.00, self.customer_1.wallet)

    def test_number_of_drinks_customer_has_in_hand(self):
        self.assertEqual(0, len(self.customer_1.drinks_in_hand))

    