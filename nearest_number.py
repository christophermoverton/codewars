#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#  3. INTEGER x
#

def closestNumber(a, b, x):
    # Write your code here
    n = a**b
    ans1 =  int((n//x)*x)

    ans1diff  = abs(n-ans1)
    ans2 = ans1+x
    ans2diff = abs(n-ans2)
    if ans1diff < ans2diff:
        return ans1
    elif ans2diff <= ans1diff:
        return ans2

#if __name__ == '__main__':
    ##fptr = open(os.environ['OUTPUT_PATH'], 'w')
import testcase_nearest_number
t = int(input().strip())

for t_itr in range(t):
    first_multiple_input = input().rstrip().split()

    a = int(first_multiple_input[0])

    b = int(first_multiple_input[1])

    x = int(first_multiple_input[2])

    result = closestNumber(a, b, x)

    print(str(result) + '\n')

    ##fptr.close()
