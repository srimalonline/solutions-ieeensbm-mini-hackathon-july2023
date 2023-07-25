#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Solution Code
    player_ranks = []
    ranked = list(dict.fromkeys(ranked))
    rank_l = len(ranked)
    player.reverse()
    i = 0
    j = 0
    for i in range(len(player)):
        while j<rank_l and player[i] < ranked[j]:
            j += 1
            if j >= len(ranked):
                break
        player_ranks.append(j + 1)
    player_ranks.reverse()
    return player_ranks
    # Solution Code

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
