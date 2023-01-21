#!/bin/python3

import math
import os
import random
import re
import sys
import testcase_bestdivisors


if __name__ == '__main__':
    n = int(input().strip())
    factors = []
    maxf = 0
    maxf_num = 0
    for i in range(1, n+1):
        if n % i == 0:
            if i >= 10:
                s = sum(list(map(int,list(str(i))))) 
                if s > maxf:
                    maxf_num = i
                    maxf = s
                elif s == maxf:
                    if maxf_num > i:
                        maxf_num = i
            else:
                if i > maxf:
                    maxf_num = i
                    maxf = i
                elif i == maxf:
                    if maxf_num > i:
                        maxf_num = i

            factors.append(i)
    print(maxf_num)