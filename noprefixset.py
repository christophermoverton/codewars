#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#
import testcase_noprefixset3
root = {}
max_roots = {}
max_len = 0
min_len = 99999999999999999999999999
def add_to(root,s):
    current_node = root.setdefault(s[0],[0,{}])
    if len(s) == 1:
        current_node[0] += 1
    else:
        add_to(current_node[1],s[1:])
        
def is_prefix(root,s):
    if len(s) == 1:
        if len(root[s[0]][1])>0 or root[s[0]][0] > 1:
            return True
        else:
            return False
    else:
        if root[s[0]][0] > 0:
            return True
        else:
            return is_prefix(root[s[0]][1],s[1:])

def noPrefix(words):
    count = 0
    if min_len == max_len:
        for word in words:
            if word in max_roots:
                print('BAD SET')
                print(word)
                return 
            else:
                max_roots[word] = 1
        print('GOOD SET')
    else:
        for word in words:
            add_to(root,word)
            #print(root)
            if is_prefix(root,word):
                print("BAD SET")
                print(word)
                break
            count += 1
            if count == n:
                print("GOOD SET")    # Write your code here

# if __name__ == '__main__':
n = int(input().strip())

words = []
#max_len = 0
for _ in range(n):
    words_item = input()
    m = len(words_item) 
    if m >max_len:
        max_len = m
    if m < min_len:
        min_len = m
    
    words.append(words_item)

noPrefix(words)
