﻿import math

def linear_equations(a,b):
    if a == 0:
        if b == 0:
            #0x = 0  -- for every x
            return []
        else :
            #0x = -b  -- no solution
            return math.nan
    else:
        return -b / a

a = int(input("Въведете число за а: "))
b = int(input("Въведете число за b: "))

result =  linear_equations(a, b)

print("Резултатът е: ", result)
