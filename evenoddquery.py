#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. 2D_INTEGER_ARRAY queries
#
import testcase_evenodd5
def solve(arr, queries):
    # Write your code here
    res = []
    for query in queries:
        x,y = query
        nextarrx = 1
        if x < y:
            nextarrx = arr[x]   
        if nextarrx == 0 and x < y:
            res.append('Odd')
            continue
        if arr[x-1]%2 == 0:
            res.append('Even')
        else:
            res.append('Odd')  
    return res     

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

arr_count = int(input().strip())

arr = list(map(int, input().rstrip().split()))

q = int(input().strip())

queries = []

for _ in range(q):
    queries.append(list(map(int, input().rstrip().split())))

result = solve(arr, queries)

print('\n'.join(result))
#fptr.write('\n')
import testcase_evenodd5_out
for i in range(q):
    ea = input()
    a = result[i]
    if a != ea:
        print('Answer: '+str(a))
        print('Expected Answer: '+str(ea))
        x,y = queries[i]
        print(queries[i])
        print(arr[x])
        print(arr[x-1])
        print(i)

    ##fptr.close()
