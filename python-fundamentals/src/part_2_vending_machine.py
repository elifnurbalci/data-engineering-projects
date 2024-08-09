class VendingMachine:

    def __init__(self):
        self.credit = 0
        self.stock = {'A': {}, 'B': {}, 'C': {}}

    def add_credit(self, amount):
        self.credit += amount

    def credit_checker(self, price):
        if self.credit >= price:
            return True
        else:
            return 
        
    def add_stock(self, item, row):
        if item == self.stock[row]:
            return "This item already exists, please add another one!"
        self.stock[row] = item
        return self.stock

    def purchase_item(self, row):
        if self.credit < self.stock[row]['price']:
            return "Insufficient credit!"
        else:
            self.credit -= self.stock[row]['price']
            self.stock[row]['quantity'] -= 1
            return self.stock[row]['name']
