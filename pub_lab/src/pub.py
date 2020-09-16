from src.drink import Drink
#from src.customer import Customer


class Pub:
    def __init__(self, name, cash_in_till):
        self.name = name
        self.cash = cash_in_till
        self.menu_of_drinks = []  
        

    def till_transaction(self, transaction_amount):
        self.cash += transaction_amount

    
    def add_drink(self, drink):
        self.menu_of_drinks.append(drink)

    
    def remove_drink(self, drink):
        self.menu_of_drinks.remove(drink)



    def drink_count(self):
        return len(self.menu_of_drinks)

    