#!/bin/python3

import math
import os

import random
import re
import sys
from itertools import combinations
#from collections import SortedSet
from sortedcontainers import SortedSet
from collections import OrderedDict
import numpy
import bisect
import testcase_study25_2
import timeit
import time
def long_function():
    print('function start')
    time.sleep(5)
    print('function end')

#
# Complete the 'similarPair' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. 2D_INTEGER_ARRAY edges
#
class bnt:
    def __init__(self,data):
        self.data = data 
        self.left = None
        self.right = None

    def insert(self, node):
        if self.data < node:
            if self.left == None:
                self.left = bnt(node)
            else:
                self.left.insert(node)
        elif self.data > node:
            if self.right == None:
                self.right = bnt(node)
            else:
                self.right.insert()
    def count_traversal_similiar(self,k):
        count = 0
        stack = [self.data]
        completed = set([self.data])
        current = None
        current_path = None
        stack_path = [self.data]
        while True:
            if len(stack) == 0:
                break
            if current == None:
                current = stack.pop()
                current_path = stack_path.pop()
            current_path_sort = current_path[0:].sort()
            #search first and last index of sorted
            if self.left != None:
                for i in [self.left.data]: 
                    lbi = numpy.searchsorted(current_path_sort,i-k,side='left')
                    ubi = numpy.searchsorted(current_path_sort,i+k,side='right')
                    v1 = current_path_sort[lbi]
                    #v2 = current_path_sort[ubi]
                    n = ubi - lbi
                    count+=n
                stack_path.append(self.left.data)
                stack.append(self.left)
            if self.right != None:
                for i in [self.right.data]: 
                    lbi = numpy.searchsorted(current_path_sort,i-k,side='left')
                    ubi = numpy.searchsorted(current_path_sort,i+k,side='right')
                    v1 = current_path_sort[lbi]
                    #v2 = current_path_sort[ubi]
                    n = ubi - lbi
                    count+=n
                stack_path.append(self.right.data)
                stack.append(self.right)
        return count
                            
def similarPair2(n,k,edges):
    def build_bnt(edges):
        a,b = edges[0]
        root = bnt(a)
        root.insert(b)
        for edge in edges[1:]:
            a,b = edge
            root.insert()
            
def similarPair(n, k, edges):
    # Write your code here
    def build_graph(edges):
        graph = {}
        for edge in edges:
            a,b = edge
            if a in graph:
                graph[a]['children'].append(b)
            else:
                graph[a] = {'parent':[],'children':[b]}
            if b in graph:
                graph[b]['parent'].append(a)
            else:
                graph[b]= {'parent': [a], 'children':[]}
        return graph
    def find_root(graph):
        roots = []
        for node in graph:
            if len(graph[node]['parent']) == 0:
                roots.append(node)
        return roots
    paths = [] ## out of recursive def traverse_graph return 
    def traverse_graph(node,graph,path):
        graphc = graph.copy()
        stack = [node]
        stack_track = []
        current = None
        count = 0
        a = [0 for i in range(4*n)]
        def add(x, v):
            #x += 1
            while x <= n:
                a[x] += v
                x += x & -x

        def que(x):
            #x += 1
            if x <= 0:
                return 0
            ret = 0
            x = min(n, x)
            while x > 0:
                ret += a[x]
                x -= x & -x
            return ret
        add(node,1)
        while True:
            if current == None:
                if len(stack)==0:
                    break
                else:
                    current = stack.pop()
                    
            if len(graphc[current]['children']) ==0:
                if not len(stack) == 0:
                    
                    next_child = stack[-1]
                    while True:
                        childp = stack_track.pop()
                        if childp == next_child:
                            break
                        else:
                            add(childp,-1)
                else:
                    break
                current = None
            else: 
                children = graphc[current]['children']
                child = children.pop()
                if children:
                    stack.append(current)
                    stack_track.append(current)
                stack.append(child)
                stack_track.append(child)
                count+=que(child+k)-que(child-k-1)
                add(child,1)
                current = None
        return count    
    count = 0
    graph = build_graph(edges)
    #print(graph)
    roots = find_root(graph)
    #print(roots)
    for root in roots:
        count += traverse_graph(root,graph,[root])
    #print(paths)
    return count            
                
                


