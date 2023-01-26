#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    # maxid 
    maxid = max(arr)
    tarr = [0]*(maxid+1)
    for el in arr:
        tarr[el]+=1
    maxfrq = 0
    maxtyp = 0
    for typid, freq in enumerate(tarr):
        if freq > maxfrq:
            maxfrq = freq
            maxtyp = typid
    return maxtyp

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
