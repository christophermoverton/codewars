#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'componentsInGraph' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY gb as parameter.
#

def componentsInGraph(gb):
    # Write your code here
    graph = {}
    completed = []
    #build edges 
    minn = 1e9
    maxn = 0
    for edge in gb:
        a,b = edge
        if a not in graph:
            graph[a] = [b]
        else:
            graph[a].append(b)
        if b not in graph:
            graph[b] = [a]
        else:
            graph[b].append(a)
    #traverse from node
    for edge in gb:
        a,b = edge
        nodestack = []
        #if a not in completed:
        completed = set()
        nodestack = [(a,1)]
        gcount = 0
        while nodestack:
            node,count = nodestack.pop()
            while graph[node]:
                enode = graph[node].pop()
                if enode not in completed:
                    nodestack.append((enode,count+1))
            completed.add(node)
            # if count > gcount:
            #     gcount = count
        gcount = len(completed)
        if gcount < minn and gcount >= 2:
            minn = gcount
        if gcount > maxn:
            maxn = gcount
    return [minn,maxn]


    

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
import testcase_componentingraph4
n = int(input().strip())

gb = []

for _ in range(n):
    gb.append(list(map(int, input().rstrip().split())))

result = componentsInGraph(gb)

print(' '.join(map(str, result)))
# fptr.write('\n')

# fptr.close()
