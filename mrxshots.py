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
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY shots
#  2. 2D_INTEGER_ARRAY players
#
import array
# with range update


# Python Code for Interval tree
class Interval:
    def __init__(self, low, high):
        self.low = low
        self.high = high
 
    def __str__(self):
        return "[" + str(self.low) + "," + str(self.high) + "]"
 
 
class Node:
    def __init__(self, range, maxv,minv):
        self.range = range
        self.maxv = maxv
        self.minv = minv
        self.count = 1
        self.left = None
        self.right = None
 
    def __str__(self):
        return "[" + str(self.range.low) + ", " + str(self.range.high) + "] " + "max = " + str(self.max) + "\n"
 
 
def insert(root, x):
    if root == None:
        return Node(x, x.high, x.low)
 
    if x.low < root.range.low:
        root.left = insert(root.left, x)
    else:
        root.right = insert(root.right, x)
 
    if root.maxv < x.high:
        root.maxv = x.high
    if root.minv > x.low:
        root.minv = x.low
    root.count += 1
 
    return root
 
 
def inOrder(root):
    if root == None:
        return
 
    inOrder(root.left)
    print(root, end="")
    inOrder(root.right)


def searchInterval(root,x):
    count = 0
    nodestack = []
    nodestack.append(root) 
    while nodestack:
        node = nodestack.pop()
        t1 = (x.low >= node.range.low and x.low <= node.range.high)
        t2 = (x.high >= node.range.low and x.high <= node.range.high)
        t3 = (x.low <= node.range.low)
        t4 = (x.high >= node.range.high)
        if (t1 and t4) or (t3 and t4) or (t3 and t2) or (t1 and t2):
            count +=1
            # if (node.left and node.left.max >= x.low):
            #     nodestack.append(node.left)
            # elif (node.right and node.right.max >= x.low):
            #     nodestack.append(node.right)
        t5 = node.left and node.left.maxv >= x.low
        t6 = node.left and node.left.minv <= x.high
        t7 = node.right and node.right.maxv >= x.low
        t8 = node.right and node.right.minv <= x.high
        if t5 and t6:
            # the overlapping node may be present in left child
            nodestack.append(node.left)
        if t7 and t8:
            nodestack.append(node.right)
    return count

def solve(shots,players):
    res = 0
    maxn = max(shots, key = lambda x: x[1])
    maxn = max(maxn)
    maxp = max(players,key = lambda x: x[1])
    maxp = max(maxp)
    maxn = max(maxn,maxp)
    left_interval_arr = [0]*(maxn+2)
    right_interval_arr = [0]*(maxn+2)
    for shot in shots:
        left_interval_arr[shot[0]]+=1
        right_interval_arr[shot[1]+1]-=1
    sl_int_arr = [0]*(maxn+2)
    sr_int_arr = [0]*(maxn+2)
    sl_int_arr[1] = left_interval_arr[1]
    sr_int_arr[1] = right_interval_arr[1]
    for i in range(2,maxn+2):
        sl_int_arr[i] = sl_int_arr[i-1]+left_interval_arr[i]
        sr_int_arr[i] = sr_int_arr[i-1]+right_interval_arr[i]
    for player in players:
        l,r = player
        res+= (sl_int_arr[r]+sr_int_arr[l])
    return res

def solve2(shots, players):
    # Write your code here
    root = None
    root = insert(None,Interval(shots[0][0],shots[0][1]))
    for shot in shots[1:]:
        lr_interval = Interval(shot[0],shot[1])
        root = insert(root,lr_interval)
    sumS_i = 0
    for player in players:
        sumS_i += searchInterval(root,Interval(player[0],player[1])) 
    return sumS_i
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
import testcase_mrxshots3
first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

shots = []

for _ in range(n):
    shots.append(list(map(int, input().rstrip().split())))

players = []

for _ in range(m):
    players.append(list(map(int, input().rstrip().split())))

result = solve(shots, players)

print(str(result) + '\n')

#fptr.close()
