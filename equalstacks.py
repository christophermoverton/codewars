#!/bin/python3

import math
import os
import random
import re
import sys
import testcase_equalstacks3
#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def equalStacks(h1, h2, h3):
    # Write your code here
    h1c = h1[0:]; h2c=h2[0:]; h3c=h3[0:];
    hcs = [h1c,h2c,h3c]
    res = 0
    lh1 = sum(h1c)
    lh2 = sum(h2c)
    lh3 = sum(h3c)
    while True:
        # lh1 = sum(h1c)
        # lh2 = sum(h2c)
        # lh3 = sum(h3c)
        lhs = [lh1,lh2,lh3]
        maxlh3 = 0
        maxlh3_stack = None
        max_i = None
        if not h1c and not h2c and not h3c:
            break
        for i,lh in enumerate(lhs):
            if lh > maxlh3:
                maxlh3 = lh
                maxlh3_stack = hcs[i]
                max_i = i
        maxGreater = False
        for lh in lhs:
            if maxlh3 > lh:
                maxGreater = True
        if maxGreater:
            v = maxlh3_stack.pop(0)
            if max_i == 0:
                lh1 -= v
            elif max_i == 1:
                lh2 -= v
            elif max_i == 2:
                lh3 -= v
        else:
            res = sum(maxlh3_stack)
            break
    return res

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

first_multiple_input = input().rstrip().split()

n1 = int(first_multiple_input[0])

n2 = int(first_multiple_input[1])

n3 = int(first_multiple_input[2])

h1 = list(map(int, input().rstrip().split()))

h2 = list(map(int, input().rstrip().split()))

h3 = list(map(int, input().rstrip().split()))

result = equalStacks(h1, h2, h3)

print(str(result) + '\n')

    #fptr.close()
