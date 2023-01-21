#!/bin/python

import heapq
from sys import hash_info
from tkinter import E

class TreeNode():
    # It instantiates the class
    def __init__ (self, val):
        self.val = val
        self.place = 0
        self.height = 1
        self.cnt = 1
        self.rep = 0
        self.left = None
        self.right = None

# Self Balancing Binary Search Tree based on the type of AVL Trees
class sbbst():
    # It instantiates the class O(1)
    def __init__(self, valslist = None):
        self.head = None
        self.N = 0
        self.count = 0
        self.sizes = []
        self.sumsizes = []
        self.listInOrder = []
        if type(valslist) == list:
            for val in valslist:
                self.head = self.insertNode(self.head, val)

    # It return True if the val is found, False otherwhise O(logN)
    def search(self, node, val):
        if not node:
            return False
        else:
            if node.val < val:
                return self.search(node.right, val)
            elif val < node.val:
                return self.search(node.left, val)
            else:
                return True

    # It inserts a node and updates the head node O(logN)
    def insert(self, val):
        self.head = self.insertNode(self.head, val)
    
    # It inserts a node with a value and returns the node of the modified subtree O(logN)
    def insertNode(self, node, key):
        # Step 1 - Perform normal BST
        if not node:
            self.N += 1
            return TreeNode(key)
        
        elif key < node.val:
            node.cnt +=1
            node.left = self.insertNode(node.left, key)
        elif key > node.val:
            node.cnt +=1
            node.right = self.insertNode(node.right, key)
        else:
            node.cnt +=1
            node.rep +=1
            self.N +=1
        
        # 2: Update the height of the node
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        # 3: Get the balance factor
        balance = self.getBalance(node)
        # 4: If the node is unbalanced, try out the 2 cases
        if balance > 1: # Case 1: Left (Left/Right)
            if key > node.left.val:
                node.left = self.leftRotate(node.left)
            return self.rightRotate(node)
        if balance < -1: # Case 2: Right (Left/Right)
            if key < node.right.val:
                node.right = self.rightRotate(node.right)
            return self.leftRotate(node)
        # Return the result node
        return node

    # It deletes a node with a certain value and updates the head node O(logN)
    def delete(self, val):
        self.head = self.deleteNode(self.head, val)

    # It deletes a node with a certain value and returns the node of the modified subtree O(logN)
    def deleteNode(self, node, key):
        # 1: Standard BST delete
        if not node:
            return node

        elif key < node.val:
            node.cnt-=1
            node.left = self.deleteNode(node.left, key)
        elif key > node.val:
            node.cnt -=1
            node.right = self.deleteNode(node.right, key)

        else: # key == node.val  
            if node.rep == 0:          
                if node.left is None:
                    self.N -= 1
                    temp = node.right
                    node = None
                    return temp
                elif node.right is None:
                    self.N -= 1
                    temp = node.left
                    node = None
                    return temp
                else: # node.left and node.right
                    temp = self.getMinValueNode(node.right)
                    node.val = temp.val
                    node.cnt -=1
                    node.right = self.deleteNode(node.right, temp.val)
            else:
                node.cnt -=1
                node.rep -=1
                self.N -=1

        # Return None if there is no more nodes
        if node is None:
            return node
        # 2: Update the height of the node
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        # 3: Get the balance factor
        balance = self.getBalance(node)
        # 4: If the node is unbalanced, try out the 2 cases
        if balance > 1: # Case 1: Left (Left/Right)
            if self.getBalance(node.left) < 0:
                node.left = self.leftRotate(node.left)
            return self.rightRotate(node)
        if balance < -1:# Case 2: Right (Right/Left)
            if self.getBalance(node.right) > 0:
                node.right = self.rightRotate(node.right)
            return self.leftRotate(node)
        # Return the result node
        return node 
    
    # It rotates the tree to the left and returns the node O(1)
    def leftRotate(self, node):
        rnode = node.right
        T = rnode.left
        # Perform rotation
        rnode.left = node
        node.right = T
        nodelcnt = node.left.cnt if node.left else 0
        Tcnt = T.cnt if T else 0
        node.cnt = Tcnt + nodelcnt+ 1+node.rep
        rnodercnt = rnode.right.cnt if rnode.right else 0
        rnode.cnt = rnode.left.cnt + rnodercnt + 1 + rnode.rep
        # Update heights
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        rnode.height = 1 + max(self.getHeight(rnode.left), self.getHeight(rnode.right))
        # Return the new node
        return rnode

    # It rotates the tree to the right and returns the node O(1)
    def rightRotate(self, node):
        lnode = node.left
        T = lnode.right
        # Perform rotation
        lnode.right = node
        node.left = T
        nodercnt = node.right.cnt if node.right else 0
        Tcnt = T.cnt if T else 0
        node.cnt = Tcnt + nodercnt+ 1 + node.rep
        lnodelcnt = lnode.left.cnt if lnode.left else 0
        lnode.cnt = lnode.right.cnt + lnodelcnt + 1 + lnode.rep
        # Update heights
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        lnode.height = 1 + max(self.getHeight(lnode.left), self.getHeight(lnode.right))
        # Return the new node
        return lnode

    # It returns the height of a node O(1)
    def getHeight(self, node):
        if not node:
            return 0
        return node.height

    # It returns the balance of the node O(1)
    def getBalance(self, node): 
        if not node:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    # It returns the min Node O(logN)
    def getMinValueNode(self, node):
        if node is None or node.left is None:
            return node
        return self.getMinValueNode(node.left)

    # It returns the min value of the Tree O(logN + K)
    def kthsmallest(self, K):
        if K < 0:
            print('There are not enough elements in the Tree')
            return None
        elif self.N//2+1 < K:
            return self.kthlargest(self.N+1-K)
        else:
            stack = []
            node = self.head
            while(stack or node):
                if node:
                    stack.append(node)
                    node = node.left
                else:
                    node = stack.pop()
                    if K == 1:
                        return node.val
                    else:
                        K -= 1
                    node = node.right
    
    # It returns the max value of the Tree O(losgN + K)
    def kthlargest(self, K):
        if K < 0:
            print('There are not enough elements in the Tree')
            return None
        elif self.N//2+1 < K:
            return self.kthsmallest(self.N+1-K)
        else:
            stack = []
            node = self.head
            while(stack or node):
                if node:
                    stack.append(node)
                    node = node.right
                else:
                    node = stack.pop()
                    if K == 1:
                        return node.val
                    else:
                        K -= 1
                    node = node.left

    # It returns the min value of the Tree O(logN + K)
    def getMinVal(self, node=-1):
        if node == -1:
            if self.head == None:
                print('No elements in the Tree')
                return float('inf')
            else:
                node = self.head
        if node.left:
            return self.getMinVal(node.left)
        else:
            return node.val

    # It returns the max value of the Tree O(logN)
    def getMaxVal(self, node=-1):
        if node == -1:
            if self.head == None:
                print('No elements in the Tree')
                return float('-inf')
            else:
                node = self.head
        if node.right:
            return self.getMaxVal(node.right)
        else:
            return node.val

    # It returns the number of elements in the Tree O(1)
    def getSize(self):
        return self.N
    
    # It returns the height of the Tree O(1)
    def getHeightTree(self):
        if self.head == None:
            return 0
        return self.head.height

    def findMedian(self, root):
        if (root == None):
            return 0
        count = self.N
        current = root
        prev = None
        target = count//2+1
        targets = []
        completed = {}
        index = 1
        # print('current: '+str(current.val))
        # print('target: '+str(target))
        # start 1 indexing  
        while (current != None):
            if prev:
                if current.left:
                    index = current.left.cnt+1+prev
                else:
                    index = prev+1
            else:
                if current.left:
                    index = current.left.cnt+1
                else:
                    index = 1
            indicies = [index+i for i in range(current.rep+1)]
            minindex = min(indicies)
            maxindex = max(indicies)
            if minindex > target:
                completed[index] = current.val
                current = current.left if current.left else None
            elif maxindex < target:
                prev = maxindex
                completed[index] = current.val
                current = current.right if current.right else None
            else:
                if count%2==0:
                    if targets:
                        return (current.val+targets.pop())/2
                    elif not targets and target-1 in completed:
                        return (current.val+completed[target-1])/2
                    elif not targets and target-1 in indicies:
                        return current.val
                    else:
                        completed[index] = current.val
                        targets.append(current.val)
                        target = target-1
                        current = root
                        # print('restarting root')
                        prev = None
                        # if index > target:
                        #     current = current.left if current.left else None
                        # else:
                        #     prev = index
                        #     current = current.right if current.right else None
                else:
                    return current.val

    def inOrder(self, node=-1):
        if node == -1:
            node = self.head
        if node:
            return self.inOrder(node.left) + [node.val] + self.inOrder(node.right)
        else:
            return []

