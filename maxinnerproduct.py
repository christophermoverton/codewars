#!/bin/python3

import math
import os
import random
import re
import sys
import testcase_maxinnerproduct2
class Node:
    def __init__(self,data,index):
        self.data = data
        self.right = None
        self.left = None
        self.index = index
    def insert(self, root,data,index):
        if root:
            if root.data >= data:
                if root.left:
                    self.insert(root.left,data,index)
                else:
                    root.left = Node(data,index)
            elif root.data < data:
                if root.right:
                     self.insert(root,right,data,index)
                else:
                    root.right = Node(data,index)
    def search_closest(self, root, data):
        pass

class LinkedListNode:
    def __init__(self,data,index):
        self.data = data
        self.index = index
        self.next = None
    def insert(self, root, data, index, prev=None):
        if root:
            if root.data >= data:
                if prev:
                    prev.next = LinkedListNode(data,index)
                    prev.next.next = root
                else:
                    rnode = LinkedListNode(data,index)
                    rnode.next = root
                    return rnode
            else:
                self.insert(root.next, data,index,root)
        else:
            if prev:
                prev.next = LinkedListNode(data,index)
        return root
    def insert_left_track(self, root, data, index):
        ## reverse order storage with update most current value and index 
        ## for repeating values 
        if root:
            if root.data == data:
                rnode = LinkedListNode(data,index)
                rnode.next = root.next
                return rnode
            else:
                rnode = LinkedListNode(data,index)
                rnode.next = root
                return rnode
        else:
            return LinkedListNode(data,index)
        return root
    def pop(self,root):
        return root.next
    

a = [3,10,2,1,22,14,15,2,3,8,5,3,5]
root = LinkedListNode(a[0],0)
a.pop(0)
for i,v in enumerate(a):
    root = root.insert(root,v,i)
iroot = root
while True:
    if iroot:
        print(iroot.data)
    else:
        break
    iroot = iroot.next

# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def solve(arr):
    SR = None
    SL = None
    IPmax = 0
    MaxV = 0
    Max_i = 0
    for i,v in enumerate(arr):
        # check search right stack.  This is a sorted linked list stack.
        ## linked list values are stored with left search index already
        ## added.  Note: this isn't the index of Linked list node but
        ## but the Left(i) index
        while True:
            if SR:
                if SR.data < v:
                    Left_i = SR.index
                    IP = (Left_i+1)*(i+1)
                    if IP > IPmax:
                        IPmax = IP
                    SR = SR.pop(SR)
                else:
                    break
            else:
                break
        ## check left search
        if v > MaxV:
            MaxV = v
            Max_i = i

        elif v < MaxV:
            ## search nearest neighbor index left
            # j = i-1 
            lindex = 0
            iSL = SL
            while True:
                # if j <= 0:
                #     break
                # if j < Max_i:
                #     break
                slv = None
                ilv = None
                if iSL:
                    slv = iSL.data
                    ilv = iSL.index
                else:
                    break
                if slv > v:#arr[j] > v:
                    lindex = ilv
                    break
                # j-=1
                iSL = iSL.next
            
            if SR:
                SR = SR.insert(SR,v,lindex)
            else:
                SR = LinkedListNode(v,lindex)
        if SL:
            SL = SL.insert_left_track(SL, v, i)
        else:
            SL = LinkedListNode(v,i)
    return IPmax

def solve2(arr):
    # Write your code here
    maxInnerProduct = 0
    N = len(arr)
    for i,v in enumerate(arr):
        #search left
        j = i-1
        lindex = 0
        while True:
            if j <= 0:
                break
            if arr[j] > v:
                lindex = j
                break
            j-=1
        j = 1+i
        rindex = 0
        while True:
            if j >= N:
                break
            if arr[j] > v:
                rindex = j 
                break
            j+=1
        ip = (lindex+1)*(rindex+1)
        if ip> maxInnerProduct:
            maxInnerProduct = ip
    return maxInnerProduct

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

arr_count = int(input().strip())

arr = list(map(int, input().rstrip().split()))

result = solve(arr)

print(str(result) + '\n')


