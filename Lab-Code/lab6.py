'''
Created on March 18, 2021
@author:   Eleni Rotsides
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return n % 2 == 1
# L-> R Base 2 representation of 42: 101010
# Odd base 10 number least sig bit: 1, even: 0
# This completely changes the value of the number. Adding or removing
   # digits on the right offsets the number and changes its value. The power of
   # 2's will be different and therefore the value will differ.
# N is odd:        N is even:

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    elif isOdd(n):
        return numToBinary(int(n/2)) + str(1)
    else:
        return numToBinary(int(n/2)) + str(0)

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    elif s[-1] == '0':
        return binaryToNum(s[:-1]) * 2 
    else:
        return binaryToNum(s[:-1]) * 2 + 1

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    answer = numToBinary(binaryToNum(s) + 1)
    numToMultBy = 8 - len(answer)
    if numToMultBy < 0 and len(answer) > 8:
        cutoff = len(answer) - 8
        return answer[cutoff:]
    return numToMultBy * '0' + answer

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n < 0:
        pass
    else:
        print(s)
        return count(increment(s), n-1)

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    elif n % 3 == 0:
        return numToTernary(int(n/3)) + str(0)
    elif n % 3 == 1:
        return numToTernary(int(n/3)) + str(1)
    else:
        return numToTernary(int(n/3)) + str(2)

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    elif s[-1] == '0':
        return ternaryToNum(s[:-1]) * 3 
    elif s[-1] == '1':
        return ternaryToNum(s[:-1]) * 3 + 1
    else:
        return ternaryToNum(s[:-1]) * 3 + 2
