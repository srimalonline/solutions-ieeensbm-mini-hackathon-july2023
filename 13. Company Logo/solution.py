#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    tempdic = {}
    noValues = list(map(lambda x : tempdic.update({x : len(s.split(x))-1}), sorted(set(s))))
    res = {val[0] : val[1] for val in sorted(tempdic.items(), key = lambda x: (-x[1], x[0]))} 
    for k,v in list(res.items())[:3]:
        print(k,v)