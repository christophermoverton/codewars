#!/bin/python3
# note numpy doesn't import in hackkerank problem, and 3d lists operate slow in python
# so 3dFenwick tree structure unfortunately doens't pass speed muster using non numpy 
#approach unless one could a native python 3d python array structure...I haven't found
# a work around.  Hashing with dicts isn't any faster.  array module in python
# I believe is of a single dimension, so not useful.

#alternately solution using dictionary is given by if you want to pass tests
# T = int(input())
# for i in range(T):
#     N,M = [int(s) for s in input().split()]
#     data = {}
#     for j in range(M):
#         info = input().split()
#         if info[0] == "UPDATE":
#             data[info[1]+" "+info[2]+" "+info[3]] = int(info[4])
#         else:
#             x1 = int(info[1])
#             y1 = int(info[2])
#             z1 = int(info[3])
#             x2 = int(info[4])
#             y2 = int(info[5])
#             z2 = int(info[6])
#             res = 0
#             for k,v in data.items():
#                 corr = [int(s) for s in k.split()]
#                 if corr[0] <= x2 and x1 <= corr[0] and corr[1] <= y2 and y1 <= corr[1] and corr[2] <= z2 and z1 <= corr[2]:
#                     res += v
#             print(res)
#
import math
import os
from platform import java_ver
import random
import re
import sys
import numpy as np

class Fenwick3D:
    def __init__(self,n):
        # self.tree = None
        # self.tree = [None for i in range(n + 1)]
        # for i in range(n + 1):
 
        #     self.tree[i]= [None for i in range(n + 1)]
        #     for j in range(n+1):
        #         self.tree[i][j] = [None for j in range(n+1)]
        #         for k in range(n+1):
        #             self.tree[i][j][k] = 0
        self.tree = np.zeros((n+1,n+1,n+1))
    
        self.n = n

    def add(self, x, y, z, val):
        # x+=1; y+=1; z+=1;
        i = x
        while i <= self.n:
            j = y 
            while j <= self.n:
                k = z
                while k <= self.n:
                    self.tree[i][j][k] +=val
                    k+=(k&-k)
                j+=(j&-j)
            i+=(i&-i)

    def updateBit(self, x,y,z,val):
        #update_value = self.query(x,y,z,x,y,z)
        E = self.sum(x,y,z)
        G = self.sum(x-1,y,z)#self.sum(x1-1,y2,z2)
        D = self.sum(x,y-1,z)#self.sum(x2,y1-1,z2)
        A = self.sum(x-1,y-1,z)#self.sum(x1-1,y1-1,z2)
        F = self.sum(x,y,z-1)#self.sum(x2,y2,z1-1)
        H = self.sum(x-1,y,z-1)#self.sum(x1-1,y2,z1-1)
        B = self.sum(x-1,y-1,z-1)#self.sum(x1-1,y1-1,z1-1)
        C = self.sum(x,y-1,z-1)#self.sum(x2,y1-1,z1-1)
        update_value = E-G-D+A-F+H+B+C
        self.add(x,y,z,val-update_value)

    def sum(self,x, y, z):
        # x+=1; y+=1; z+=1;        
        # if (x < 0) or (y<0) or (x > self.n) or (y>self.n) or (z<0) or (z>self.n):
        #     return 0

        ans = 0;
        i = x
        while i > 0:
            j = y
            while j >0:
                k = z
                while k > 0:
                    ans += self.tree[i][j][k]
                    k-=(k&-k)
                j-= (j&-j)
            i-=(i&-i)
        return ans

    def query(self,x1,y1,z1,x2,y2,z2):
        #volumetric sum and differences of vertices of the queried cube
        #Note: remember to add what is volumetrically doubly subtracted and 
        #subtract what is doubly added.  Helps diagraming the queried
        #cube in a generalized way to see forumulation beyond 2D case.
        E = self.sum(x2,y2,z2)
        G = self.sum(x1-1,y2,z2)
        D = self.sum(x2,y1-1,z2)
        A = self.sum(x1-1,y1-1,z2)
        F = self.sum(x2,y2,z1-1)
        H = self.sum(x1-1,y2,z1-1)
        B = self.sum(x1-1,y1-1,z1-1)
        C = self.sum(x2,y1-1,z1-1)
        return E-G-D+A-F+H-B+C


def cubeSum(n, operations):
    #x_encode = [0]*((n*n*n)+(n*n)+n+1)
    past_query = {}
    pst_enc_x = Fenwick3D(n)
    res = []
    for op in operations:
        op = op.split()
        if op[0] == 'UPDATE':
            x,y,z,w = list(map(int,op[1:]))
            #encode_xyz = coordinate_encode(x,y,z,n)
            if (x,y,z) in past_query:
                prev_w = past_query[(x,y,z)]
                update_w = w-prev_w
                pst_enc_x.add(x,y,z,update_w)
                past_query[(x,y,z)] = w
            else:
                pst_enc_x.add(x,y,z,w)
                past_query[(x,y,z)] = w
        elif op[0] == 'QUERY':
            x1,y1,z1,x2,y2,z2 = list(map(int,op[1:]))
            #encode_xyz_1 = coordinate_encode(x1,y1,z1,n)
            #encode_xyz_2 = coordinate_encode(x2,y2,z2,n)
            sum = pst_enc_x.query(x1,y1,z1,x2,y2,z2)
            res.append(sum)           
    return res

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
import testcase_cubesumation3
T = int(input().strip())
results = []
for T_itr in range(T):
    first_multiple_input = input().rstrip().split()

    matSize = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    ops = []

    for _ in range(m):
        ops_item = input()
        ops.append(ops_item)

    res = cubeSum(matSize, ops)
    results.extend(res)
    print('\n'.join(map(str, res)))
#     fptr.write('\n')
import testcase_cubesummation3_out
for i in range(len(results)):
    ea = int(input())
    if results[i]!=ea:
        print('ea: '+str(ea))
        print('a: '+str(results[i]))
        print(i)
# fptr.close()
