a = 1000
b = "Hello"
c = 0b110010011
d = 90
e = 3.14159
f = 0x3f
g = .5

print(f"{a:b}")
print(f"{d:c}") #  Converts to unicode character
print(f"{c:d}") #  Converts number to base 10 decimal
print(f"{f:d}") #  converts to base 10 decimal. In this case it was a hex value
print(f"{a:x}") #  Converts to Hex
print(f"{e:.2f}") #  this will show 2 digits after the decimal
print(f"{g:%}") #  This will display a value with the percentage sign.
print(f"{g:.2%}")