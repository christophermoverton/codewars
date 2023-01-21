#!/bin/python3

import math
import os
import random
import re
import sys
import testcase_swapnodes
sys.setrecursionlimit(20000)
class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
# Insert Node
   def insert(self,leftnode, rightnode):
      self.left = Node(leftnode)
      self.right = Node(rightnode)
      
# Print the Tree
   def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print( self.data),
      if self.right:
         self.right.PrintTree()
# Inorder traversal
# Left -> Root -> Right
   def inorderTraversal(self, root):
      res = []
      if root:
         res = self.inorderTraversal(root.left)
         if root.data != None:
            res.append(root.data)
         res = res + self.inorderTraversal(root.right)
      return res
#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#

def swapNodes(indexes, queries):
    # Write your code here
    sroot = Node(1)
    root = sroot
    indexes_r = indexes[::-1]
    #print(indexes_r)
    nodestack = [root]
    while True:
        if (len(nodestack) == 0):
            break
        root = nodestack.pop()
        vleft,vright = indexes_r.pop()
        if vleft == -1:
            vleft = None
        if vright == -1:
            vright = None
        
        root.insert(vleft,vright)
        # print('root:'+str(root.data))
        # print('root.left:' +  str(root.left.data))
        # print('root.right:'+str(root.right.data))
        # print('vleft: '+str(vleft))
        # print('vright:'+str(vright))
        if vleft != None:
            nodestack.insert(0,root.left)
        if vright != None:
            nodestack.insert(0,root.right)
    print(sroot.inorderTraversal(sroot))
    k = 0
    for q in queries:
        k = q
        levelstack = [0]
        nodestack = [sroot]
        while True:
            if (len(nodestack) == 0):
                break
            root = nodestack.pop() 
            level = levelstack.pop()
            if (level+1) % k == 0 and (level+1) != 0:
                prevl = root.left
                #prevr = root.right
                root.left = root.right 
                root.right = prevl
            if root.left != None:
                nodestack.insert(0,root.left)
                levelstack.insert(0,level+1)
            if root.right != None:
                nodestack.insert(0,root.right)
                levelstack.insert(0,level+1)
        otrav = sroot.inorderTraversal(sroot)
        ostr = ''
        for i in otrav:
            ostr+=str(i)+' '
        print(ostr)

n = int(input().strip())

indexes = []

for _ in range(n):
    indexes.append(list(map(int, input().rstrip().split())))

queries_count = int(input().strip())

queries = []

for _ in range(queries_count):
    queries_item = int(input().strip())
    queries.append(queries_item)

result = swapNodes(indexes, queries)

#print('\n'.join([' '.join(map(str, x)) for x in result]))
    #fptr.write('\n')

    #fptr.close()
