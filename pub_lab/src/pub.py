from Drink import *
#from Customer import *


class Pub:
    def __init__(self, name, cash_in_till):
        self.name = name
        self.cash = cash_in_till
        self.menu_of_drinks = []  
        
    def add_drink(self, name_of_drink):
        self.menu_of_drinks.append(name_of_drink)
        

    def till_transaction(self, transaction_amount):
        self.cash += transaction_amount

    
    def drink_count(self):
        return len(self.list_of_drinks)

    