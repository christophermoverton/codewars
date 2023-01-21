#!/bin/python3

import math
import os
import random
import re
import sys
import testcase_newyearchaos2
#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    ## using sort index for q as strategy
    ## check flow involves checking the true_index of q[i] where it should be
    ## relative position i on q.  If if i < true_index then the position was bribed
    ## additional check flow includes checking for leading zeros on sort index of q 
    ## labeled qc.  To check for leading zeros simply iterate and count trailing 
    # zeros to the maxelement on qc.  Then using equation lz = maxel-i-1-tz
    #  some elements of q with i may match the true_index but have, leading zeros.
    # I do this because lz can be variably mixed requiring a much deeper
    # iteration of qc relative trailing zeros to maxel which is more likely
    # to be less likely deep iterative intensive.  If it is deeper, then 
    # likely to cause a 'Too chaotic' break  
    tbribes = 0
    nl = len(q)
    i = 0
    qc = [0]*(nl+1)
    maxel = 0
    while True:
        if i > nl-1:
            break
        n = q[i]
        t1 = False
        true_index = n-1
        qc[n] = 1
        if n > maxel:
            maxel = n
        bcount = 0
        if n != maxel:
            j = n+1
            tz = 0
            while j <= maxel:
                if qc[j] == 1:
                    bcount+=1
                else:
                    tz +=1
                j+=1
            ## check the number of elements i 
            ## implies no leading zeros on qc list
            ## lz = maxel - n -tz (trailing zeros)
            lz = maxel-i-1-tz
            if lz > 0:
                t1 = True
                bcount = lz
            #t1 = True
        if i < true_index:
            bribes = abs(true_index-i)
            
            if bribes > 2:
                print('Too chaotic')
                return
            
            tbribes+=bribes
        elif t1:
            if bcount > 2:
                print('Too chaotic')
                return
            tbribes+=bcount
        i+=1
    print(tbribes)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
