#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#
from itertools import permutations
import decimal 
A = 10**9+7
factorials = [0]*2001
def fact(lower,upper):

    res = 1
    i = lower
    j = upper - lower
    while i <= upper:
        res*=i/j
        i+=1
        j-=1
    return res

factorials[0] = 1
decimal.getcontext().prec=5000
for i in range(1,2001):
    factorials[i] = (i*factorials[i-1])
##print(factorials)
def solve(n, m):
    # Write your code here
    #too slow method
    # ml = [1]*(m-1)
    # nl = [0]*n
    # ml.extend(nl)
    # return len(set(permutations(ml,len(ml))))
    ##formula for unique permutations (n+m)!/(n!)(m-1)!
    ## note m-1 ensures that 1 is leading string pick
    ## for m-1 choices left
    E = decimal.Decimal(2.718281828459045)
    ml = m-1
    mn = ml+n
    #c= factorials[mn]
    d = decimal.Decimal(factorials[mn])
    e =decimal.Decimal(factorials[m-1])
    f = decimal.Decimal(factorials[n])
    g = d/(e*f)
    return int(g%decimal.Decimal(A))
    #print(len(str(c)))
    #print(len(str(d)))
    #a = decimal.Decimal(factorials[mn])/(decimal.Decimal(factorials[ml])*decimal.Decimal(factorials[n]))
    return int(a)%A
    # maxmn = max(ml,n)
    # minmn = min(ml,n)
    # f_mn = fact(maxmn+1,mn)
    # return int((f_mn)%A)
    #use sterling equation for a = (n+m-1)!/((m-1)!*n!))
    #also use logarithm to prevent overflow 
    #one can use math.e to convert final computation back to a 
    #for log(a) computation e(log(a)) where e is the inverse
    # function of log
    a_s = math.log(2*(math.pi*(n+m-1)**.5))
    b_s = math.log(1/(2*(math.pi*(m-1)**.5)))
    c_s = math.log(1/(2*(math.pi*(n)**.5)))
    loga = (n+m-1)*math.log(n+m-1)+a_s + (1-m)*math.log(m-1)+b_s-n*math.log(n)+c_s
    Dloga = decimal.Decimal(loga)
    return int(E**Dloga)%A
    #return int((factorials[mn]/(factorials[ml]*factorials[n]))%A)

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
import testcase_sherlockpermutations3
t = int(input().strip())
res = []
for t_itr in range(t):
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = solve(n, m)
    res.append(result)
    print(str(result) + '\n')

import testcase_sherlockpermutations3_out
    
for i in range(t):
    ea = int(input())
    a = res[i]
    if ea!=a:
        print('expected answer: '+str(ea))
        print('answer: '+str(a))
        print(i)
