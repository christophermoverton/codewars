#!/bin/python3

import math
import os
import random
import re
import sys
import testcase_dynamicarrays
#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    last_answer = 0
    res = []
    arr = [[] for i in range(n)]
    for q in queries:
        qtype, x, y = q
        idx = (x^last_answer)%n
        if qtype == 1:
            arr[idx].append(y)
        if qtype == 2:
            last_answer = arr[idx][y%len(arr[idx])]
            res.append(last_answer) 
    return res


    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

q = int(first_multiple_input[1])

queries = []

for _ in range(q):
    queries.append(list(map(int, input().rstrip().split())))

result = dynamicArray(n, queries)

print('\n'.join(map(str, result)))
#fptr.write('\n')

    #fptr.close()
