#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    # Solution Code
    if len(s)%2!=0:
        return -1
    l_str = s[:(len(s)//2)]
    r_str = s[(len(s)//2):]
    l_str = [*l_str]
    r_str = [*r_str]
    l_str.sort()
    r_str.sort()
    result = 0
    for i in range(len(l_str)):
        found_match = False
        for j in range(len(r_str)):
            if l_str[i] == r_str[j]:
                found_match = True
                r_str.pop(j)
                break
        if not found_match:
            result+=1
    return result
    # Solution Code

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = anagram(s)
        fptr.write(str(result) + '\n')
    fptr.close()