#!/bin/python3

import math
import os
import random
import re
import sys
import collections
#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    def leftrotate(st, d):
        tmp = st[d : ] + st[0 : d]
        return tmp
   
    # In-place rotates s
    # towards right by d
    def rightrotate(st, d):
        return leftrotate(st, len(st) - d)
    
    os = 'abcdefghijklmnopqrstuvwxyz'
    ros = list(os)
    ros = collections.deque(ros)
    ros.rotate(k)
    keymap = {}
    for i,v in enumerate(os):
        keymap[ros[i]] = v
    outstr = ''
    
    for ch in s:
        if ch.isalpha():
            if ch.islower():
                outstr+= keymap[ch]
            else:
                chl = ch.lower()
                nchl = keymap[chl]
                outstr+= nchl.upper()
        else:
            outstr+=ch
    return outstr
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
