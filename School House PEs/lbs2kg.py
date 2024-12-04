import pyinputplus as pyip

wt = pyip.inputFloat("Enter the weight in lbs to convert: ")
kg = wt / 2.205
print()
print(f"The weight in Kilograms is {kg:.2f}kgs")