#from Drink import *
#from Customer import *


class Pub:
    def __init__(self, name, cash_in_till):
        self.name = name
        self.cash = cash_in_till  

    def till_transaction(self, transaction_amount):
        self.cash += transaction_amount

    