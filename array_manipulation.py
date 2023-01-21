#!/bin/python3

import math
import os
import random
import re
import sys
import testcase_array_manipulation
#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#
class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
      self.k = None
# Insert method to create nodes
   def insert(self, data):
      if self.data:
         if data < self.data:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
         if data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
   def add(self, a, b, k):
        nodestack = []
        completed = set()
        while True:
            if len(nodestack) == 0:
                break
            node = nodestack.pop()
            if not a in completed:
                if a < node.data:
                    if b > node.data and node.data not in completed:
                        node.k += k
                        completed.add(node.data)

                    if node.left != None:
                        nodestack.insert(0,node.left)
                    else:
                        node.left = Node(a)
                        node.left.k = k
                        completed.add(a)
                elif a > node.data:
                    if node.right != None:
                        nodestack.insert(0,node.right)
                    else:
                        node.right = Node(a)
                        node.right.k = k
                        completed.add(a)  

   def find_nearest_path(self, data):
        res = []
        if self.data:
            res.append(self.data)
            if data < self.data:
                if not self.left is None:
                    res.extend(self.left.find_nearest_path(data))
            elif data > self.data:
                if not self.right is None:
                    res.extend(self.right.find_nearest_path(data))
        return res

def arrayManipulation3(n, queries):
    sum_track = {}
    #index_track = {}
    arr = [0]*n
    #start root
    a,b,k = queries[0]
    root = Node(a)
    root.insert(b)
    sum_track[a] = k
    sum_track[b] = k
    index_track = {a:b, b:a}
    list_indicies = [a,b] ## keep list sorted
    for q in queries[1:]:
        new_index_track = {}
        a,b,k = q
        resa = root.find_nearest_path(a)
        resb = root.find_nearest_path(b)
        lindex = 0
        if resa:
            lindex = list_indicies.index(resa[-1])
        uindex = 0
        if resb:
            uindex = list_indicies.index(resb[-1])
        ##get pair collections
        list_indc = list_indicies[lindex:uindex+1] 
        for val in list_indc:
            if a <= val and b >= val:
                sum_track[val] += k
        lneighbor = 0
        if lindex-1 > 0:
            lneighbor = lindex-1
        if a < resa[-1] and list_indicies[lneighbor] < a:
            sum_track[a] = sum_track[lneighbor]+k
        elif a > resa[-1]:
            sum_track[a] = sum_track[resa[-1]]

                


# def arrayManipulation4(n, queries):
#     arr = [0]*n
#     qs = queries[0:]
#     qs = sorted(qs, key=lambda [a,b,k]: max(b-a))
#     for q in qs:
#         a,b,k = q
#         #get set el
#         lbound = a-2
#         ubound = b
#         if lbound <0:
#             lbound = 0
#         if ubound > n-1:
#             ubound = n-1
#         larr = arr[0:lbound]
#         marr = arr[a-1:b]
#         uarr = arr[ubound:]
#         marrs = set(marr)
#         if len(marrs) > 1:
#             i = 0
#             while (i <= b-a):
#                 marr[i]+= k
#                 i+=1
#         else:
#             el = marr[0]
#             marr = [el+k]*len(marr)
#         larr.extend(marr)
#         larr.extend(uarr)
#         arr = larr

#     return max(arr)

def arrayManipulation2(n, queries):
    # slow
    arr = [0]*n
    resmax = 0
    for q in queries:
        a,b,k = q
        iterq = a-1
        while iterq <=b-1:
            arr[iterq]+=k
            iterq+=1
    return max(arr)

def arrayManipulation(n, queries):
    arr = [0]*n
    for i in queries:
        a,b,k = i
        arr[a-1] += k
        if b != len(arr):
            arr[b] -= k
    st = 0
    maxval = 0
    for i in arr:
        st+=i
        if st > maxval:
            maxval = st
    return maxval

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

queries = []

for _ in range(m):
    queries.append(list(map(int, input().rstrip().split())))

result = arrayManipulation(n, queries)

print(str(result) + '\n')

    
