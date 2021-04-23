'''
Created on March 20, 2021
@author:   Eleni Rotsides and Julio Lora
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - HW 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

def compress(S):
    '''Calls compressHelper and returns the correct result depending on
    what the first number is (a 0 or 1) so that it always adheres to the
    0 1 0 1 pattern.'''
    if(S[0] == '1'):
        return '0' * COMPRESSED_BLOCK_SIZE + compressHelper(S)
    return compressHelper(S)

'''
The largest number of bits that our comopress algorithm could possibly
use to encode a 64-bit string/image is 31, or whatever the MAX_RUN_LENGTH
variable equates to. In this case, its 31, but if it were to be changed to a
different value, then it would be the different value.
'''

def compressHelper(S):
    '''Takes a binary string S of length 64 as input and returns another binary
    string as ouput. The output binary string is a run-length-encoding of the
    input string.'''
    if S == '':
        return ''
    else:
        consec = count(S[0],S)
        binary = numToBinary(consec)
        goodVal = checkInput(binary)
        if consec > MAX_RUN_LENGTH:
            return goodVal + ('0' * COMPRESSED_BLOCK_SIZE) + compressHelper(S[MAX_RUN_LENGTH:])
        else:
            return goodVal + compressHelper(S[consec:])  

def checkInput(S):
    '''Ensures a binary number S is within the range of the MAX_RUN_LENGTH
    and if the string S is 5 digits long. Returns the proper value for input'''
    num = COMPRESSED_BLOCK_SIZE-len(S)
    if len(S) > 5:
        return numToBinary(MAX_RUN_LENGTH)
    if len(S) >= 0 and len(S) <= 5:
        return num * '0' + S

def uncompress(S):
    '''Calls uncompressHelper to undo the compression that the compress function returns'''
    return uncompressHelper(S, '0')

def uncompressHelper(S, num):
    '''Undoes the compression that the compress function returns'''
    if S == '':
        return ''
    nextNum = '0'
    if num == '0':
        nextNum = '1'
    return binaryToNum(S[:COMPRESSED_BLOCK_SIZE]) * num + uncompressHelper(S[COMPRESSED_BLOCK_SIZE:], nextNum)

def compression(S):
    '''Returns the ratio of the compressed size to the original size of the
    image S'''
    return len(compress(S)) / len(S)

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

'''
To test our functions, we ran some small tests to start so we can see how our functions
are behaving (for example: compress('000111') and compress('111000'). After we got our
functions working as intended, then we started using tests that exceeded the MAX_RUN_LENGTH
to see if this edge case is accounted for. The remaining tests were done by running the test
script that was provided. We also made sure to run the script after new tweaks were made when we
found another unaccounted for edge case, just to make sure our code still works, in addition to
testing the edge case.
'''


'''
Professor Lai isn't accounting for the case where the string/image is for example
'01010101' . The conversion will always be longer than the original input because the
number of consective bits is smaller than what the conversion would be, and if there's enough of those,
like in the above example, then the output will always be longer, and Professor Lai's algorithm is
faulty.
'''


def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    elif s[-1] == '0':
        return binaryToNum(s[:-1]) * 2
    elif s[-1] == '1':
        return binaryToNum(s[:-1]) * 2 + 1    
    
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return n % 2 == 1

def count(numStr, S):
    '''Returns the number of times S[0] exists consecutively'''
    if S == '':
        return 0
    if S[0] != numStr:
        return 0
    else:
        return 1 + count(numStr, S[1:])

