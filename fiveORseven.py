#!usr/bin/env python3
bad = 35
myList = []
myList2 = []

for i in range(0, 5000, 5):
        if i%bad != 0:
             myList.append(i)
    

for i in range(0,5000,7):
    if i%bad!=0:
          myList2.append(i)

ansSum = sum(myList2) + sum(myList)
print(ansSum)