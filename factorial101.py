# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 02:36:44 2016

@author: pamitto
"""

# factorial 2! = 2x1; 3!=3x2x1; 4!=4x3x2x1; n!=nxn-1xn-2x...n-(n-1)
def fact(n):
    if n < 0:
        raise RuntimeError ("Factorial undefined for negative values")
    elif n == 0:
        return 1
    else:    
        num = n
        for i in xrange(1, n):
            num *= (n-i)      
        return num

print fact(0)
