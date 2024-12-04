#!/usr/bin/env python3
import pyinputplus as pyip

iterItem = pyip.inputStr(prompt="what do you word to repeat:> ")
#print(iterItem)

for i in iterItem:
    print (i + "\t\U00002620")

