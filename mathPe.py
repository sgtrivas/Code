""" Information on the math module and pyinputplus can be found on docs.python.org/3"""
#  import math and call it m to shorten it
import math as m
#  import pyinputplus for input validation since we are using integers.
import pyinputplus as pyip

#  creating a function and called it facto to find the factorial of a number. facto will accept one value
def facto(x):
    #  taking the variable of 'x' and assigning it the the math function 'factorial' which does the work for us.
    x = m.factorial(x)
    #  returning the result to the user.
    return x

#  takin a number, an integer, from the user to get the Factorial from
numBer = pyip.inputInt("Enter a number to get the Factorial of: ")
#  passing the users input to our facto function.
ans = facto(numBer)
#  printing our answer
print(f"The factorial of {numBer} is: {ans}")
