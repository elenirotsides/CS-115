from cs115 import *

'''
Eleni Rotsides
I pledge my honor that I have abided by the Stevens Honor System
'''

def numToBaseB(N,B):
    '''Calls numToBaseBHelper and also gets rid of a leading zero if there
    is one.'''
    answer = numToBaseBHelper(N,B)
    if answer[0] == '0':
        return answer[1:]
    else:
        return answer
    
def numToBaseBHelper(N,B):
    '''Takes as input a non-negative (0 or larger) integer N and a base B
    (between 2 and 10 inclusive) and returns a string representing the number
    N in base B.'''
    if N == 0:
        return '0'
    else:
        return numToBaseB(N//B,B) + str(N % B)

def baseBToNum(S,B):
    '''Takes as input a string S and a base B where S represents a number in
    base B where B is between 2 and 10 inclusive. Returns an integer in
    base 10 representing the same number as S.'''
    if S == '':
        return 0
    else:
        return baseBToNum(S[:-1], B) * B + int(S[-1])
    
def baseToBase(B1,B2,SinB1):
    '''Takes three inputs: a baseB1, a baseB2 (both of which are between 2 and
    10, inclusive) and SinB1, which is a string representing a number in
    base B1. baseToBaseshould return a string representing the same number in
    base B2.'''
    return numToBaseB(baseBToNum(SinB1, B1), B2)

def add(S,T):
    '''That takes two binary strings S and T as input and returns their sum,
    also in binary'''
    return numToBaseB(baseBToNum(S, 2) + baseBToNum(T, 2), 2)

FullAdder = \
{ ('0','0','0') : ('0','0'),
  ('0','0','1') : ('1','0'),
  ('0','1','0') : ('1','0'),
  ('0','1','1') : ('0','1'),
  ('1','0','0') : ('1','0'),
  ('1','0','1') : ('0','1'),
  ('1','1','0') : ('0','1'),
  ('1','1','1') : ('1','1') }

def addB(S1,S2):
    '''Takes two strings as input, S1 and S2. These strings are the
    representations of binary numbers. Returns a new string representing
    the sum of the two input strings using binary addition, not base
    conversions.'''
    pass
