import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer_1 = Customer("David", 50.00)

    def test_customer_has_name(self):
        self.assertEqual("David", self.customer_1.name)
