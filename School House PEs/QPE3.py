def your_function(digits):
    return ''.join([' ', '', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ'][int(char[0])][char.count(char[0]) - 1]for char in digits.split())

print(your_function("44 33 555 555 666")) # "HELLO"
print(your_function("7 999 8 44 666 66 0 444 7777 0 222 666 666 555")) # "PYTHON IS COOL"
print(your_function("0")) # " "