import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Ox", 100.00)        #Pub("Ox", 100.00) must have capital P for Pub because its the class Pub.

    def test_pub_has_name(self):
        self.assertEqual("Ox", self.pub.name)

    def test_pub_has_cash_in_till(self):
        self.assertEqual(100.00, self.pub.cash)
    
    def test_till_transaction__add(self):
        self.pub.till_transaction(5)
        self.assertEqual(105.00, self.pub.cash)

