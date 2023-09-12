inString = ['This is exhausting. Python is frying my brain!']
#instring = sorted(inString, reverse=True)
#print(instring)
for item in inString:
    item.split(',')
    items = ''.join(sorted(set(item)))
    print(items)
   


