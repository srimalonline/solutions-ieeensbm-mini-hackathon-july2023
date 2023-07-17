#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    # Solution
    for i in range(len(s)-1):
            if(i==0):
                s = s[0].upper()+s[1:]
            if(s[i]==" "):
                s = s[:i+1]+s[i+1].upper()+s[i+2:]
    return s
    # Solution Code

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
