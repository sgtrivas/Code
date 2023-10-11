#!/usr/bin/env python3
def boxy(n,m):
    print('*' * m)
    for item in range(n-2):
        print('*' + (m-2)* ' ' + '*')
    print('*' * m)

n = int(input("How tall you want the box to be: "))
m = int(input("How wide do you want the box to be: "))
boxy(n,m)
