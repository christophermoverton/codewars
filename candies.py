#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'distributeCandy' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY score as parameter.
#

def distributeCandy(score):
    # Write your code here
    res = 0
    candies = {}

    for i, val in enumerate(score):
        if i-1 > 0 and i < len(score)-1:
            prev = i-1
            if prev not in candies:
                #measure val next
                nextval = score[i+1]
                if val not in candies:
                    if val >= nextval:
                        res+=3
                        candies[i] = 2
                        candies[i+1] = 1
                    else:
                        res+=3
                        candies[i] = 1
                        candies[i+1] = 2
                        
            else:
                pcandies = candies[i-1]
                ccandies = candies[i]
                prevval = score[i-1]
                nextval = score[i+1]
                if prevval < val and val < nextval:
                    candies[i+1] = ccandies+1
                elif prevval > val and prevval < nextval :
                    candies[i+1] = pcandies+1
                elif prevval > val and val > nextval:
                    candies[i+1] = ccandies-1
                elif prevval < val and prevval > nextval:
                    candies[i+1] = pcandies-1
                elif prevval > val and val < nextval:
                    candies[i+1] = ccandies+1
                elif prevval < nextval and nextval < val:
                    candies[i+1] =    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    score_count = int(input().strip())

    score = []

    for _ in range(score_count):
        score_item = int(input().strip())
        score.append(score_item)

    result = distributeCandy(score)

    fptr.write(str(result) + '\n')

    fptr.close()
