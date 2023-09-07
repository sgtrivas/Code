#!/bin/usr/env python3

usrVal = input("enter binary value to convert: ")
binVal = int(usrVal, 2)
hexVal = hex(int(binVal))

#ascVal = chr()
print(f"Base10: {binVal}, Hex: {hexVal}") 