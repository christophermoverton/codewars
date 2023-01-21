
#!/bin/python3

import math
import os
import random
import re
import sys

def palindromeIndex(s):
        i = 0
        j = len(s) - 1
        index = -1
        while i < j:
            if s[i] != s[j]:
                if index >= 0:
                    break
                if (s[i + 1], s[i + 2]) == (s[j], s[j - 1]):
                    index = i
                    i += 3
                    j -= 2
                elif (s[i], s[i + 1]) == (s[j - 1], s[j - 2]):
                    index = j
                    i += 2
                    j -= 3
                continue
            i+=1
            j-=1
        return index

def palindromeIndex2(s):
    # Write your code here
    if s == s[::-1]:
        return -1
    for i,ch in enumerate(s):
        if i == len(s)-1:
            istr = s[0:len(s)-1]
            if istr == istr[::-1]:
                return len(s)-1
        elif i == 0:
            istr = s[1:]
            if istr == istr[::-1]:
                return 0
        else:
            istr = s[0:i]+s[i+1:]
            if istr == istr[::-1]:
                return i

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

q = int(input().strip())

for q_itr in range(q):
    s = input()

    result = palindromeIndex(s)

    print(str(result) + '\n')

#fptr.close()