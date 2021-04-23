from cs115 import *

'''
I pledge my honor that I have abided by the Stevens Honor System
Eleni Rotsides
'''

def mult(x, y):
    '''Returns the product of x and y'''
    return x * y

def factorial(n):
    '''Assuming n is a positive integer, this function returns the
    factorial of x'''
    return reduce(mult, range(1, n+1))

def add(x,y):
    '''Returns the sum of x and y'''
    return x + y

def mean(L):
    '''Takes a list, L, as input and returns the average value in that list'''
    return reduce(add, L) / len(L)

def divides(n):
    '''Returns a function that checks whether a number divides n''' 
    def div(k):
        return n % k == 0
    return div

def prime(n):
    '''Returns True or False, depending on whether or not the given positive
    integer, n, is prime or not'''
    if n == 1:
        return False
    return sum(map(divides(n), range(2,n))) == 0
