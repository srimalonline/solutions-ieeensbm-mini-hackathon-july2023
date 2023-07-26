#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isItPalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isItPalindrome(s):
    ## Solution Code
    isPalindrome = False
    length = len(s)
    mid = length//2
    leftSub = s[:mid]
    rightSub = s[mid+1:] if length%2==1 else s[mid:]
    isPalindrome = True if leftSub[::-1]==rightSub else False
    if isPalindrome:
        return "PALINDROME"
    else:
        return "NOT PALINDROME"
    ## Solution Code

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isItPalindrome(s)

    fptr.write(result + '\n')

    fptr.close()
