#Create a simple tip calculator. So GET the BILL amt, GET Tip rate, Calculate both, Display totals

'''print("How much was the bill? ","\n")
print("How much tip percentage would you like to leave? ","\n")
print("The total bill was $","\n")
print("The total tip is $","\n")
print("The new total including tip is $","\n")'''


bill = int(input("How much was the bill? "))
tip = int(input("How much tip percentage would you like to leave? "))
tip2 = float(tip)/100
total = bill * float(tip2)
total2 = bill + total
print("\n")
print(f"The total bill was ${bill}\n")
print(f"The total tip amount is ${total}\n") 
print(f"The new total including tip is ${total2}\n")

