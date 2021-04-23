'''
Created on March 15, 2021
@author:   Eleni Rotsides
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Hw 5 (Rev. Oct 2020 by D.N.)
'''
from turtle import * # Needed for graphics

def sv_tree(trunk_length, levels):
    '''Described in the homework assignment.'''
    pencolor("cyan")
    pensize(8)
    if levels == 0:
        penup()
    else:
        forward(trunk_length)
        right(30)
        sv_tree(trunk_length/2, levels-1)
        pendown()
        left(60)
        sv_tree(trunk_length/2, levels-1)
        pendown()
        right(30)
        backward(trunk_length)
        
    
memo = {}
def fast_lucas(n):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''
    if n in memo:
        return memo[n]
    if n == 0:
        memo[n] = 2
        return 2
    if n == 1:
        memo[n] = 1
        return 1
    else:
        add = fast_lucas(n-1) + fast_lucas(n-2)
        memo[n] = add
        return add
        
    
def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    def fast_change_helper(amount, coins, memo):
        '''Does the job of fast_change, assuming coins is a tuple.'''
        if (amount, coins) in memo:
            return memo[(amount, coins)]
        if amount <= 0:
            return 0
        if coins == ():
            return float('inf')
    
        first = coins[0]
        rest = coins[1:]
    
        if first > amount:
            memo[(amount, coins)] = fast_change_helper(amount, rest, memo)
            return fast_change_helper(amount, rest, memo)
        if first == amount:
            memo[(amount, coins)] = 1
            return 1
        if first < amount:
            use = 1 + fast_change_helper(amount - first, coins, memo)
            lose = fast_change_helper(amount, rest, memo)
            minimum = min(use, lose)
            memo[(amount, coins)] = minimum
            return minimum
    

    # Call the helper. Note we converted the list to a tuple.
    return fast_change_helper(amount, tuple(coins), {})

# If you did this correctly, the results should be nearly instantaneous.
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))

# Should take a few seconds to draw a tree.
sv_tree(100, 4)
