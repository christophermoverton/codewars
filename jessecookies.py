#!/bin/python3

import math
import os
import random
import re
import sys
import testcase_jessecookies
#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#
from heapq import heapify, heappush, heappop

def get_number_mixes(cookies, minimum_value):
    cookies = list(cookies)
    heapify(cookies)
    count = 0
    while cookies[0] < minimum_value:
        if len(cookies) < 2:
            return -1
        heappush(cookies, heappop(cookies) + 2 * heappop(cookies))
        count += 1
    return count

def cookies(k, A):
    # Write your code here
    #s_1+2*s_2 = s_3
    return get_number_mixes(A,k)
        

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

k = int(first_multiple_input[1])

A = list(map(int, input().rstrip().split()))

result = cookies(k, A)

print(str(result) + '\n')

    #fptr.close()
