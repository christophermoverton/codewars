#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'costlyIntervals' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY A
#

from collections import deque
def costlyIntervals(n, k, A):
    # Return a list of length n consisting of the answers
    # cost(l,r) = (or(l,r)-and(l,r))-(max(l,r)-min(l,r))
    # objective to maximize bitwise 'or', minimize bitwise'and' ,and minimize difference
    #of max(l,r) and min(l,r).
    # Worked solution involves finding from 1 element stack seed for left right search
    # a continuous left right run of cost(l,r) stack of range l,r until a break 
    # in costlr < k.  If element stack seed length of 1, yields costlr < k on next right iterative 
    # search, this stack element is discarded, and add present element to stack.
    # Otherwise for condition of costlr < k and stack length > 1, 
    # check head of stack for left search of continuous elements
    # and add to stack.  Once, a maximum right search of stack yields, costlr < k,
    # then double check from head to tail total costlr while
    # recording previous elements or,and,min, max of subarray (0,k) where k 
    # ranges to a maximum of len(elstack).  if costlr is true for stack, then 
    # return length of stack, otherwise, right search until costlr >= k, 
    # and return at search iteration +1 which records to element map maximum
    # costlr subarray length for element.  While checking and recording
    # subarray length for element, right to left search elements to be kept 
    # in costlr stack for next costlr subarray search.  This completes 
    # looped procedural check.  At finish of left to right iteration of A,
    # left search head of stack (if not completed), for maximum costlr subarray
    # and record in element map costlr subarray length.
    # Note:  My iterative checks on 4th test case, show +1 3908, and 1304 for most
    # elements relative expected answer.  Since subarray stack of elements, is double checked
    # for costlr >= k, where is flaw in logic for length of subarray stack +1
    # occurring?  Holding on problem because of answer set.        
    def lrcheck(elstack):
        cstack = []
        lorA = elstack[0][4]
        landA = lorA
        mina = elstack[0][4]
        maxa = elstack[0][4]
        cstack.append([lorA,landA,mina,maxa])
        for i in range(1,len(elstack)):
            lorA = lorA|elstack[i][4]
            landA = landA&elstack[i][4]
            if elstack[i][4] < mina:
                mina = elstack[i][4]
            if elstack[i][4] > maxa:
                maxa = elstack[i][4]
            cstack.append([lorA,landA,mina,maxa])
        costlr = (lorA-landA)-(maxa-mina)
        if costlr >= k:
            return len(cstack)
        else:
            j = len(cstack)-2
            while j >= 0:
                lorA,landA,mina,maxa = cstack[j]
                costlr = (lorA-landA)-(maxa-mina)
                if costlr >= k:
                    return j+1
   
    elmap = [-1]*len(A)
    lastel_i = 0
    elstack = [(A[0],A[0],A[0],A[0],A[0],0)]  # (|,&,minA,maxA,a)
    elstack = deque(elstack)
    for i in range(1,len(A)):
        a = A[i]
        orA, andA, minA,maxA = elstack[-1][0:4]
        next_orA = orA|a
        next_andA = andA&a
        next_minA = minA
        next_maxA = maxA
        if a < minA:
            next_minA = a
        if a > maxA:
            next_maxA = a
        costlr = (next_orA - next_andA)-(next_maxA-next_minA)
        if costlr >= k:
            elstack.append((next_orA,next_andA,next_minA,next_maxA,a,i))
        else:

            remove = False
            rind = 0
            #check last el_i is included on present elstack
            # checks head of elstack on back track 
            # note: this failed with previous costlr check
            j = lastel_i
            lorA = orA;landA=andA;lminA=minA;lmaxA=maxA;
            while j >= 0: 
                lastel = A[j]
                lorA = lastel|lorA
                landA = lastel&landA
                #lminA = minA
                #lmaxA = maxA
                if lastel < minA:
                    lminA = lastel
                if lastel > maxA:
                    lmaxA = lastel
                costlr = (lorA-landA)-(lmaxA-lminA)
                if costlr >= k:
                    elstack.appendleft((None,None,None,None,lastel,j))
                else:
                    break
                j-=1
            #check backtrack on tail ensuring tail elements
            # for elstack inclusion
            elstack_count = lrcheck(elstack)
            mina_j = a; maxa_j = a; or_a_j = a; and_a_j = a;
            j = len(elstack)-1
            while j >= 0:
                a_j,jindex = elstack[j][4:6]
                if remove:
                    if elstack_count > elmap[jindex]:
                        elmap[jindex] = elstack_count
                    j-=1
                    continue
                or_a_j = a_j|or_a_j
                and_a_j = a_j&and_a_j
                if a_j < mina_j:
                    mina_j = a_j
                if a_j > maxa_j:
                    maxa_j = a_j
                costlr_j = (or_a_j-and_a_j)-(maxa_j-mina_j)
                if costlr_j < k:
                    if len(elstack) > 1:
                        if elstack_count > elmap[jindex]:
                            elmap[jindex] = elstack_count
                        remove = True
                        rind = j
                else:
                    prev_oraj = or_a_j
                    prev_andaj = and_a_j
                    prev_minaj = mina_j
                    prev_maxaj = maxa_j
                    if elstack_count > elmap[jindex]:
                        elmap[jindex] = elstack_count
                j-=1

            lastel_i = elstack[0][5]
            elstack = deque(list(elstack)[rind+1:]) if rind < len(elstack)-1 else deque([])
            if len(elstack)>0:
                elstack.append((prev_oraj,prev_andaj,prev_minaj,prev_maxaj,a,i))
            else:    
                elstack.append((a,a,a,a,a,i))
    if len(elstack) > 1:
        for el in elstack:
            if len(elstack) > elmap[el[-1]]:
                elmap[el[-1]] = len(elstack)
    return elmap

