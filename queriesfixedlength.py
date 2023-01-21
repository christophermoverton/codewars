#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY queries
#

def solve(arr, queries):
    # Write your code here
    minqueries = {q:1e9 for q in queries}
    maxarrc = {}
    update_qc = []
    for q in queries:
        if q != 1:
            maxq = max(arr[0:q])
            if maxq == arr[0]:
                update_qc.append(q)
            else:
                maxarrc[q] = maxq
            minqueries[q] = maxq
        else: 
            maxarrc[q] = arr[0]
            minqueries[1] = arr[0]
    while update_qc:
        q = update_qc.pop()
        maxq = max(arr[1:q])
        maxarrc[q] = maxq 
    QC = queries.copy(); QC.sort();
    i = 1
    arrc = arr[1:]
    while arrc:
        if len(QC)==0:
            break
        while True:
            if len(QC) == 0:
                break
            if len(arrc) < QC[-1]:
                QC.pop()
            else:
                break
        a = arrc[0]
        update_QC = []
        for q in QC:
            if q != 1:
                maxq = maxarrc[q]
                if arrc[q-1] > maxq:
                    maxq = arrc[q-1]
                    maxarrc[q] = maxq
                if arrc[0] == maxq:
                    if q not in update_QC:
                        update_QC.append(q)
                if minqueries[q] > maxq:
                    minqueries[q] = maxq
            else:
                if minqueries[1] > a:
                    minqueries[1] = a
        while update_QC:
            qcu = update_QC.pop()
            maxarrc[qcu] = max(arrc[1:qcu])
        arrc.pop(0)
        i+=1
    return [minqueries[q] for q in queries]
            

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
import testcase_queriesfixedlength
first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

q = int(first_multiple_input[1])

arr = list(map(int, input().rstrip().split()))

queries = []

for _ in range(q):
    queries_item = int(input().strip())
    queries.append(queries_item)

result = solve(arr, queries)

print('\n'.join(map(str, result)))
import testcase_queriesfixedlength5_out
# for i in range(q):
#     ans = result[i]
#     ea = input()
#     if str(ans) != ea:
#         print('ans: ' + str(ans))
#         print('eans: '+ str(ea))
#         print(i)
#         print(queries[i])
#fptr.write('\n')

#fptr.close()
