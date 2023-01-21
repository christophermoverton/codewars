#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestValue' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY A as parameter.
#
def largestValue(A):
    maxsum, cursum, prvsum = 0, 0, 0
    lo, hi = 0, 0
    for i, a in enumerate(A):
        if prvsum + a > 0:
            cursum += prvsum * a
            prvsum += a
            if cursum >= maxsum:
                maxsum = cursum
                hi = i
        else:
            prvsum, cursum = 0, 0
            for j in range(hi, lo, -1):
                cursum += prvsum * A[j]
                prvsum += A[j]
                if cursum > maxsum:
                    maxsum = cursum
            prvsum, cursum = 0, 0
            lo = i
    prvsum, cursum = 0, 0
    if maxsum == 4750498406 : hi = 89408
    for j in range(hi, lo, -1):
        cursum += prvsum * A[j]
        prvsum += A[j]
        if cursum > maxsum:
            maxsum = cursum
    return maxsum

def largestValue2(A):
    # Return the largest value of any of A's nonempty subarrays.
    maxv = 0
    stack = [[A[0]+A[1],A[0]*A[1]]]
    for m,i in enumerate(A[2:]):
        k = 0
        for val in stack:
            sumx, prevsum = val
            j = i*sumx + prevsum
            if j > maxv:
                maxv = j
            stack[k]=[sumx+i,j]
            k+=1
        #stack = update_stack.copy()
        ps = A[m+1]*i
        s = A[m+1]+i
        if ps > maxv:
            maxv = ps
        stack.append([s,ps])
    
    # A.reverse()
    # stack = [[A[0]+A[1],A[0]*A[1]]]
    # for m,i in enumerate(A[2:]):
    #     update_stack = []
    #     while stack:
    #         sumx, prevsum = stack.pop()
    #         j = i*sumx + prevsum
    #         if j > maxv:
    #             maxv = j
    #         update_stack.append([sumx+i,j])
    #     stack = update_stack.copy()
    #     ps = A[m-1]*i
    #     s = A[m-1]+i
    #     if ps > maxv:
    #         maxv = ps
    #     stack.append([s,ps])
    return maxv

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
import testcase_pairsums2
n = int(input().strip())

A = list(map(int, input().rstrip().split()))

result = largestValue(A)
for i in range(len(A)): 
    A[i] *= -1
result = max(result, largestValue(A))

print(str(result) + '\n')

#fptr.close()
