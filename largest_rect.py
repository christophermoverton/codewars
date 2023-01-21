#!/bin/python3

import math
from msvcrt import kbhit
import os
import random
import re
import sys
from turtle import left
import testcase_largest_rect2
#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def insert(self, root, data):
        if root:
            if data < root.data:
                if root.left:
                    self.insert(root.left, data)
                else:
                    root.left = Node(data)
            if data > root.data:
                if root.right:
                    self.insert(root.right, data)
                else:
                    root.right = Node(data)
    def search_lub_gub(self,root, data, glb_lub):
        
        if root:
            if data < root.data:
                if glb_lub[1] > root.data:
                    glb_lub[1] = root.data
                if root.left:
                    self.search_lub_gub(root.left,data, glb_lub)
            if data > root.data:
                if glb_lub[0] < root.data:
                    glb_lub[0] = root.data
                if root.right:
                    self.search_lub_gub(root.right, data, glb_lub)
###Find the largest rectangle area per k array continuous spacing,
### and the minimum value val = min[x_i,...,x_i+k] and subset.
### where area = k*val.  Key to this problem is that stack 
## processing inner and outer pops for min subset generation
## redundantly leads to repeating val = min[x_i,...x_i+k] for 
## some x_m on any number of subsets. Strategy in this solution
# involves for choice x ensuring that it is the minimum of the 
# subset of h and that we can compute the maximum 
# length subset for choice x.  That is for x the maximum length 
# subset does not include y such that y < x.  
# Note: There is no need to compute
# area for all subsets being area less than maximum
# length subset of x.  The next part of this strategy
# uses a sorted array of h called sx.   
# Using a sorted array sx, and binary search tree called
# completed, track completed indicies to determine the largest 
# k subset for choice x_m in list.  Example first iteration:
# set x = sx.pop(0).  This is applied to first index of 
# h array.  Since there are no completed indicies in h,
# the largest subset is the length of h, and area = x*length of h
# insert x_index to array.  Note: x = xs.pop(0) in xs is the 
# smallest value of h in first iteration.  
# Note: all values of h are dictionary
# hash keyed including repeat multiple indicies for x for
# quick index referencing on h.  Note: the algorithim
# does not change ordering or modify h.
# The next iteration chooses x = 2nd lowest value of sx.
# So we determine the largest subset containing x but excluding
# the previous completed index in completed.
# Determining this largest subset by searching the binary
# tree and determining the greatest lower bound of x_i (index of x)
# and least upper bound of x_i. The least upper bound is
#  min{set of all completed indices such that y is in completed and 
# y > x_i}  The greatest lower bound of x_i is max{set of all completed
# indicies such that y in completed means y < x_i}.  Abbreviated notation 
# Lub(x_i) means that there 
# is no completed index y < lub(x_i) and conversely,
# there is no completed index y > glb(x_i).  So these bounds
# determining the maximum subset length for x_i. 
# Set k = lub(x_i)-glb(x_i)-1  then compute area, add x to completed 
# and repeat iteration for next x.  The advantage again in this 
# algorithim avoids smaller subsets containing x where k is maximum length
# for area containing x.  Secondly repeated values of x in h with 
# differing indicies,
# are added to BST-completed accounting for changes in lub and glb
# as applies xs a sorted array ascending.  The sorted array 
# provides choice of x at pop(0) so that no value greater than 
# pop(0) is less than x.  This means that all completed values 
# of previous iteration are accounted for in the [x_j,...,x_j+k]
# subset of x ensuring x is minimum.

            
def largestRectangle(h):
    def put(kx, k, v):
        if k in kx:
            kx[k].append(v)
        else:
            kx[k] = [v]
    hc = h[0:]
    #hash list hc key list value to array index for quick search
    kx = {}
    for i,val in enumerate(hc):
        put(kx,val,i)
    sx = sorted(hc)
    lub_s = len(hc) #least upper bound for all m > x_i 
    glb_s = -1  #greatest lower bound for all j < x_i 
    
    completed = Node(kx[sx[0]][-1]) #[]#[0]*lub_s
    maxval = 0
    
    while sx:
        x = sx.pop(0)
        x_i = kx[x].pop()
        lub = lub_s
        glb = glb_s
        s_glb_lub = [glb,lub]
        completed.search_lub_gub(completed,x_i,s_glb_lub)
        glb, lub = s_glb_lub
        k_x_i = lub-glb-1
        area = k_x_i*x
        if area > maxval:
            maxval = area
            #print(maxval)
        completed.insert(completed,x_i)
        #print(x)
    return maxval

def largestRectangle2(h):
    # Write your code here
    hc = h[0:]
    #hc.sort()
    maxval = 0
    l = len(hc)
    k = l
    minhc1 = min(hc)
    minhc = minhc1
    while hc:
        sub_k = k
        sub_hc = hc[0:]
        sub_minhc = minhc
        while sub_hc:
            val = sub_minhc
            if sub_k*val > maxval:
                maxval = sub_k*val
                print(maxval)
            if hc[-1]==sub_minhc and k !=1:
                sub_minhc = min(sub_hc[0:-1])
            elif k==1:
                sub_minhc = hc[0]
            sub_k-=1
            sub_hc.pop()
        #print(k)
        if hc[0] == minhc and k !=1:
            minhc = min(hc[1:])
        elif k == 1:
            minhc = hc[0]
        k-=1

        hc.pop(0)
    # hc = h[0:]
    # k = l
    # minhc = minhc1
    # while hc:
    #     val = minhc
    #     if k*val > maxval:
    #         maxval = k*val
            
    #     k-=1
    #     if hc[-1] == minhc and k != 0:
    #         minhc = min(hc[0:-1])
    #     hc.pop()
    return maxval

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

n = int(input().strip())

h = list(map(int, input().rstrip().split()))

result = largestRectangle(h)

print(str(result) + '\n')

#fptr.close()
