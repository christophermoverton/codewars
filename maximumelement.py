#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

from collections import deque
import heapq

class MaxHeap:
 
    # Initialize the max heap
    def __init__(self, data=None):
        if data is None:
            self.data = []
        else:
            self.data = [-i for i in data]
            heapq.heapify(self.data)
 
    # Push item onto max heap, maintaining the heap invariant
    def push(self, item):
        heapq.heappush(self.data, -item)
 
    # Pop the largest item off the max heap, maintaining the heap invariant
    def pop(self):
        return -heapq.heappop(self.data)
 
    # Pop and return the current largest value, and add the new item
    def replace(self, item):
        return heapq.heapreplace(self.data, -item)
 
    # Return the current largest value in the max heap
    def top(self):
        return -self.data[0]

def getMax(operations):
    # Write your code here
    stack = deque([])
    maxheap = MaxHeap()
    remove = {}
    res = []
    maxv = -1
    for op in operations:
        op = list(map(int,op.split()))
        type = 0
        val = 0
        if len(op) == 1:
            type = op[0]
        else:
            type,val = op
        if type == 1:
            stack.append(val)
            maxheap.push(val)
        elif type == 2:
            val = stack.pop()
            if maxheap.top() == val:
                maxheap.pop()
            else:
                if val in remove:
                    remove[val][0]+=1
                else:
                    remove[val] = [1]
        else:
            while maxheap.top() in remove:
                j = remove[maxheap.top()][0]
                delkey = maxheap.top()
                while j > 0:
                    maxheap.pop()
                    j-=1
                del remove[delkey]
            res.append(maxheap.top())
    return res            


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
import testcase_maximumelement2
n = int(input().strip())

ops = []

for _ in range(n):
    ops_item = input()
    ops.append(ops_item)

res = getMax(ops)

print('\n'.join(map(str, res)))
import testcase_maximumelement2_out
for i in range(len(res)):
    ea = int(input())
    if res[i] != ea:
        print('ea: '+str(ea))
        print('a: '+str(res[i]))
        print(i)
#fptr.write('\n')

#fptr.close()
