# Enter your code here. Read input from STDIN. Print output to STDOUT
from ctypes.wintypes import tagRECT
## unsolved for all testcases too slow...array module adaptation 
## doesn't seem to help
from collections import deque
import array
class Node:
    def __init__(self,node_id, value=0):
        self.node_id = node_id
        self.value = value
        self.children = []
class Tree:
    def  __init__(self,N):
        self.root = None
        self.tails = None
        self.graph = None
        self.values = array.array('l',[0]*(N+1))
        self.parents = array.array('l',[-1 for x in range(N+1)])
        self.levels = array.array('l',[0 for x in range(N+1)])
        self.treepaths = {}
    def insert(self, target_id, node_id):
        if not self.root:
            self.root = target_id
            #self.root.children = [Node(node_id)]
            self.graph = {}
            #self.values[target_id] = 0
            self.graph[target_id] = [node_id]
            self.graph[node_id] = [target_id]
            # if not self.tails:
            #     self.tails = {}
            #     self.tails[self.root.node_id] = self.root
            #     self.tails[self.root.left.node_id] = self.root.left
            return self.root
        else:
            #res = [False]
            self.insert_node(target_id, node_id)
            #return res[0]

    def insert_node(self, target_id, node_id):
        if target_id in self.graph:
            self.graph[target_id].append(node_id)
        else:
            self.graph[target_id] = [node_id]
        if node_id in self.graph:
            self.graph[node_id].append(target_id)
        else:
            self.graph[node_id] = [target_id]

    def buildTreepaths(self):
        completed = set()
        nodestack = deque([[self.root,0]])
        while nodestack:
            node,level = nodestack.popleft()
            #self.treepaths[nodes[-1]] = nodes
            self.levels[node] = level
            completed.add(node)
            for child in self.graph[node]:
                if child not in completed:
                    self.parents[child] = node
                    
                    nodestack.append([child,level+1])

    def findcommonancestor(self,a, b):
        if self.levels[a] > self.levels[b]:
            for _ in range(self.levels[a] - self.levels[b]):
                a = self.parents[a]
        elif self.levels[b] > self.levels[a]:
            for _ in range(self.levels[b] - self.levels[a]):
                b = self.parents[b]
        while a != b:
            a, b = self.parents[a], self.parents[b]
        return a

    def findprevvals(self,a):
        val = 0
        a = self.parents[a]
        while a is not -1:
            val += self.values[a]
            a = self.parents[a]
        return val

    def findprevmax(self,a, stop):
        max_a = self.values[a]
        while a != stop:
            a = self.parents[a]
            if max_a > 0:
                max_a += self.values[a]
            else:
                max_a = self.values[a]
        return max_a

    def findmax(self,a, b):
        common_ancestor = self.findcommonancestor(a, b)
        ancestor_val = self.findprevvals(common_ancestor)
        max_a = self.findprevmax(a, common_ancestor)
        max_b = self.findprevmax(b, common_ancestor)
        return max(max_a, max_b) + ancestor_val
        
    def addtosubtree(self,root, n):
        self.values[root] += n

    def addValue(self, target,value):
        self.addValue_node(target,value)

    def addValue_node(self,target,value):
        if target == self.root:
            for i in range(len(self.values)):
                self.values[i] += value
            return 
        completed = set()
        target_path = self.treepaths[target]
        completed.extend(target_path[0:-1])
        nodestack = deque([[target_path[-1],False]])
        hitTarget = False
        while nodestack:
            node,trd = nodestack.popleft() #trd = target_reached
            if node == target and not trd:
                self.values[node] += value 
                trd = True
                hitTarget = True
                ## clear nodestack at subtree root
                nodestack = []
            elif trd:
                self.values[node] += value
            for child in self.graph[node]:
                if child not in completed:
                    nodestack.append([child,trd])
            completed.append(node)
        if not hitTarget:
            print('missed target: '+str(target))
            print('missed value: '+str(value))


    def findMax(self,target1,target2):
        path1 = self.findMax_node(target1)
        path2 = self.findMax_node(target2)

        #find root of path subtree
        sub_tree_start = 0
        for i,node in enumerate(path1):
            if node in path2:
                sub_tree_start = i
            else:
                break
        maxv = -1e9

        for node in path1[sub_tree_start:]:
            if self.values[node] > maxv:
                maxv = self.values[node]
        for node in path2[sub_tree_start:]:
            if self.values[node] > maxv:
                maxv = self.values[node]
        return maxv
          
    def findMax_node(self, target):
        return self.treepaths[target]

        # node_stack = [[node]]
        # completed = []
        # while node_stack:
        #     inodes = node_stack.pop()
        #     inode = inodes[-1]
        #     if inode == target:
        #         return inodes
        #     else:                
        #         for child in self.graph[inode]:
        #             if not child in completed:
        #                 il = inodes[0:]
        #                 il.append(child)
        #                 node_stack.append(il)
        #         completed.append(inode)
                    
        # return None
    
import testcase_subtreepaths6       
N = int(input())
T = Tree(N)
for i in range(N-1):
    n1,n2 = list(map(int,input().split()))
    T.insert(n1,n2)
T.buildTreepaths()
Q = int(input())
queries = []
results = []
count = 0
qmax = {}
for i in range(Q):
    q = input().split()
    if q[0] == 'add':
        qmax = {}
        T.addtosubtree(int(q[1]),int(q[2]))
    elif q[0] == 'max':
        if (int(q[1]),int(q[2])) in qmax:
            res = qmax[(int(q[1]),int(q[2]))]
            results.append(res)
            print(res)
            continue
        # if count == 61:
        #     print('error '+str(q[1]))
        #     print('error '+str(q[2]))
        res = T.findmax(int(q[1]),int(q[2]))
        qmax[(int(q[1]),int(q[2]))] = res
        print(res)
        results.append(res)
        count+=1
import testcase_subtreepaths6_out
for i,v in enumerate(results):
    ea = int(input())
    if ea != v:
        print('answer: '+str(v))
        print('eanswer: '+ str(ea))
        print(i)
