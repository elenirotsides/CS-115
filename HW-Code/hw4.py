from cs115 import *

'''
Created on March 8, 2021
@author:   Eleni Rotsides
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - HW 4
'''

def addPasc(numList):
    '''Helper function for pascal_row that creates a new list of sums of
    adjacent terms in the original list.'''
    if numList == [numList[0]]:
        return []
    return [numList[0] + numList[1]] + addPasc(numList[1:])

def pascal_row(num):
    '''Returns a list of elements found in a certain row of Pascal’s Triangle.
    Takes an integer num as input (represents the row's number), and it is
    assumed that the input will always be non-negative.'''
    if num == 0:
        return [1]
    else:
        return [1] + addPasc(pascal_row(num - 1)) + [1]

def pascal_triangle(num):
    '''Takes as input a single integer num and returns a list of lists
    containing the values of all the rows up to and including row n.'''
    return map(pascal_row, range(num + 1))

def test_pascal_row():
    '''Test pascal_row, returns nothing if all tests pass'''
    assert pascal_row(0) == [1]
    assert pascal_row(1) == [1,1]
    assert pascal_row(5) == [1, 5, 10, 10, 5, 1]
    assert pascal_row(4) == [1, 4, 6, 4, 1]

def test_pascal_triangle():
    '''Test pascal_triangle, returns nothing if all tests pass'''
    assert pascal_triangle(0) == [[1]]
    assert pascal_triangle(1) == [[1], [1, 1]]
    assert pascal_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
    assert pascal_triangle(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
