#!/usr/bin/env python3

mylist = []
for i in range(1,5050505,23):
    if i % 2 == 1:
       mylist.append(i)
#difference between the 2
print(sum(mylist))
#print(min(mylist))
#print(max(mylist))


