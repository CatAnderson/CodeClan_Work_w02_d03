class Drink:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.list_of_drinks = []

    def drink_count(self):
        return len(self.list_of_drinks) 

    #def add_drink_to_list_of_drinks(self, name):
    #    self.list_of_drinks.append(name)


    
