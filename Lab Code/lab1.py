from cs115 import *
import math

'''
I pledge my honor that I have abided by the Stevens Honor System
Eleni Rotsides
'''

def inverse(n):
    '''Takes a number n as input and returns its reciprocal'''
    return 1/n

def e(n):
    '''Approximates the mathematical value e using a Taylor expansion, assuming
    n is a positive integer'''
    return sum(map(inverse, map(math.factorial, range(1, n+1)))) + 1

def error(n):
    '''Returns the absolute value of the difference between the "actual"
    value of e and the approximation in the e(n) function, assuming that
    n terms (beyond the leading 1) are used.'''
    difference = math.e - e(n)
    return abs(difference)

    
