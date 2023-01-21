#!/bin/python3

import math
import os
import random
import re
import sys
import heapq
#
# Complete the 'minimumAverage' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY customers as parameter.
def minWait(allOrders) :
    heapq.heapify(allOrders)
    totalWaitTime = 0
    numOrders = len(allOrders)
    if numOrders == 0 :
        return 0
    pendingOrders = []
    currentTime = allOrders[0][0]
    loop = True
    while loop :
        while len(allOrders) != 0 and allOrders[0][0] <= currentTime :
            order = heapq.heappop(allOrders)   
            heapq.heappush(pendingOrders, (order[1], order[0]))
        if len(pendingOrders) != 0 :
            minWaitOrder = heapq.heappop(pendingOrders)
            waitTime = currentTime - minWaitOrder[1] + minWaitOrder[0]
            totalWaitTime += waitTime
            currentTime += minWaitOrder[0]
        else :
            currentTime += 1
        if len(pendingOrders) == 0 and len(allOrders) == 0 :
            loop = False
    return int(totalWaitTime/numOrders)

def minimumAverage(customers):
    # Write your code 
    heapq.heapify(customers)
    csort = customers[0:]
    CH = [(csort[0][1],csort[0][0])]
    #OT = {csort[0][1]:[csort[0][0]]}
    WT = []
    prevOT = csort[0][0]
    csort.pop(0)
    loop = True
    j = 0
    while loop:
        while csort and csort[0][0] <= prevOT:
            ot,ct = heapq.heappop(csort)
            heapq.heappush(CH,(ot,ct))
        if CH:
            customer = heapq.heappop(CH)
            ctime,otime = customer
            #otime = heapq.heappop(OT[customer])
            wt_prev = WT[-1] if WT else 0
            wt_i = ctime + wt_prev + prevOT-otime
            WT.append(wt_i)
            prevOT = otime
        else:
            j+=1
            prevOT+=1
        if j > 100000:
            j = 0
            prevOT = csort[0][0]
        if not csort and not CH:
            break

            
    print(WT)
    return int(sum(WT)/len(WT))
    

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
import testcase_minavgwaittime3
n = int(input().strip())

customers = []

for _ in range(n):
    customers.append(list(map(int, input().rstrip().split())))

result = minWait(customers)

print(str(result) + '\n')

#fptr.close()
