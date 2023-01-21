#!/bin/python3

import math
import os
import random
import re
import sys
import testcase_poisonous_plants3

#
# Complete the 'poisonousPlants' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY p as parameter.
#
def poisonousPlants(p):
    stack = [(p[0], 0)]
    maxN = 0
    for i in range(1, len(p)):
        if (p[i] > p[i - 1]):
            stack.append((p[i], 1))
            maxN = max((maxN, 1))
        else:
            n = 0
            while (len(stack) > 0 and stack[-1][0] >= p[i]):
                #iterating through asending stack and popping stack
                # while adjusting count n until descend value
                # found or len(stack) == 0.
                # Count backtracking.  Example p = [1,33,31,...]
                # means (33,1) added to stack.  31 < 33, so else while
                # stack pop (33,1) leaves stack length 1.  with n = 1,
                # and dayToDie = 2, maxN = max((1,2)) = 2
                # noting (1,0) persists in stack through descending series of 
                # p.

                n = max((n, stack[-1][1]))
                stack.pop()
            dayToDie = 0 if len(stack) == 0 else n + 1
            maxN = max((maxN, dayToDie))

            stack.append((p[i], dayToDie))
    return maxN

def poisonousPlants3(p):
    # Write your code here
    res = p[0:]
    temp = []
    i = 0
    days = 0
    days_list = []
    days_graph = {(val,i):0 for i,val in enumerate(res)}
    prev_list = []
    prev_temp_state = []
    iter_graph = {}
    while len(res) > 1:
        prev_check = False
        # priority to check next left first before previous iterations
        if i-1 >=0:
            if res[i] > res[i-1]:
                temp.append((res[i],i))
                prev_temp_state.append(i)
                if prev_list:
                    prev_list.pop()
                prev_list.append(i-1)
                days_list.append(days+1)
                
                if i+1 < len(res):
                    iter_graph[(res[i+1],i+1)] = (res[i],i)
            else:
                prev_check = True
        if prev_list and prev_check:
            prev = prev_list.pop()
            if res[i]>res[prev]:
                temp.append(i)
                prev_list.append(prev)
                prev_check = True
                days_list[-1] += 1
        
        if i == len(res)-1:
            print('len of temp: '+str(len(temp)))
            print('len of res: '+str(len(res)))
            print('len of prev_temp: '+str(prev_temp_state))
            if len(temp) == 0:
                break
            if len(prev_temp_state) > 2:
                temp = prev_temp_state
            temp.sort(reverse=True)
            for i in temp:
                res.pop(i)
            temp = []
            prev_temp_state = []
            i = 0
            days_list.sort()
            days_list = [days_list[0],days_list[-1]]
            prev_list = []
            days+=days_list[0]
            print(days)
        if len(res) == 1:
            break
  
        i+=1
    
    days_list.sort()
    return days_list[-1]
                

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

n = int(input().strip())

p = list(map(int, input().rstrip().split()))

result = poisonousPlants(p)

print(str(result) + '\n')

#fptr.close()
