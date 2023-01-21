#!/bin/python3

import math
import os
import random
import re
import sys
import datetime
#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#
import testcase_legoblocks2
def legoBlocks(n, m):
    A = 1000000000+7
    r = [0]*(m+1)
    a = [0]*(m+1)
    #print(datetime.datetime.now())

    a[0] = 1
    for j in range(1, m+1):
        a[j] += a[j-1] if j-1>=0 else 0
        a[j] += a[j-2] if j-2>=0 else 0
        a[j] += a[j-3] if j-3>=0 else 0
        a[j] += a[j-4] if j-4>=0 else 0
    #print(datetime.datetime.now())    
    for j in range(1, m+1):
        a[j] = a[j] % A
        a[j] = a[j] ** n
        a[j] = a[j] % A
    #print(datetime.datetime.now())
    
    r[1] = 1
    for j in range(2, m+1):
        r[j] = a[j]
        for k in range(1, j):
            r[j] -= r[k]*a[j-k]
        r[j] = r[j] % A
    #print(datetime.datetime.now())
    return r[m]%A


MOD = 10**9+7
global Tetra
Tetra = {}
global max_tet
max_tet = 0
def legoBlocks2(n, m):
    global max_tet
    global Tetra
    def Tetranacci(X):
        if X == 0:
            return 1
        elif X > 0:
            tw1 = Tetra[X-1] if X-1 in Tetra else Tetranacci(X-1)%MOD
            tw2 = Tetra[X-2] if X-2 in Tetra else Tetranacci(X-2)%MOD
            tw3 = Tetra[X-3] if X-3 in Tetra else Tetranacci(X-3)%MOD
            tw4 = Tetra[X-4] if X-4 in Tetra else Tetranacci(X-4)%MOD
            return tw1+tw2+tw3+tw4
        elif X < 0:
            return 0
    # Write your code here
    def A(w,h):
        if w in Tetra:
            return (Tetra[w]**h)%MOD
        else:
            Tw = Tetranacci(w)%MOD
            Tetra[w] = Tw
            return Tw**h
    S_w_h= {(1,m):1}
    def S(w,h):
        if (w,h) in S_w_h:
            return S_w_h[(w,h)]
        res = 0
        S_i_h = []
        for i in range(1,w):
            res += S(i,h)*A(w-i,h)%MOD
        res = A(w,h)-res
        S_w_h[(w,h)] = res%MOD
        return res
        #A(w,h) - S(w-1,h)*A(w-k,h) 
        #S(W,H) = A(W,H) - sum_x( S(X,H)*A(W-X,H) ) //implicitly, S(1,H)=1
    
    for i in range(max_tet,m+1):
        if i not in Tetra:
            tw = Tetranacci(i)%MOD
            Tetra[i] = tw
        if i > max_tet:
            max_tet = i
    return S(m,n)%MOD

    #A(W,H) = T(W)^H



# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

t = int(input().strip())

for t_itr in range(t):
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = legoBlocks(n, m)

    print(str(result) + '\n')

    #fptr.close()
