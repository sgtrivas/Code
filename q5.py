#!/usr/bin/env python3
def Hex_to_Rgb (hex):
   
   """Function:
	 input: 6 digit hex code
	 output: RGB format"""
   h = hex.lstrip('#')
   return int(h[i:i+2], 16) for i in (0, 2, 4)

Hex_to_Rgb('#FF0508')

