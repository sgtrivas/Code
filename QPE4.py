def your_function(value, base):
    return int(value, base)
    '''
    valid_digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    value = value.upper()
    value10 = 0
    for digit in value:
        value10 *= base
        value10 += valid_digits.index(digit)
    return value10
    '''

print(your_function("655", 8)) # 429
print(your_function("1101", 2)) # 13
print(your_function("12201543", 11)) # 23354378