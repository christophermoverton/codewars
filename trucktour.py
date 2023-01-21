#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

def truckTour(petrolpumps):
    # Write your code here
    n = len(petrolpumps)
    nodes = []
    i = 0
    p,d = petrolpumps[0]
    pa = p-d
    if pa > 0:
        nodes.append((pa,i))
        i = 1
    while i < n:
        p,d = petrolpumps[i]
        pa = p-d
        update_nodes = []
        while nodes:
            opa, j = nodes.pop(0)
            npa = opa+pa
            if npa > 0:
                update_nodes.append((npa,j))
        nodes = update_nodes.copy()
        if pa > 0:
            nodes.append((pa,i))
        #pa = p-d
        i+=1
    return nodes[0][1]
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

n = int(input().strip())

petrolpumps = []

for _ in range(n):
    petrolpumps.append(list(map(int, input().rstrip().split())))

result = truckTour(petrolpumps)

print(str(result) + '\n')

#fptr.close()
