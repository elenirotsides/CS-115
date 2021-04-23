#
# life.py - Game of Life lab
#
# Name: Eleni Rotsides
# Pledge: I pledge my honor that I have abided by the Stevens Honor System
#

import random
import sys 

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row
    
def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A += [createOneRow(width)]
    return A 

def printBoard( A ):
    """
    this function prints the 2d list-of-  lists
    A without spaces (using sys.stdout.write)
    """
    for row in A:
        for col in row:
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )

def diagonalize(width,height):
    """ creates an empty board and then modifies it
    so that it has a diagonal strip of "on" cells.
    """
    A = createBoard( width, height )
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

def innerCells(w,h):
    '''Returns a 2D array of all live cells - with the value of 1 - except
    for a one-cell-wide border of empty cells (with the value of 0) around
    around the edge of the 2D array.'''
    A = createBoard(w,h)
    for row in range(1, h - 1 ):
        for col in range(1, w - 1):
            A[row][col] = 1
    return A

def randomCells(w,h):
    '''Returns an array of randomly-assigned 1's and 0's except that the outer
    edge of the array is still completely empty (all 0's) as in the case of
    innerCells.'''
    A = createBoard(w,h)
    for row in range(1, h - 1 ):
        for col in range(1, w - 1):
            A[row][col] = random.choice([0,1])
    return A

def copy(A):
    '''Returns a deep copy of the array A.'''
    copy = createBoard(len(A[0]), len(A))
    for row in range(len(A)):
        for col in range(len(A[0])):
            copy[row][col] = A[row][col]
    return copy

def innerReverse(A):
    '''Takes old array A and creates a new generation of the same shape
    and size. Returns a new array with cells not in the border flipped; so
    if it was a 0 it is now a 1, and vice versa.'''
    B = copy(A)
    for row in range(1, len(B) - 1):
        for col in range(1, len(B[0]) - 1):
            if B[row][col] == 1:
                B[row][col] = 0
            else:
                B[row][col] = 1
    return B

def next_life_generation(A):
    '''
    makes a copy of A and then advanced one
    generation of Conway's game of life within
    the *inner cells* of that copy.
    The outer edge always stays 0. 
    '''
    newA = copy(A)
    for row in range(1, len(newA) - 1):
        for col in range(1, len(newA[0]) - 1):
            if countNeighbors(row, col, A) < 2:
                newA[row][col] = 0
            if countNeighbors(row, col, A) > 3:
                newA[row][col] = 0
            if countNeighbors(row, col, A) == 3 and A[row][col] == 0:
                newA[row][col] = 1
    return newA

def countNeighbors(row, col, A):
    '''Returns the number of live neighbors for a cell in the board A at a
    particular row and col'''
    count = 0
    if A[row - 1][col] == 1:
        count += 1
    if A[row - 1][col - 1] == 1:
        count += 1
    if A[row - 1][col + 1] == 1:
        count += 1
    if A[row][col - 1] == 1:
        count += 1
    if A[row][col + 1] == 1:
        count += 1
    if A[row + 1][col - 1] == 1:
        count += 1
    if A[row + 1][col] == 1:
        count += 1
    if A[row + 1][col + 1] == 1:
        count += 1        
    return count
    
