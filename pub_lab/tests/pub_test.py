import unittest
from src.pub import Pub
from src.drinks import Drinks
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Ox", 100.00)        #Pub("Ox", 100.00) must have capital P for Pub because its the class Pub.

    def test_pub_has_name(self):
        self.assertEqual("Ox", self.pub.name)

    

