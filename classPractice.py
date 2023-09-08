class Kettle(object):
    #everything describing a Kettle i.e. price, make(brand), etc.
    def __init__(self, make, price): #__init__ is a method
        self.make = make #<--attributes
        self.price = price
        self.on = False


    def switch_on(self):
        self.on = True


#attribute
kenwood = Kettle("Kenwood", 5.99)
print(kenwood.make)
print(f'${kenwood.price:.2f}')

hamilton = Kettle("Hamilton-Beech", 13.00)
print(hamilton.make)
print(f'${hamilton.price:.2f}')

print(f'Models: {kenwood.make} = ${kenwood.price:.2f}, {hamilton.make} = ${hamilton.price:.2f}')

"""
Class: a template for creating objects. All objects created using the same class will have the same characteristics.
Object: an instance of a class.
Instantiate: create an instance of a class.
Method: a function defined in a class.
Attribute: a variable bound to an instance of a class.
"""