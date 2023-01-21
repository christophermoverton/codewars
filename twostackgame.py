#!/bin/python3

import math
import os
import random
import re
import sys
import testcase_twostackgame4
#
# Complete the 'twoStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER maxSum
#  2. INTEGER_ARRAY a
#  3. INTEGER_ARRAY b
#
def twoStacks(maxSum, a, b):
    suma = sum(a)
    sumb = sum(b)
    # print(suma)
    # print(sumb)
    if suma + sumb < maxSum:
        return len(a)+len(b)
    ac = a
    bc = b
    if suma < sumb:
        ac = b
        bc = a
    # else:
    #     ac = a
    #     bc = b
    total = 0
    indexT = 0
    lasta_i = 0
    #temp = []
    completed = True
    for i in range(len(ac)):
        if total + ac[i] > maxSum:
            completed = False
            break
        else:
            total += ac[i]
            indexT += 1
            #temp.append(ac.pop(0))
            #lasta_i = i
    if not completed:
        i -= 1
    total_b = 0
    for j in range(len(bc)):
        if bc[j]+total_b <= maxSum:
            if bc[j] + total <= maxSum:
                total += bc[j]
                indexT += 1
                total_b += bc[j]
                #bc.pop(0)
            else:
                if i < 0:
                    break
                total -= ac[i]
                i-=1
                
                total += bc[j]
                total_b += bc[j]
                #bc.pop(0)
        else:
            break

    return indexT

def twoStacks3(maxSum, a, b):
    suma = sum(a)
    sumb = sum(b)
    # print(suma)
    # print(sumb)
    if suma + sumb < maxSum:
        return len(a)+len(b)
    ac = a
    bc = b
    if suma < sumb:
        ac = b
        bc = a
    # else:
    #     ac = a
    #     bc = b
    total = 0
    indexT = 0
    lasta_i = 0
    temp = []
    while len(ac) > 0:
        if total + ac[0] > maxSum:
            break
        else:
            total += ac[0]
            indexT += 1
            temp.append(ac.pop(0))
            #lasta_i = i

    total_b = 0
    while len(bc)>0:
        if bc[0]+total_b <= maxSum:
            if bc[0] + total <= maxSum:
                total += bc[0]
                indexT += 1
                total_b += bc[0]
                bc.pop(0)
            else:
                total -= temp[-1]
                temp.pop()
                total += bc[0]
                total_b += bc[0]
                bc.pop(0)
        else:
            break

    return indexT


def twoStacks2(maxSum, a, b):
    # Write your code here
    NS = [] #node stack
    #initialize node stack
    ac = a[0:]
    bc = b[0:]
    aset = set()
    aval = ac.pop(0)
    aset.add(aval)
    maxCount = 0
    suma = sum(a)
    sumb = sum(b)
    print(suma)
    print(sumb)
    print(maxSum)
    preAppendA = False
    if suma+sumb < maxSum:
        print('hit')
    if aval <= maxSum:
        ## check ratio of aval to maxSum
        ## preappend account all choices less than 1e-6
        if aval/maxSum < 1e-6:
            preAppendA = True
        else:
            NS.append([ac[0:],bc[0:],aval,1])
            maxCount = 1
    bset = set()
    bval = bc.pop(0)
    bset.add(bval)
    acc = a[0:]
    preAppendB = False
    if bval <= maxSum:
        if bval/maxSum < 1e-4:
            preAppendB = True
        else:
            NS.append([acc[0:],bc[0:],bval,1])
            maxCount = 1
    if preAppendA and preAppendB:
        absum = aval+bval
        abcount = 2
        while True:
            aval = ac[0]
            bval = bc[0]
            choices = [None,None]
            if aval/maxSum < 1e-3:
                choices[0] = aval
            if bval/maxSum < 1e-3:
                choices[1] = bval
            if choices[0] == None and choices[1] == None:
                break
            for i,choice in enumerate(choices):
                if choice != None:
                    absum+=choice
                    abcount += 1
                if i == 1:
                    ac.pop(0)
                else:
                    bc.pop(0)
            if maxSum-absum < 6e6 and maxSum-absum > 0:
                break
        NS.append([ac[0:],bc[0:],absum,abcount])
    # if not aset and not bset:
    #     return 1
    while True:
        if not NS:
            break
        update_NS = []
        while NS:
            node = NS.pop()
            choices = [None,None]
            if node[0]:
                choices[0] = node[0][0]
            if node[1]:
                choices[1] = node[1][0]
            #choices = [node[0][0],node[1][0]]
            for i,choice in enumerate(choices):
                if choice != None:
                    CMS = node[2]
                    if CMS+choice > maxSum:
                        if node[3] > maxCount:
                            maxCount = node[3]
                    else:
                        #node[2] += choice
                        #node[3] += 1

                        node_i = node[i].copy()
                        node_i.pop(0)
                        node_i1 = node[(i+1)%2].copy()
                        newnode = []
                        if i == 0:
                            newnode = [node_i,node_i1, node[2]+choice,node[3]+1]
                        else:
                            newnode = [node_i1, node_i, node[2]+choice, node[3]+1]         
                        if newnode[3] > maxCount:
                            maxCount = newnode[3]
                        update_NS.append(newnode)
        NS = update_NS.copy()
    return maxCount    
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

g = int(input().strip())
res = []
for g_itr in range(g):
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    maxSum = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = twoStacks(maxSum, a, b)
    res.append(result)
    print(str(result) + '\n')
import testcase_twostackgame4_out
for answer in res:
    expected_answer = int(input())
    if answer != expected_answer:
        print('expected answer: '+str(expected_answer))
        print('answer: '+str(answer))
    #fptr.close()
