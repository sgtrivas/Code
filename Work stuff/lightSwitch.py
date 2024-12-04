class LightSwitch():
    def __init__(self):
        self.switchIsOn = False
        print(f"Welcome to the room. My status is {self.switchIsOn}")

    def turnOn(self):
        #  turn the switch on
        self.switchIsOn = True
        print("turnOn() method...I am on")
    
    def turnOff(self):
        #  turn the switch off
        self.switchIsOn = False
        print("turnOff() method...I am off")

    def show(self):
        #  added for testing
        print(f'show() method...My status is: {self.switchIsOn}')


#  'o' is a good way to label your objects!
oLightSwitch = LightSwitch()

# call the methods in the LightSwitch class with your newly created object!
oLightSwitch.show()
oLightSwitch.turnOn()
oLightSwitch.show()
oLightSwitch.turnOff()
oLightSwitch.show()
oLightSwitch.turnOn()
oLightSwitch.show()


