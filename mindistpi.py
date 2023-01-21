#!/bin/python3

import sys
import math
import testcase_mindistpi
nums_pi = [	0, 1, 3, 22, 333, 355, 103993, 104348, 208341, 312689, 833719, 1146408, 4272943, 5419351, 80143857, 165707065, 245850922, 411557987, 1068966896, 2549491779, 6167950454, 14885392687, 21053343141, 1783366216531, 3587785776203, 5371151992734, 8958937768937]
denoms_pi = [1, 0, 1, 7, 106, 113, 33102, 33215, 66317, 99532, 265381, 364913, 1360120, 1725033, 25510582, 52746197, 78256779, 131002976, 340262731, 811528438, 1963319607, 4738167652, 6701487259, 567663097408, 1142027682075, 1709690779483, 2851718461558, 44485467702853]
print(len(nums_pi))
print(len(denoms_pi))
min,max = input().strip().split(' ')
min,max = [int(min),int(max)]
mindist = [999999999999999999,None,None]
denom_subset = []
for i,v in enumerate(denoms_pi):
    if v >= min and v <= max:
        denom_subset.append([v,i])
for val in denom_subset:
    d = val[0]
    n = nums_pi[val[1]]
    b = abs(n/d-math.pi)
    if b < mindist[0]:
        mindist[0] = b
        mindist[1] = d
        mindist[2] = n
# for i in range(min,max+1):
#     d = i
#     n = d*3
#     prev = abs(n/d-math.pi)
#     while True:
#         b = abs(n/d-math.pi)
#         if b < mindist[0]:
#             mindist[0] = b
#             mindist[1] = d
#             mindist[2] = n
#         if b > prev:
#             break
#         prev = b
#         n+=1
print(str(mindist[2])+"/"+str(mindist[1]))