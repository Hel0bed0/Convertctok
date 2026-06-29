#!/usr/bin/env python3


 # Function that converts C to K
 
 #Loop Script
while True:
 
 # User Input
    n = float(input("Enter Celsius Value (will crash if NaN):  "))

    c = 1

 # Convert
    def CelsiusTokelvin (c):
        return n + 273.15

    y = CelsiusTokelvin (c)

    

 # Print Answer
    print (f"{n} Celsius is equal to {y} Kelvin\n"
           "Method: added 273.15\n")
 #ask to exit
    ex = int(input("1 to exit, other to not:  "))
    if ex == 1:
        break

