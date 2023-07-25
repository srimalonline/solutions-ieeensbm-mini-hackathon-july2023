#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'twoPluses' function below.
def twoPluses(grid):
    areas = dict() 
    overlap_grid = [[set() for j in range(len(grid[i]))] for i in range(len(grid))]
    counter=-1
    
    collisions=dict() 
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            valid_moves=True if grid[i][j]=="G" else False 
            idx = 0
            max_area=0
        
            while valid_moves:
                    to_detect_i=[i]
                    to_detect_j=[j]
                    
                    for k in range(2):
                        if k == 0:
                            if i - idx < 0 or j-idx < 0:
                                valid_moves=False 
                                break
                        else:
                            if i + idx >= len(grid) or j+idx >= len(grid[i]):
                                valid_moves=False    
                                break 
                            
                    if valid_moves:
                      if grid[i+idx][j] == "G" and grid[i-idx][j] == "G" and \
                       grid[i][j+idx] == "G" and grid[i][j-idx] == "G":
                       
                        max_area+=1 if idx == 0 else 4  
                        
                        for r in range(2):
                         for p in range(1, idx+1):
                            for c in range(2):
                                if c==0:
                                  if r==0:
                                    to_detect_i.append(i+p)
                                    to_detect_j.append(j)
                                  else:
                                    to_detect_j.append(j+p)
                                    to_detect_i.append(i)
                                else:
                                    if r==0:
                                        to_detect_i.append(i-p)
                                        to_detect_j.append(j)
                                    else:
                                        to_detect_j.append(j-p)
                                        to_detect_i.append(i)
                                
                        idx+=1 
                        
                        counter+=1
                        collisions[counter]=set()
                    
                        for k in range(len(to_detect_i)):
                        
                            l=overlap_grid[to_detect_i[k]][to_detect_j[k]]
                            
                            for element in l:
                                collisions[element].add(counter)
                              
                            collisions[counter].union(l)
                            l.add(counter)
                        
                        areas[counter]=max_area
                         
                      else:
                        valid_moves=False
                                        
                
    if len(areas)==0:
        return 0
    else:
        max_vals=set()
        max_vals.add(0)
        for i in range(len(areas)):
            for j in range(i+1,len(areas)):
                if j not in collisions[i]:
                   max_vals.add(areas[i]*areas[j])
                
        return max(max_vals)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
