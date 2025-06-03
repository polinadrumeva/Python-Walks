import math

def linear_equations(a,b):
    if a == 0:
        if b == 0:
            return []
        else :
            return math.nan
    else:
        return -b / a


