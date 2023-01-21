#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#
import testcase_pairs3
def pairs(k, arr):
    my_dict = {}
    result = 0
    for ele in arr:
        my_dict[ele] = 1
        if ele + k in my_dict:
            result += 1
        if ele -k in my_dict:
            result += 1
    return result

def pairs2(k, arr):
    # Write your code here
    arrc = arr.copy()
    arrc.sort()
    ## track k count of prev node_stack
    nodes = [[arrc[0],[arrc[0]]]]
    Tcount = 0
    completed = []
    for i in arrc[1:]:
        update_stack = []
        while True:
            #node = nodes.pop(0)
            if not nodes:
                break
            node = nodes[0]
            vc = abs(i-node[0])
            if vc <= k:
            
                node[1].append(i)
                
                t1 = not (node[0],i) in completed and not (i,node[0]) in completed
                if vc == k and t1:
                    completed.append((i,node[0]))
                    #completed.append((node[0],i))
                    Tcount +=1
                break
            else:
                nodes.pop(0)
                #update_stack.append(node)
        if nodes:
            nodes[-1][1].append(i)
        nodes = update_stack.copy()
        if nodes:
            last_node = nodes[-1]
            ladds = []
            cindex = 0
            for ind,j in enumerate(last_node[1]):
                vc = abs(i-j)
                if vc <= k:
                    #ladds.append(j)
                    t1 = not (i,j) in completed and not (j,i) in completed
                    if vc == k and t1: 
                        completed.append((i,j))
                        Tcount+=1
                    cindex = ind
                    break
            ladds = last_node[1][cindex:0]                          
            nodes.append([i,ladds])
        else:
            nodes.append([i,[i]])
    return Tcount

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

k = int(first_multiple_input[1])

arr = list(map(int, input().rstrip().split()))

result = pairs(k, arr)

print(str(result) + '\n')

    #fptr.close()
