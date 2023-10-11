dict1 = {  "xxlx":"xx!xx",
    "xfx":"ExLx",
    "0":'xSx',
     "www.":"SxQxUxIxRxRx",
     "python.org":'xRxExT',
     "pickle rick":'ExC' }

#  The variable below is the dictionary being sorted by its keys. this is what will be used to extract the values.
val1 = sorted(dict1.items())
#  this is the long way to do it but it is the easiest way. if you notice the index(key) is the first number \ 
#  and the value is the second. they are all '1' because there is only one value. if you put two it will error out.
#  We also replace the string 'x' with nothing to remove the spaces 
print(val1)
val2 = val1[0][1].replace('x',''),val1[1][1].replace('x',''),val1[2][1].replace('x',''),val1[3][1].replace('x',''),val1[4][1].replace('x',''),val1[5][1].replace('x','')
#  finally we join the output together to get the flag!
print(''.join(val2))



