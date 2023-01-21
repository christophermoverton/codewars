##large array queries
import math
import os
import random
import re
import sys
import bisect

#
# Complete the 'playingWithNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY queries
#

def playingWithNumbers(arr, queries):
    # Write your code here
    sarr_pos = {}
    sarr_neg = {}
    arr_pos = []
    arr_neg = []
    k_p = 0
    k_n = 0
    for i in arr:
        if i < 0:
            k_n+=abs(i)
            sarr_neg[i]=k_n
            arr_neg.append(i)
        elif i >= 0:
            k_p+=i
            sarr_pos[i]=k_p
            arr_pos.append(i)
    arr_neg.sort()
    arr_pos.sort()
    l_p = len(arr_pos)
    l_n = len(arr_neg)
    sumq = 0
    sumeq = 0
    for i in queries:
        sumq += i
        if sumq < 0:
            # find max index of i on positive subset
            maxindex = bisect.bisect_right(sarr_pos,abs(i))-1
            amaxval = arr_pos[-1]
            mval = arr_pos[maxindex]
            k_n = l_p - maxindex
            s_pos = sarr_pos[mval] 
            sumeq = abs(sumq)*l_n + (s_pos - abs(sumq)*maxindex) + (sarr_pos[amaxval]- s_pos- abs(sumq)*k_n)
            print(sumeq)  
        else:
            # find max index of i on positive subset
            maxindex = bisect.bisect_right(sarr_neg,abs(i))-1
            amaxval = arr_neg[-1]
            mval = arr_neg[maxindex]
            k_n = l_n - maxindex
            s_neg = sarr_neg[mval] 
            sumeq = abs(sumq)*l_p + (s_neg - abs(sumq)*maxindex) + (sarr_neg[amaxval] - s_neg- abs(sumq)*k_n)
            print(sumeq)  
        #print(sumarr + (n-k)*i - k*i 

#fptr = open(os.environ['OUTPUT_PATH'], 'w')

n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

q = int(input().strip())

queries = list(map(int, input().rstrip().split()))

result = playingWithNumbers(arr, queries)

print('\n'.join(map(str, result)))
#fptr.write('\n')

#fptr.close()