#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY tree as parameter.
#
class Node:
    def __init__(self,value,map_value):
        self.value = value
        self.map_value = map_value
        self.left = None
        self.right = None
class BST:
    def __init__(self)

def solve(tree):
    # Write your code here
    graph = {}
    minv = 1e10
    maxv = -1
    if not tree:
        return 1
    for edge in tree:
        a,b = edge
        if a in graph:
            graph[a].append(b)
        else:
            graph[a] = [b]
        if b in graph:
            graph[b].append(a)
        else:
            graph[b] = [a]
        if a > maxv:
            maxv = a
        if a < minv:
            minv = a
        if b > maxv:
            maxv = b
        if b < minv:
            minv = b
    subsetcnt = maxv-minv+1
    l_i = minv+1
    l = minv
    l_r_set = set()
    for r in range(minv+1,maxv+1):
        found = False
        for node in graph[l_i]:
            if node >= l and node <= r:
                subsetcnt+=1
                l_r_set.add((l,r))
                #l_r_set.add((l_i,r))
                l_i = r
                found = True
                break
        if not found:
            l = r
            l_i = r
    r = maxv
    l = maxv-1
    r_i = maxv-1
    for l in range(maxv-1,minv-1,-1):
        found = False
        for node in graph[r_i]:
            if node >= l and node <= r:
                if not (l,r) in l_r_set:
                    subsetcnt+=1
                    l_r_set.add((l,r))
                    #l_r_set.add((l,r_i))
                    r_i= l
                    found = True
                    break
                else:
                    r_i = l
                    found = True
                    break
        if not found:
            r_i = l
            r = l
    return subsetcnt


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
import testcase_self_driving_bus4

n = int(input().strip())

tree = []

for _ in range(n - 1):
    tree.append(list(map(int, input().rstrip().split())))

result = solve(tree)

print(str(result) + '\n')

# fptr.close()
