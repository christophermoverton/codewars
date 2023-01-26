#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here
    count = 0
    q = []
    for el in s:
        nq = []
        while q:
            mEl,dEl = q.pop()
            if mEl+1 < m and dEl+el < d:
                mEl += 1
                dEl = dEl+el
                nq.append([mEl,dEl])
            elif mEl+1 == m and dEl+el ==d:
                count +=1 
        if m == 1 and el == d:
            count+=1
        if 1 < m and el < d:
            nq.append([1,el])
        q = nq[0:]
    return count 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