def costlyIntervals2(n, k, A):
    # Return a list of length n consisting of the answers
    # cost(l,r) = (or(l,r)-and(l,r))-(max(l,r)-min(l,r))
    # objective to maximize bitwise 'or', minimize bitwise'and' ,and minimize difference
    #of max(l,r) and min(l,r)
    elmap = [-1]*len(A)
    elstack = [(A[0],A[0],A[0],A[0],A[0],0)]  # (|,&,minA,maxA,a)
    for i in range(1,len(A)):
        a = A[i]
        orA, andA, minA,maxA = elstack[-1][0:4]
        next_orA = orA|a
        next_andA = andA&a
        if a < minA:
            minA = a
        if a > maxA:
            maxA = a
        costlr = (next_orA - next_andA)-(maxA-minA)
        if costlr >= k:
            elstack.append((next_orA,next_andA,minA,maxA,a,i))
        else:
            mina_j = a; maxa_j = a; or_a_j = a; and_a_j = a;
            j = len(elstack)-1
            remove = False
            rind = 0
            while j >= 0:
                a_j,jindex = elstack[j][4:6]
                if remove:
                    elmap[jindex] = len(elstack)
                    j-=1
                    continue
                or_a_j = a_j|or_a_j
                and_a_j = a_j&and_a_j
                if a_j < mina_j:
                    mina_j = a_j
                if a_j > maxa_j:
                    maxa_j = a_j
                costlr_j = (or_a_j-and_a_j)-(maxa_j-mina_j)
                if costlr_j < k:
                    if len(elstack) > 1:
                        elmap[jindex] = len(elstack)
                        remove = True
                        rind = j
                    else:
                        if len(elstack) > elmap[jindex]:
                            elmap[jindex] = len(elstack)
                j-=1
            elstack = elstack[rind+1:] if rind < len(elstack)-1 else []
            elstack.append((a,a,a,a,a,i))
    if len(elstack) > 1:
        for el in elstack:
            elmap[el[-1]] = len(elstack)
    return elmap




# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
import testcase_costlyintervals4

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

k = int(first_multiple_input[1])

A = list(map(int, input().rstrip().split()))

result = costlyIntervals(n, k, A)
result2 = costlyIntervals(n,k,A[::-1])
result2.reverse()
pathstring = 'C:\\Users\\chris\\Documents\\'
file = open(pathstring+'costlyinterval.txt', 'w')
file.write('test test test')
file.write(str(result))
file.write(str(result2))
##for i in range(len(result)):
##    result[i] = max(result[i],result2[i])
print('\n'.join(map(str, result)))
#fptr.write('\n')
# import testcase_costlyintervals4_out
# for i in range(len(result)):
#     ea = int(input())
#     if result[i] != ea:
#         print('ea: '+str(ea))
#         print('a: '+str(result[i]))
#         print(i)

#fptr.close()
