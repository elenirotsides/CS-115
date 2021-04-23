# mandelbrot.py
# Lab 9
#
# Name: Eleni Rotsides
#
# I pledge my honor that I have abided by the Stevens Honor System
#

# keep this import line...
from cs5png import PNGImage
from cs115 import *

# start your Lab 9 functions here:

def mult(c,n):
    '''Returns the product of c times n without using multiplication.
    Uses only a loop and addition to multiply c by the integer n '''
    result = 0
    for x in range(n):
        result = result + c

    return result

def update(c,n):
    '''update starts with z=0 and runs z = z**2 + c
       for a total of n times. It returns the final z.'''
    z = 0
    for x in range(n):
        z = z**2 + c
        
    return z

def inMSet(c,n):
    '''Takes as input a complex number c and integer n. Returns a Boolean
    True if the complex number c is in the Mandelbrot set and False otherwise.
    Takes in c for the update step of z = z**2 + c
    n, the maximum number of times to run that step.
    Will return False as soon as abs(z) gets larger than 2
    Will return True if abs(x) never gets larger than 2 (for n iterations)'''
    z = 0
    for x in range(n):
        if abs(z) > 2:
            return False
        z = z**2 + c
        
    return True
    
