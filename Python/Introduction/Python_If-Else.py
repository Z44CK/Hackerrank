# Python If-Else

# Task 
# Given an integer, n, perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

# Input Format
# A single line containing a positive integer, n.

# Constraints
# 1 <= n <= 100

# Output Format
# Print Weird if the number is weird; otherwise, print Not Weird.

#!/bin/python

import sys


N = int(raw_input().strip())

if N % 2 != 0:
    print "Weird"
else:
    if N >= 2 and N <= 5:
        print "Not Weird"
    elif N >= 6 and N <= 20:
        print "Weird"
    elif N > 20:
        print "Not Weird"
# -------------------------------------------------------------
# syntax that is specific to Python 2.x. In Python 3.x, the raw_input() 
# function has been replaced by the input() function. Also, in Python 3.x, you don't need to call the strip() method on input.
n = int(input())

if n % 2 != 0:
    print("Weird")
else:
    if (n >= 2) and (n <= 5):
        print("Not Weird")
    elif (n >= 6) and (n <= 20):
        print("Weird")
    else:
        print("Not Weird")

