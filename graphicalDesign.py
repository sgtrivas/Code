#!/usr/bin/env python3


def triangle(base, character):
    count = 0
    for i in range(1, base+1,2):
        
        myLine = (i * character).center(base," ")
        print(myLine)
        count+=1   
        
    print(f"height: " , count )
triangle(3,"X")
