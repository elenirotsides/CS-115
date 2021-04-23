from cs115 import *

'''
I pledge my honor that I have abided by the Stevens Honor System
Eleni Rotsides
'''

def change(amount, coins):
    '''Amount is a non-negative integer indicating the amount of money to be made and
    coins is a list of coin values with 1 always being in the list when we first call
    the function. Returns a non-negative integer indicating the minimum number of coins
    required to make up the given amount.'''
    if amount <= 0:
        return 0
    if coins == []:
        return float('inf')
    
    first = coins[0]
    rest = coins[1:]
    
    if first > amount:
        return change(amount, rest)
    if first == amount:
        return 1
    if first < amount:
        use = 1 + change(amount - first, coins)
        lose = change(amount, rest)
        return min(use, lose)   
    
