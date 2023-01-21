#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'polynomialDivision' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#  3. 2D_INTEGER_ARRAY queries
# 
class Node:
    def __init__(self, value, index):
        self.left = None
        self.right = None
        self.value = value
        self.index = index

class BST:
    def __init__(self):
        self.root = None
    def insert(self, value,index):
        self.insert_node(self.root, value, index)
    
    def insert_node(self, node, value, index):
        if node:
            if index < node.index:
                if node.left:
                    self.insert_node(node.left,value,index)
                else:
                    node.left = Node(value,index)
            elif index == node.index:
                node.value = value
            else:
                if node.right:
                    self.insert_node(node.right,value,index)
                else:
                    node.right = Node(value,index)
        else:
            self.root = Node(value,index)

    def search(self, hi_index, low_index):
        return self.search_node(self.root, hi_index,low_index)

    def search_node(self, node, hi_index, low_index):
        res = []
        if node:
            if node.index <= hi_index and node.index >= low_index:
                res.append([node.value,node.index])
                if node.left: 
                    res.extend(self.search_node(node.left,hi_index,low_index))
                if node.right:
                    res.extend(self.search_node(node.right,hi_index,low_index))
            elif node.index < low_index:
                if node.right:
                    res.extend(self.search_node(node.right,hi_index,low_index))
            elif node.index > hi_index:
                if node.left:
                    res.extend(self.search_node(node.left,hi_index,low_index))
        return res      

def leastSigBit(num):
    return (num & -num)
# implementation of a Fenwick tree
class PrefixSumTree(object):
    def __init__(self,array):
        l = len(array)
        self.sums = [0] * l
        for i in range(1,l):
            cl = i - leastSigBit(i)
            for j in range(cl+1,i+1):
                self.sums[i] = (self.sums[i] + array[j]) % m

    def sum(self,i):
        sum = 0
        while i > 0:
            sum = (sum + self.sums[i]) % m
            i -= leastSigBit(i)
        return sum

    # adds toAdd to the ith element of array
    def add(self,i,toAdd):
        while i <= len(self.sums)-1:
            self.sums[i] = (self.sums[i] + toAdd) % m
            i += leastSigBit(i)


# Python3 implementation of the approach
m = 10**9+7

def modMult(a, b, mod): 
  
    res = 0; # Initialize result 
  
    # Update a if it is more than 
    # or equal to mod 
    a = a % mod; 
  
    while (b): 
      
        # If b is odd, add a with result 
        if (b & 1): 
            res = (res + a) % mod; 
              
        # Here we assume that doing 2*a 
        # doesn't cause overflow 
        a = (2 * a) % mod; 
  
        b >>= 1; # b = b / 2 
      
    return res; 
 
# Function to return the GCD
# of given numbers
def gcd(a, b):
 
    if (a == 0):
        return b
    return gcd(b % a, a)
 
