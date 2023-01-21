#!/bin/python3

import math
import os
import random
import re
import sys

primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
#
# Complete the 'primeCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def primeCount(n):
    # Write your code here
    global primes
    pcount = 0
    pfactors = 1
    i=0
    while pfactors <= n:
        pcount+=1
        pfactors*=primes[i]
        i+=1
    return max(0,pcount-1)
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
import testcase_primefactors
q = int(input().strip())

for q_itr in range(q):
    n = int(input().strip())

    result = primeCount(n)

    print(str(result) + '\n')

    #fptr.close()
