'''
Created on April 29, 2021
@author:   Eleni Rotsides
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Hw 12 - Date class
'''
from cs115 import range

DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    def __repr__(self):
        '''This method also returns a string representation for the object.'''
        return self.__str__()

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False

    def copy(self):
        '''Returns a new object with the same month, day, year
        as the calling object (self).'''
        dnew = Date(self.month, self.day, self.year)
        return dnew

    def equals(self, d2):
        '''Decides if self and d2 represent the same calendar date,
        whether or not they are the in the same place in memory.'''
        return self.year == d2.year and self.month == d2.month and \
           self.day == d2.day

    def tomorrow(self):
        '''Will change the calling object so that it represents one calendar
        day after the date it originally represented. Does not return anything.
        '''
        if self.day == DAYS_IN_MONTH[12] and self.month == 12:
            self.day = 1
            self.month = 1
            self.year = self.year + 1
        elif self.month == 2 and self.isLeapYear():
            if self.day == 28:
                self.day = 29
            elif self.day == 29:
                self.day = 1
                self.month = 3
            else:
                self.day = self.day + 1
        elif self.day == DAYS_IN_MONTH[self.month]:
            self.day = 1
            self.month = self.month + 1
        else:
            self.day = self.day + 1

    def yesterday(self):
        '''Will change the calling object so that it represents one calendar
        day before the date it originally represented. Does not return anything.
        '''
        if self.day == 1 and self.month == 1:
            self.day = 31
            self.month = 12
            self.year = self.year - 1
        elif self.month == 3 and self.isLeapYear() and self.day == 1:
            self.day = 29
            self.month = 2
        elif self.month == 3 and self.day == 1:
            self.day = 28
            self.month = 2
        elif self.day == 1:
            self.day = DAYS_IN_MONTH[self.month-1]
            self.month = self.month - 1
        else:
            self.day = self.day - 1

    def addNDays(self, N):
        '''Will change the calling object so that it represents N calendar days
        after the date it originally represented.'''
        for i in range(N):
            print(self)
            self.tomorrow()
        print(self)

    def subNDays(self, N):
        '''Will change the calling object so that it represents N calendar days
        before the date it originally represented. Assumes N is a non-negative
        integer.'''
        for i in range(N):
            print(self)
            self.yesterday()
        print(self)

    def isBefore(self, d2):
        '''Will return True if the calling object is a calendar date before the input
        named d2 (which will always be an object of type Date).'''
        if self.year < d2.year:
            return True
        elif self.month < d2.month and self.year == d2.year:
            return True
        elif self.day < d2.day and self.month == d2.month and self.year == d2.year:
            return True
        else:
            return False

    def isAfter(self, d2):
        '''Will return True if the calling object is a calendar date after the input
        named d2 (which will always be an object of type Date).'''
        if self.year > d2.year:
            return True
        elif self.month > d2.month and self.year == d2.year:
            return True
        elif self.day > d2.day and self.month == d2.month and self.year == d2.year:
            return True
        else:
            return False

    def diff(self, d2):
        '''Will return an integer representing the number of days between self and d2.'''
        selfCopy = self.copy()
        d2Copy = d2.copy()

        if selfCopy.equals(d2Copy):
            return 0
        elif selfCopy.isBefore(d2Copy):
            counter = 0
            while selfCopy.isBefore(d2Copy):
                selfCopy.tomorrow()
                counter += 1
            return -counter
        elif selfCopy.isAfter(d2Copy):
            counter = 0
            while selfCopy.isAfter(d2Copy):
                selfCopy.yesterday()
                counter += 1
            return counter

    def dow(self):
        '''Will return a string that indicates the day of the week (dow) of the object
        (of type Date) that calls it.'''
        if self.diff(Date(11,9,2011)) % 7 == 0:
            return "Wednesday"
        if self.diff(Date(11,9,2011)) % 7 == 6:
            return "Tuesday"
        if self.diff(Date(11,9,2011)) % 7 == 5:
            return "Monday"
        if self.diff(Date(11,9,2011)) % 7 == 4:
            return "Sunday"
        if self.diff(Date(11,9,2011)) % 7 == 3:
            return "Saturday"
        if self.diff(Date(11,9,2011)) % 7 == 2:
            return "Friday"
        if self.diff(Date(11,9,2011)) % 7 == 1:
            return "Thursday"
