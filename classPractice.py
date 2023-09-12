class Kettle(object):
    #everything describing a Kettle i.e. price, make(brand), etc.
    #class attribute that all instances will share
    power_source  = "electricity"

    def __init__(self, make, price): #__init__ is a contructor method
        self.make = make #<--attributes
        self.price = price
        #self.power = power
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

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

Kettle.switch_on(kenwood)
print(kenwood.on)
kenwood.switch_on()

print ("*" * 80)

kenwood.power = 1.5 
print(kenwood.power)
#print(hamilton.power)

print("Switch to atomic power")
Kettle.power_source = "atomic"
#using class attributes ONLY EXISTS IN THIS CLASS
#all 3 are sharing the power_source class attribute
print(Kettle.power_source)
print("Switch kenwood to gas")
#this didnt change the class attribute because its consiered a local variable.
kenwood.power_source = "gas"
print(kenwood.power_source)
print(hamilton.power_source)

print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)