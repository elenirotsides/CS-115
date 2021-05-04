# nim template DNaumann (2018), for assignment nim_hw11.txt 

# Global variables used by several functions
piles = []         # list containing the current pile amounts
num_piles = 0      # number of piles, which should equal len(pile)

'''
Eleni Rotsides
I pledge my honor that I have abided by the Stevens Honor System.
'''

from cs115 import range

def play_nim():
    """ plays game of nim between user and computer; computer plays optimally """
    
    init_piles()
    display_piles()
    while True:
        user_plays()
        display_piles()
        if sum(piles) == 0:

            # TODO print a message telling the user they won
            print("Oh wow....you actually won. Good job, I guess.")
            break
        computer_plays()
        display_piles()
        if sum(piles) == 0:

            # TODO print a message telling the user the computer won
            print("I win...AGAIN HAHAHAHA BAZINGAAAA")

            break


def init_piles():
    """ Assign initial values to the global variables 'num_piles' and
        'piles'
        User chooses number of piles and initial size of each pile.
        Keep prompting until they enter valid values."""
    global piles
    global num_piles
    
    # TODO - Done
    num_piles = int(input("How many piles do you want to play with? "))

    while num_piles <= 0 or num_piles > 15:
        if num_piles <= 0:
            print("Sorry, the number of piles must be greater than 0.")
            num_piles = int(input("Please enter a new value: "))
        if num_piles > 15:
            print("Sorry, that number is too large.")
            num_piles = int(input("Please enter a number less than 16: "))
            
    piles = [0] *  num_piles
    
    for i in range(num_piles):
        
        piles[i] = int(input("How many in pile " + str(i) + "? "))
        while piles[i] <= 0 or piles[i] > 15:
            if piles[i] <= 0:
                print("Sorry, the number in that pile cannot be less than 1.")
                piles[i] = int(input("Please enter a new number for pile " + str(i) + ": "))
            if int(num) > 15:
                print("Sorry, the number in that pile cannot be greater than 15.")
                piles[i] = int(input("Please enter a new number for pile " + str(i) + ": "))
        
def display_piles():
    """ display current amount in each pile """
    global piles
    global num_piles

    # TODO - Done
    
    for i in range(num_piles):
        print("pile " + str(i) + " = " + str(piles[i]))


def user_plays():
    """ get user's choices and update chosen pile """
    global piles
    
    print("Your turn ...")
    p = get_pile()
    amt = get_number(p)
    piles[p] = piles[p] - amt


def get_pile():
    """ return user's choice of pile
        Keep prompting until the choice is valid, i.e.,
        in the range 0 to num_piles - 1. """
    global piles
    global num_piles

    # TODO - Done

    p = int(input("What pile? "))
    
    while p not in range(num_piles):
        p = int(input("That pile doesn't exist....pick another pile: "))
    while piles[p] == 0:
        p = int(input("Sorry, you can't pick from that pile. Please pick a different pile: "))
    return p


def get_number(pnum):
    """ return user's choice of how many to remove from pile 'pnum'
        Keep prompting until the amount is valid, i.e., at least 1
        and at most the amount in the pile."""
    global piles

    # TODO - Done

    numToRemove = int(input("How many? "))
    while numToRemove < 1 or numToRemove > piles[pnum]:
        print("Sorry, you can't remove that many.")
        numToRemove = int(input("Try again. How many? "))

    return numToRemove


def game_nim_sum():
    """ return the nim-sum of the piles """
    global piles
    # global num_piles 

    # TODO - Done

    pilesCopy = piles
    
    def helper(pilesCopy):
        '''recursively calculates the num-sum of the piles'''
        if pilesCopy == []:
            return 0
        else:
            return pilesCopy[0] ^ helper(pilesCopy[1:])
    
    return helper(pilesCopy)
    

def opt_play():
    """ Return (p,n) where p is the pile number and n is the amt to
        remove, if there is an optimal play.  Otherwise, (p,1) where
        is the pile number of a non-zero pile.

        Implement this using game_nim_sum() and following instructions
        in the homework text."""
    global piles
    global num_piles 

    # TODO - Done 

    nim_sum = game_nim_sum()
    
    pile_sums = []
    for i in range(num_piles):
        pile_sums += [(i,piles[i] - (piles[i] ^ nim_sum))]

    sorted_pile_sums = sorted(pile_sums, key=lambda x: x[1])

    def sort(sorted_pile_sums):
        '''reverses sorted_pile_sum list so the largest amount to be removed is first'''
        if sorted_pile_sums == []:
            return []
        else:
            return sort(sorted_pile_sums[1:]) + [sorted_pile_sums[0]]
    
    sort = sort(sorted_pile_sums)
    
    for i in range(num_piles):
        if sort[i][1] <= piles[sort[i][0]] and piles[sort[i][0]] > 0:
            return sort[i]
    for i in range(num_piles):
        if piles[sort[i][0]] > 0:
            return (sort[i][0], 1)


def computer_plays():
    """ compute optimal play, update chosen pile, and tell user what was played

        Implement this using opt_play(). """
    global piles
    global num_piles

    # TODO - Done

    pile_to_remove_from = opt_play()[0]
    opt_remove = opt_play()[1]

    piles[pile_to_remove_from] -= opt_remove

    print("My turn...prepare to be dazzled!!!")
    print("I remove " + str(opt_remove) + " from pile " + str(pile_to_remove_from))
    


#   start playing automatically
if __name__ == "__main__" : play_nim()