# Recursive function to return (x ^ n) % m
def modexp(x, n):
 
    if (n == 0) :
        return 1
     
    elif (n % 2 == 0) :
        return modexp((x * x) % m, n // 2)
     
    else :
        return (x * modexp((x * x) % m,
                           (n - 1) / 2) % m)
 
 
# Function to return the fraction modulo mod
def getFractionModulo(a, b):
 
    c = gcd(a, b)
 
    a = a // c
    b = b // c
 
    # (b ^ m-2) % m
    d = modexp(b, m - 2)
 
    # Final answer
    ans = ((a % m) * (d % m)) % m
 
    return ans

def expanded_synthetic_division(dividend, divisor):
    """Fast polynomial division by using Expanded Synthetic Division. 
    Also works with non-monic polynomials.

    Dividend and divisor are both polynomials, which are here simply lists of coefficients. 
    E.g.: x**2 + 3*x + 5 will be represented as [1, 3, 5]
    """
    out = list(dividend)  # Copy the dividend
    normalizer = divisor[0]
    for i in range(len(dividend) - len(divisor) + 1):
        # For general polynomial division (when polynomials are non-monic),
        # we need to normalize by dividing the coefficient with the divisor's first coefficient
        out[i]  = getFractionModulo(out[i], normalizer)
        #out[i] /= normalizer

        coef = out[i]
        if coef != 0:  # Useless to multiply if coef is 0
            # In synthetic division, we always skip the first coefficient of the divisor,
            # because it is only used to normalize the dividend coefficients
            for j in range(1, len(divisor)):
                out[i + j] = (out[i+j] +(-divisor[j] * coef)%m)%m

    # The resulting out contains both the quotient and the remainder,
    # the remainder being the size of the divisor (the remainder
    # has necessarily the same degree as the divisor since it is
    # what we couldn't divide from the dividend), so we compute the index
    # where this separation is, and return the quotient and remainder.
    separator = 1 - len(divisor)
    return out[:separator], out[separator:]  # Return quotient, remainder.

def polynomialDivision(a, b, queries):
    pc = c[0:]
    res = []
    rootv = getFractionModulo(-b,a)
    poly_comp = [0]*len(pc)
    poly_comp[0] = 1
    poly_comp_sum = [0]*(len(pc)+1)
    poly_comp_sum[1] = pc[0]
    
    for i in range(1,len(pc[1:])+1):
        poly_comp[i] = (poly_comp[i-1]*rootv)%m
        ns = (poly_comp[i]*pc[i])%m
        poly_comp_sum[i+1] = ns #(poly_comp_sum[i-1]+ns)%m
    sumTree = PrefixSumTree(poly_comp_sum)
    # def checkRoot(l,h):
    #     # get summation from low to high
    #     psum = 0
    #     if l > 0:
    #         psum = (poly_comp_sum[h]-poly_comp_sum[l-1])%m
    #         div = pow(rootv, l, m)#(rootv**(l))%m
    #         psum = getFractionModulo(psum,div)
    #         # psum /= div
    #         psum %= m
    #     else:
    #         psum = poly_comp_sum[h]
    #     ## get bst updates
    #     updates = bst.search(h,l)
    #     for update in updates:
    #         value, index = update
    #         uv = (value*poly_comp[index-l])%m
    #         ov = (pc[index]*poly_comp[index-l])%m
    #         psum+= (uv-ov)%m
    #         psum%=m
    #     if psum%m == 0:
    #         return True
    #     else:
    #         return False
    # def checkRoot2(l,h):
    #     i = l
    #     psum = 0
    #     if rootv:
    #         while i <= h:
    #             psum+= (poly_comp[i-l]*pc[i])%m
    #             i+=1
    #         if psum%m == 0:
    #             return True
    #         else: 
    #             return False
    #     else:
    #         if pc[l]%m == 0:
    #             return True
    #         else:
    #             return False

    # def checkPoly(pindex,remainder,check):
    #     if pindex == len(pc)-1:
    #         frac = getFractionModulo(pc[pindex], a)
    #         remainder = pc[pindex-1] - (frac*b%m)
    #     else:
    #         frac = getFractionModulo(remainder, a)
    #         remainder = pc[pindex-1]-(frac*b%m)
    #     if pindex > 1:
    #         checkPoly(pindex-1, remainder%m, check)
    #     else:
    #         if remainder%m == 0:
    #             check[0]=True
    # def checkPoly2(pc,div=[a,b]):
    #     pcr = pc[0:]
    #     pcr.reverse()
    #     q,r = expanded_synthetic_division(pcr,div)
    #     if r[0] == 0:
    #         return True
    #     else:
    #         return False
    # Write your code here
    for query in queries:
        type,i,v = query
        if type == 1:
            # pc[i] = v
            #bst.insert(v,i)
            # compute how much we need to add for the sum
            toAdd = v-pc[i]
            # update the array c with our new entry q[2]
            pc[i] = v
            if rootv:
                # then we add the appropriate amount to our prefix sums.
                # since sumTree keeps track of sum c_i * x^i we multiply by the 
                # appropriate power of x
                sumTree.add(i+1,(toAdd*(poly_comp[i])) % m)
        else:
            # remember c is zero indexed but sumTree is one indexed
            # so we do sum(q[2]+1) - sum(q[1]) instead of sum(q[2]) - sum(q[1]-1)
            high = v
            low = i
            pOfX = pc[low] if rootv== 0 else (sumTree.sum(high+1) - sumTree.sum(low)) % m
            if pOfX == 0:
                res.append("Yes")
            else:
                res.append("No")
            # check = [False]
            # checkPoly(len(c)-1,0,check)
            # if check[0]:
            #     print('Yes')
            # else:
            #     print('No') 
            # ea = input()
            # ans = None
            # if checkRoot(i,v):
            #     print('Yes')
            #     ans='Yes'
            #     res.append('Yes')
            # else:
            #     ans = 'No'
            #     print('No')
            #     res.append('No')
            # if ea != ans:
            #     print('ea: '+str(ea))
            #     print('a: '+ str(ans))  
            # else:
            #     if checkPoly2(pc[i:v+1]):
            #         res.append('Yes')
            #         print('Yes')
            #     else:
            #         res.append('No')
            #         print('No')
                
    return res
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
import testcase_polynomialdivision4
first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

a = int(first_multiple_input[1])

b = int(first_multiple_input[2])

q = int(first_multiple_input[3])

c= list(map(int, input().rstrip().split()))

queries = []

for _ in range(q):
    queries.append(list(map(int, input().rstrip().split())))
import testcase_polynomialdivision4_out
result = polynomialDivision(a, b, queries)


#print('\n'.join(result))

for i,a in enumerate(result):
    ea = input()
    if ea != a:
        print('ea: '+str(ea))
        print('a: '+ str(a))
        print(i)
#fptr.write('\n')

#fptr.close()
