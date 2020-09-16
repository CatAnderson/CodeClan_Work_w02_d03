class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        self.drinks_in_hand = []

    def add_drink_to_customer_hand(self, drink):
        self.drinks_in_hand.append(drink)

    def alter_customer_wallet_amount(self, drink_price):
        self.wallet -= drink_price

    