def similarPair3(n, k, edges):
    # Write your code here
    spairs = set()
    not_spairs = set()
    completed = set()
    def build_graph(edges):
        graph = {}
        count = 0
        for edge in edges:
            a,b = edge
            if abs(a-b)<=k:
                spairs.add(tuple(edge))
                count+=1
            else:
                not_spairs.add(tuple(edge))
            if a in graph:
                graph[a]['children'].append(b)
                ##graph[a]['child_2_3'] = True
            else:
                graph[a] = {'parent':[],'children':[b],'child_2_3':False}
            if b in graph:
                graph[b]['parent'].append(a)
            else:
                graph[b]= {'parent': [a], 'children':[],'child_2_3':False}
        return [graph,count]
    def find_root(graph):
        roots = []
        for node in graph:
            if len(graph[node]['parent']) == 0:
                roots.append(node)
        return roots
    paths = [] ## out of recursive def traverse_graph return 
    def traverse_graph(node,graph,path):
        graphc = graph.copy()
        #path_track ={node:[node]}
        path_track = [node]
        stack = [node]
        stack_track = []
        current = None
        count = 0
        count2 = 0
        completed = SortedSet()
        completed.add(node)
        while True:
            if current == None:
                if len(stack)==0:
                    break
                else:
                    current = stack.pop()
                    
            if len(graphc[current]['children']) ==0:
                plist = path_track.copy()
                #pset_unordered=set(plist)
                pset = SortedSet(plist)
                psetltr = pset.intersection(completed)
                plistltr = psetltr
                minp = plistltr[0]; maxp = plistltr[-1]
                pdiff = pset.difference(psetltr)
                #print(pdiff)
                minpd = pdiff[0]; maxpd = pdiff[-1]
                                
                # for i in list(pset.difference(psetltr)):
                t1 = abs(minp-minpd)<=k 
                t2 = abs(maxp-maxpd)<=k
                t3 = abs(minp-maxpd)<=k
                t4 = abs(maxp-minpd)<=k
                t5 = abs(minpd-maxpd)<=k
                lenpdiff = len(pdiff)-1
                lpdifn = lenpdiff*(lenpdiff+1)//2
                if t1 and t2 and t3 and t4 and t5:
                    count+=len(plistltr)*len(pdiff)+lpdifn
                    #completed = completed.union(SortedSet(pdiff))
                else:
                    plist_ordered = list(psetltr)
                    pdiff_orig_i = []
                    pdiff_l = list(pdiff)
                    for i in range(len(plist)-1,0,-1):
                        if plist[i] in pdiff_l:
                            pdiff_orig_i.append(i)
                        if len(pdiff_orig_i) == len(pdiff_l):
                            break 
                    pdiff_orig_i.sort(); pdiff_orig = [plist[i] for i in pdiff_orig_i];
                    checkback = [] ## to check match on completed pdiff_orig ancestors
                    for i in pdiff_orig:
                        lbi = numpy.searchsorted(plist_ordered,i-k,side='left')
                        ubi = numpy.searchsorted(plist_ordered,i+k,side='right')
                        n = ubi - lbi
                        count+=n
                        lbi = numpy.searchsorted(checkback,i-k,side='left')
                        ubi = numpy.searchsorted(checkback,i+k,side='right')
                        n = ubi - lbi
                        count+=n
                        checkback.append(i)
                        checkback.sort()
                completed = completed.union(SortedSet(pdiff))
                if not len(stack) == 0:
                    count2 +=1
                    next_child = stack[len(stack)-1]
                    while True:
                        childp = stack_track.pop()
                        if childp == next_child:
                            break
                        else:
                            path_track.pop()##.remove(childp)
                else:
                    break
                current = None
            else: 
                children = graphc[current]['children']
                child = children.pop()
                if len(children)>0:
                    stack.append(current)
                    stack_track.append(current)
                    graphc[current]['child_2_3'] = True
                stack.append(child)
                stack_track.append(child)
                path_track.append(child)
                current = None
        #print(count2) 
        return count
        
    count = 0
    graph,count2 = build_graph(edges)
    #print(graph)
    roots = find_root(graph)
    #print(roots)
    for root in roots:
        count += traverse_graph(root,graph,[root])
    #print(paths)
    return count

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    edges = []

    for _ in range(n - 1):
        edges.append(list(map(int, input().rstrip().split())))
    #
    result = similarPair(n, k, edges)

    print(str(result))
    
    #fptr.close()
