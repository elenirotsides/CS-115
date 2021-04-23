from cs115 import *

'''
I pledge my honor that I have abided by the Stevens Honor System
Eleni Rotsides
'''

def mult(x,y):
    '''Returns the product of x and y'''
    return x * y

def dot(L, K):
    '''Returns the dot product of integer lists L and K'''
    if L == [] or K == []:
        return 0
    else:
        return mult(L[0], K[0]) + dot(L[1:], K[1:])

def explode(S):
    '''Returns a list of the characters (each of which is a string of length 1)
    in the string S'''
    if S == '':
        return []
    else:
        return [S[0]] + explode(S[1:])
    
def ind(e, L):
    '''Returns the index where the element e is first found in L, a list or
    string. If e is not in L, then this function will return the length of L'''
    if L == [] or L == '':
        return 0
    elif e == L[0]:
        return 0
    else:
        return ind(e, L[1:]) + 1

def removeAll(e, L):
    '''Returns a list that is idential to L, but with all elements e removed'''
    if L == []:
        return []
    elif e == L[0]:
        return removeAll(e, L[1:])
    else:
        return [L[0]] + removeAll(e, L[1:])

def even(X):
    '''Returns True if X is even, or False if it isn't'''
    if X % 2 == 0 :
        return True
    else:
        return False

def myFilter(f, L):
    '''F is a function that returns either True or False, aka a predicate.
    This function returns a new list that contains all of the elements of L
    for which the predicate returns True'''
    if L == []:
        return []
    elif f(L[0]) == False:
        return myFilter(f, L[1:])
    else:
        return [L[0]] + myFilter(f, L[1:])
    
def deepReverse(L):
    '''Returns the reversal of the list L, including elements that may be lists
    themselves'''
    if L == []:
        return []
    elif isinstance(L[-1], list):
        return [deepReverse(L[-1])] + deepReverse(L[:-1])
    else:
        return [L[-1]] + deepReverse(L[:-1])
