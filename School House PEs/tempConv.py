import pyfiglet as fig
import pyinputplus as pyip

ascii_banner = fig.figlet_format("DA TEMP CALC", font='cyberlarge')
print(ascii_banner)

temp = pyip.inputFloat("Enter the Temperature in Celcius: ")
Cel = temp
Far = (temp * 1.8) + 32
Kel = Cel + 273.15
print(f"The Following are your temperatures \n{Far:.1f} degrees Farenheit \n{Cel:.1f} degrees Celcius \n{Kel:.2f} degrees in Kelvin")