#!/bin/python3

import math
import os
import random
import re
import sys
import testcase_andxoror
#
# Complete the 'andXorOr' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def andXorOr(a):
    # Write your code here
    ca = a[0:]
    subsets = {}
    Smax = 0
    for i,val in enumerate(ca):
        subset_left = []
        subset_right = []
        j_r = i-1
        j_l = i+1

        minv = val
        min2 = 1e22
        j_list = [(j_r,1),(j_l,-1)]
        b_r = len(a)
        for j_v in j_list:
            j_i, ival = j_v
            while True:
                if not j_i < b_r:
                    break
                if not j_i > 0:
                    break
                if ca[j_i] >= val:
                    if ca[j_i] <= min2:
                        min2 = ca[j_i]
                        S = (((minv&min2)^(minv|min2))&(minv^min2))
                        if S > Smax:
                            Smax = S
                        #subset_right.append(S)
                        
                else:
                    min2 = minv
                    minv = ca[j_i]
                    S = (((minv&min2)^(minv|min2))&(minv^min2))
                    if S > Smax:
                        Smax = S
                    #subset_right.append(S)
                    break
                j_i+=ival
    return Smax
        

        

    

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

a_count = int(input().strip())

a = list(map(int, input().rstrip().split()))

result = andXorOr(a)

print(str(result) + '\n')


 