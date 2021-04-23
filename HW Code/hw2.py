'''
Created on February 20, 2021
@author:   Eleni Rotsides and Julio Lora
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Hw 2
'''
import sys
from cs115 import map, reduce, filter
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.

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

def combineLists(possWords,scorePoss):
    '''Takes a list of words and a list of its corresponding scores and combines
    their elements at the same index so that the new form is a list of
    [ [word, score] , .....] '''
    if possWords==[]:
        return []
    else:
        return [[possWords[0]]+[scorePoss[0]]]+combineLists(possWords[1:],scorePoss[1:])

def scoreList(Rack):
    '''Takes as input a Rack which is a list of lower-case letters and returns
    a list of all of the words in the global Dictionary that can be made from
    those letters and the score for each one'''
    return combineLists(possibleWords(Dictionary, Rack), scorePossible(Rack))

def compare(L):
    '''Compares the first score element in a list of word/score pairs to the second score
    element, and then slices the list until the largest word/score match is remaining'''
    if L[1:] == []:
        return L[0]
    if L[0][1] >= L[1][1]:
        return compare([L[0]] + L[2:])
    if L[0][1] < L[1][1]:
        return compare(L[1:])

def bestWord(Rack):
    ''' Takes as input a Rack and returns a list with two elements: the
    highest possible scoring word from that Rack followed by its score. Ties
    will be broken arbitrarily.'''
    result = scoreList(Rack)
    if result == []:
        return ['', 0]
    return compare(scoreList(Rack))

def ind(e, L):
    '''Returns the index where the element e is first found in L, a list or
    string. If e is not in L, then this function will return the length of L'''
    if L == [] or L == '':
        return 0
    elif e == L[0]:
        return 0
    else:
        return ind(e, L[1:]) + 1

#function that determines whether or not the given string can be made from Rack
def isPossible(S, Rack):
    '''Determines whether or not the given string S can be made from Rack.
    Returns True if it is possible, and false if it isn't.'''
    if S == '':
        return True
    elif Rack == []:
        return False
    elif S[0] not in Rack:
        return False
    else:
        return isPossible(S[1:], Rack[:ind(S[0], Rack)] + Rack[(ind(S[0], Rack)+1):]) 

#function that uses the above function to determine the list of all strings
#in the dictionary that can be made from the Rack
def possibleWords(wordList, Rack):
    '''Returns a list of all possible words from the Dictionary called dictionaryList,
    that can be made from a given list of letters called Rack'''
    return filter(lambda x: isPossible(x, Rack), wordList)

#function that scores those words from the above function
def scorePossible(Rack):
    '''Returns a list of scores that correspond to the words that can be made from the
    given Rack'''
    return map(lambda x: wordScore(x,scrabbleScores), possibleWords(Dictionary, Rack))
