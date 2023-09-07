#!/usr/bin/env python3

def triangle(base, character):
    count = base
    for i in range(1, base+1,2):
        
        myLine = (i * character).center(base," ")
        print(myLine)
        count-1   
    ans = count   
    #print (ans) 
    print(f"height: " , base-2 )
triangle(5,"&")

    
  
#def triangle1(base, character):
   


#triangle1(3,"X")