res = []
hashsvl = {}
def medin(a,x):
    svl = sbbst()
    root = svl.head
    for i,aop in enumerate(a):
        if aop == 'a':            
            v = x[i]
            svl.insert(v)
            if v in hashsvl:
                hashsvl[v] +=1
            else:
                hashsvl[v] = 1
            root = svl.head
            median = svl.findMedian(root)
            if median == int(median):
                median = int(median)
            res.append(str(median))
            print(median)
            #print(svl.inOrder())
        elif aop == 'r':
            v = x[i]
            N = svl.N
            if v in hashsvl:
                svl.delete(v)
                if hashsvl[v] > 1:
                    hashsvl[v]-=1
                else:
                    del hashsvl[v]
            # if svl.search(svl.head,v):
            #     resd = svl.delete(v)
            if N == svl.N:
                res.append('Wrong!')
                print('Wrong!')
                continue
            if not hashsvl:
                res.append('Wrong!')
                print('Wrong!')
                continue
            root = svl.head
            median = svl.findMedian(root)
            if median == int(median):
                median = int(median)
            res.append(str(median))
            print(median)


def medin2(a,x):
    arr = []
    for i,aop in enumerate(a):
        v = x[i]
        if aop == 'a':
            heapq.heappush(arr,v)
            arr.sort()
            m = len(arr)
            if m%2==0:
                mid = m//2-1
                avgm = (arr[mid]+arr[mid+1])/2
                avgm = int(avgm) if avgm ==int(avgm) else avgm 
                res.append(str(avgm))
                print(avgm)
            else:
                mid = m//2
                res.append(str(arr[mid]))
                print(arr[mid])
        elif aop == 'r':
            if v not in arr:
                res.append('Wrong!')
                print('Wrong!')
            else:
                arr.remove(v)
                arr.sort()
                m = len(arr)
                if m%2==0 and m !=0:
                    mid = m//2-1
                    avgm = (arr[mid]+arr[mid+1])/2
                    avgm = int(avgm) if avgm ==int(avgm) else avgm
                    res.append(str(avgm)) 
                    print(avgm)
                elif m%2!=0 and m!=0:
                    mid = m//2
                    res.append(str(arr[mid]))
                    print(arr[mid])  
                else:
                    res.append('Wrong!')
                    print('Wrong!')              
import testcase_medianupdates                
N = int(input())
s = []
x = []
for i in range(0, N):
   tmp = input().strip().split(' ')
   a, b = [xx for xx in tmp]
   s.append(a)
   x.append(int(b))
medin(s,x)
# import testcase_medianupdates4_out
# for i in range(N):
#     ea = input()
#     if res[i] != ea:
#         print('eans: '+ str(ea))
#         print('ans: '+ str(res[i]))
#         print(i)
