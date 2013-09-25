# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 19:03:31 2013

A talk given by Ned, Jessica, et al at the Boston Python Meetup


@author: NotMark
"""

## Pycon US is happening in Montreal next year. suitable for all levels
## of expertise. 7 days long. $300. Way too much money.

## Insight Squared sponsored the pizza. Business analytics for small copmanies
## Provides 'over 400' beautiful visuizations. 60 people, 17 engineers.
## Python / django. Interesting!

## Neds talk: Facts and Myths about Names and Values

x = 23
y = x
x = 12

## y still points to 23 after x gets reassigned. Makes sense.

## Values have a reference count. Values will stick around until there
## is nothing left to refer to it.

x = 'hello'
x = 'world'

## Now that nothing is pointing to 'hello', it goes away. Garbage collection.

## ** Assignment never copies data! ** Many things can refer to the same value
## Example:

nums = [1,2,3]
other = nums
nums.append(4)

print other  # [1,2,3,4] !

## Immutable values are safe

x = 'hello'
y = x
x = x + ' there'


## References can be more than just names
## List elements are references

def aug_bad(aList, val):
    aList = aList + [val, val]
    return
    
nums = [1,2,3]
aug_bad(nums, 7)
print(nums)

def aug_twice(aList, val):
    aList.append(val)
    aList.append(val)
    return
    
nums = [1,2,3]
aug_twice(nums, 7)
print(nums)

def aug_good(aList, val):
    aList = aList + [val, val]
    return aList


nums = [1,2,3]
nums = aug_good(nums, 7)
print(nums)

## This seems pretty important:
## Names have no type!
## Values have no scope!

## Values created in a function can live on after  the function scope
## dies if a variable external to the function refers to it

## pythontutor.com !
## Looks like you can step through a program with visual representations
## of all of your variables as the program executes!

## Ned Batchelors blog possibly!
## bit.ly/pynames




## Jessicas talk: Important data structure and when to use them
## or: why is my program so slowwwww

# A seemingly simple task: looking up a bunch of words

# Looking up things in a list
# The items are unordered. The algorithm has to look at every single
# item in the list. This is O(n) complexity. Effort is on the order of the
# size of the list

import time
start = time.time()

# ... execute stuff

timeTaken = time.time() - start

# Looking up things in a dictionary uses some magic hash function that she
# didn't bother explaining. This gets looked up in constant time. O(1).

# In general! Finding or inserting things in a list is much much slower
# than using a dictionary for the same function. 

# For repeated lookups, always use a dictionary.

# This talk was really crappy. It was so basic as to be useless. All I know
# is dictionaries look things up faster than lists. I was told a fact and
# not taught a concept or an approach.


## Giles' talk: Virtualenv & PIP

# Python module of the week
# www.pymotw.com