
'''
O: Open/Closed Principle

Software entities (classes, modules, functions, etc) should be open for extension, but closed for modification.

The base (or abstract) class is closed for modification and we implement concrete subclasses in order to modify their behaviour. 
'''


class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
            return self.price * 0.2

class DiscountVIP(Discount):
    def give_discount(self):
            return super().give_discount * 0.2

class SuperVIPDscount(DiscountVIP):
    def give_discount(self):
        return super().give_discount * 0.2
#----------->