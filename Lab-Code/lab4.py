from cs115 import *

'''
Created on March 3, 2021
@author:   Eleni Rotsides
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Lab 4
'''

def knapsack(capacity, itemList):
    '''Returns a list in the form [capacity, [itemList]] where itemList is
    a list of items that have the properties of weight and value, in the form
    [[itemweight, itemval], ...]. This list will house the maximum value and
    then the itemList will be the list of those items and their values. The
    list should only show data for items that satisfy the need to not exceed
    the capacity. Items cannot be reused either.'''
    #itemList = [itemweight, itemval]
    if capacity <= 0 or itemList == []:
        return [0,[]]

    first = itemList[0]
    rest = itemList[1:]

    if first[0] > capacity:
        return knapsack(capacity, rest)
    else:
        useFunc = knapsack(capacity - first[0], rest)
        use = [first[1] + useFunc[0], [first] + useFunc[1]]
        lose = knapsack(capacity, rest)
        if use[0] > lose[0]:
            return use
        return lose
    
