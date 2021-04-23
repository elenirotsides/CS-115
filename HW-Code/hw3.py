from cs115 import *

'''
Created on February 28, 2021
@author:   Eleni Rotsides
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Hw 3
'''
# Be sure to submit hw3.py.  Remove the '_template' from the file name.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# your code goes here
def giveChange(amount, coins):
    '''Returns a list whose first item is the minimum number of coins needed to give change and
    whose second item is a list of the coins in that optimal solution'''
    if amount <= 0:
        return [0, []]
    if coins == []:
        return [float('inf'), []]
    
    first = coins[0]
    rest = coins[1:]
    
    if first > amount:
        return giveChange(amount, rest)
    if first == amount:
        return [1, [amount]]
    if first < amount:
        useFunc = giveChange(amount - first, coins)
        use = [1 + useFunc[0], useFunc[1] + [first]]
        lose = giveChange(amount, rest)
        if use[0] > lose[0]:
            return lose
        return use

def giveChangeTest():
    '''Tests the giveChange function. Should return nothing if it is working properly.
    will return an error otherwise.'''
    assert (giveChange(0, [1, 3, 16, 30, 50]) == [0, []])
    assert (giveChange(35, []) == [float('inf'), []])
    assert (giveChange(35, [35, 3, 16, 30, 50]) == [1, [35]])
    assert (giveChange(48, [1, 5, 10, 25, 50]) == [6, [25, 10, 10, 1, 1, 1]])

# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
' Hints: Use map. Feel free to use some of the functions you did for
' homework 2 (Scrabble Scoring). As always, include any helper
' functions in this file, so we can test it.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def letterScore(letter, scorelist):
    '''Takes a single letter string called letter and a list called scorelist
    where each element in that list is itself a list of the form
    [character, value] where character is a single letter and value is a number
    assoicated with that letter (a scrabble score). This function returns a
    single number which is the value associated with the letter given.'''
    if letter == scorelist[0][0]:
        return scorelist[0][1]
    else:
        return letterScore(letter, scorelist[1:])

def wordScore(S, scorelist):
    '''Takes a string S, and a list of lowercase letters and their allocated
    score called scorelist, and then returns the total score for that string
    based on the values indicated in scorelist'''
    if S == '':
        return 0
    else:
        return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)

def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    if dct == []:
        return []
    else:
        return map(lambda x: [x, wordScore(x, scores)], dct)



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
' (Notice that you cannot assume anything about the length of the list.)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n], assuming L is a list and n is at least 0.'''
    if n == 0 or L == []:
        return [] 
    else:
        return [L[0]] + take(n-1, L[1:])



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:], assuming L is a list and n is at least 0.'''
    if n == 0:
        return L
    if L == []:
        return []
    else:
        return drop(n-1, L[1:])
    


