#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'steadyGene' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING gene as parameter.
#

def steadyGene(gene):
    vl=len(gene)//4
    
    genes=["A","C","T","G"]
    
    d=dict() 
    c=0
    
    for el in genes:
        counter=[m.start(0) for m in re.finditer(r'(?=(' + el + '))', gene)]

        diff = vl - len(counter) 
        if diff < 0:
            d[c]=list()
            for j in range(0,len(counter)-abs(diff)+1):
              d[c].append(([counter[j],counter[j+abs(diff)-1]]))
            c+=1
     
    if len(d)==0:
        return 0
    else:
        c_elements=[d[i].pop(0) for i in range(len(d))]

        def check_distance(element):
            min_d=min([element[i][0] for i in range(len(element))])
            max_d=max([element[i][1] for i in range(len(element))])

            return max_d - min_d + 1

        min_distance = check_distance(c_elements)
        
        while any(len(d[i]) > 0 for i in range(len(d))):
            tuples=[]
            for i in range(len(d)):
                if d[i]:
                    tuples.append([i, d[i][0]])
        
            winning_index=list() 
            for el in tuples:
                temp=c_elements.copy() 
                temp[el[0]]=el[1]
                winning_index.append([el[0], check_distance(temp)])

            index, new_min_distance = (sorted(winning_index, key=lambda x: x[1]))[0]

            c_elements[index] = d[index].pop(0)

            if new_min_distance < min_distance:
               min_distance=new_min_distance
               
        return min_distance

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    gene = input()

    result = steadyGene(gene)

    fptr.write(str(result) + '\n')

    fptr.close()