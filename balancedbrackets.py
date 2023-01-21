#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
import testcase_balancedbrackets4
class Node:
    def __init__(self, data):
        openinsert = ['(','{','[']
        closeinsert = [')','}',']']
        self.open = False
        self.data = None
        if data in openinsert:
            self.data = data
            self.open = True
        elif data in closeinsert:
            self.data = data
        self.next = None
        self.prev = None
        self.tail = None
        
    def insert(self, data):
        charset = ['(',')','{','}','[',']']
        close = {'(':')','{':'}','[':']'}
        openinsert = ['(','{','[']
        closeinsert = [')','}',']']
        if data not in charset:
            return self
        prev = None
        inode = self
        while True:
            #check closure
            if not inode:
                break
            if close[inode.data] == data and data in closeinsert:            
                if inode.prev and not inode.next:
                    self.tail = inode.prev
                    inode.prev.next = None
                    return self
                elif not inode.prev and not inode.next:
                    return None
            elif not close[inode.data] == data and data in closeinsert:
                if not inode.next:
                    return 'NO'
            #check open insert
            if data in openinsert:
                ## iterate to last node and insert
                if self.tail and inode.next:
                    
                    #prev = inode
                    inode = self.tail
                else:
                    ## insert 
                    inode.next = Node(data)
                    inode.next.prev = inode
                    self.tail = inode.next
                    return self
            #check close insert
            if data in closeinsert:
                ## iterate to last node and check close insert above
                if self.tail:
                    inode = self.tail
        return self

def isBalanced(s):
    # Write your code here
    root = None
    for ch in s:
        if root:
            res = root.insert(ch)
            if res != 'NO':
                if res:
                    root = res
                else:
                    root = None
            else:
                return 'NO'
        else:
            root = Node(ch)
            if not root.open:
                return 'NO'
            if not root.data:
                root = None
    if root:
        return 'NO'        
    return 'YES'
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

t = int(input().strip())
res = []
for t_itr in range(t):
    s = input()
    if t_itr == 15:
        print(s)
    result = isBalanced(s)
    res.append(result)
    #print(result + '\n')
import testcase_balancedbrackets4_out
for i in range(t):
    ans = res[i]
    expected_ans = input().strip()
    if ans != expected_ans:
        print(i)
        print('ans: '+str(ans))
        print('expected_ans: '+ str(expected_ans))
    #fptr.close()
