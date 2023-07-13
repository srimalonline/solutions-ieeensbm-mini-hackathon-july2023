#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    ## Solution Code
    m3m = (n-1)//3 # Maximum multiplier of 3
    m5m = (n-1)//5 # Maximum multiplier of 5
    m15m = (n-1)//15 # Maximum multiplier of 15
    
    sum_3 = (m3m+1)*(m3m*3)//2 # Sum of m3m multiples of 3
    sum_5 = (m5m+1)*(m5m*5)//2 # Sum of m5m multiples of 5
    sum_15 = (m15m+1)*(m15m*15)//2 # Sum of m15m multiples of 15
    
    m_sum = sum_3+sum_5-sum_15 # Sum m3m multiples of 3 and m5m multiples of 5 ( Sum of m15m multiples are deducted to remove the excess from the total sum as both of sum_3 and sum_5 includes the sum of m15m multiples of 15)
    print(m_sum)
    ## Solution Code