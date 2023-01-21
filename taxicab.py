#!/bin/python3

import math
import os
import random
import re
import sys
import testcase_taxicab2
#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER h
#  2. LONG_INTEGER v
#  3. 2D_INTEGER_ARRAY junctions
#  4. 2D_INTEGER_ARRAY edges
#

from collections import defaultdict
from collections import deque
class Node:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.prev = None
        self.next = None

def solve(h, v, junctions, edges):
    # building manhattan distance maps from junctions
    # index points to max n in junction for x,y respectively
    # aggregate the sequence of points from x_i-1 to x_i
    # intersection of min and max of point sequences 
    # from all yields manhattan rectangle for a given
    # point x_n formed by points (h+x_n, v+y_n), (x_n-h, y_n+v),
    # (x_n-h,y_n-v),and (x_n+h,y_n-v).  Note: this constructs
    # the set of all points that at a minimum fit the constraints
    # neeeded in distance search.  Points outside of such
    # rectangle are gauranteed to be outside graph 
    # search of point pairs fitting h,v constraint owing
    # to point minimum (most optimal and not pathwise) possible 
    # pathwise construction.  This reduces the possible
    # points needed in search before checking point pairs 
    # interior to the minimum manhattan distance rectangle.
    # Note: this does not gaurantee to points interior 
    # to manhattan rectangle are, in fact, pathwise,
    # minimized to h,v constraint conditions.  That 
    # still needs to be tested.  
    # As we finish point pairs for successively,
    # we can omit the i,j and j,i pairs already completed
    # creating a count hashing as an initialization for 
    # subsequent x_i
    junctions_sorted = sorted(junctions, key= lambda x: x[0],reverse=True)
    #junctions_sortedy = sorted(junctions, key=lambda x: x[1]) 

    def build_graph():
        
        graph = {}
        junct_to_index = {}
        # Loop to iterate over every
        # edge of the graph
        for edge in edges:
            a, b = edge[0], edge[1]
            
            # Creating the graph
            # as adjacency list
            if a in graph:
                graph[a].append(b)
            else:
                graph[a] = [b]
            if b in graph:
                graph[b].append(a)
            else:
                graph[b] = [a]
            
            junct_to_index[junctions[a]]=a
            junct_to_index[junctions[b]]=b
        return [graph,junct_to_index]

    
    graph,jc_index = build_graph()
    # Idea here is to implement a sweep line moving smallest x to largest x
    # coordinates on graph.  The sweep line traverses the set of nodes
    # sorted in queue the first junction sets the sweep line x position,
    # then check ahead for all points on sweepline for xpos match. Note:
    # the sweep_line_queue is noted as such.
    # Additionally there is a queue stack that contains mapped graphs already
    # traversed (not graph above which is generalized).  Let's notate these 
    # sub_graphs in the queue which allow for: 1) mapping the leaf nodes on the 
    # the sweep line (this allows for checking sweepline node in existing queue).
    # note: sub_graph_queue is named.  2) Thoughts on sub_graph_queue 
    # include added x and y manhattan distance prefix sum structures.
    # ideally this would allow for recomputing distance updates in leaf to 
    # existing subgraph fairly easy without updating all nodes in structure 
    # 3) updates to an existing sub_graph can be preformed as needed.
    # 4) after updates, re commence bfs search until new leaf nodes are 
    # commputed by constraints.  5) from sub_graph node length compute 
    # compliment of set to determine from root node all (i,j) pairs excluded
    # by constraints and apply to result sum.
    # Thus a sweepline queue allows us to set root.  Using existing sub_graph_queue
    # ,determine whether or not a new subgraph queue is created for root node, 
    # or using an existing sub_graph, constaining already computed nodes fitting 
    # to existing sub_graph, and quickly index updating within such prefix 
    # sum distance (x and y) for leaf nodes (these should be tracked so that iterative
    # searching on the sub_graph is not needed). After updating (and possibly removing)
    # leaf nodes, one can continue searching on existing leaf nodes of the sub_graph
    # new constraint determined leaf nodes.  Each sub_graph remains in the sub_graph
    # stack.
    def get_index(coord):
        return jc_index[coord]
    
    def bfs_root(sub_graph, root):
        def dist_diff(a,b):
            # used for root leaf local coordinate based
            # distance
            da = sub_graph[a]['dist'][0]-sub_graph[b]['dist'][0]
            db = sub_graph[a]['dist'][1]-sub_graph[b]['dist'][1]
            return [da,db]
        
        def dist_add(dab, coord):
            da = dab[0]+coord[0]
            db = dab[1]+coord[1]
            return [da,db]

        def update_remove_bfs(leaf,root):
            # check child in subgraph
            res = {'remove_from_subgraph':[],'leaf_adds':[]}
            nodestack = [leaf]
            while nodestack: 
                node = nodestack.pop()
                res['remove_from_subgraph'].append(node)
                for child in sub_graph[node]['children']:
                    if child in sub_graph:
                        dist = dist_diff(child,root)
                        if abs(dist[0])>h or abs(dist[1])>v:
                             nodestack.append(child)
                        else:
                            res['leaf_adds'].append(child)
            return res

        def update_add_bfs(leaf,root):
            res = {'remove_from_subgraph':[],'leaf_adds_subgraph':{}}
            nodestack = [leaf]
            nodestack_subgraph = {sub_graph[leaf]:{'dist':sub_graph[leaf]['dist'],'children':sub_graph[leaf]['children']}}
            while nodestack: 
                node = nodestack.pop()
                #res['remove_from_subgraph'].append(node)
                for child in nodestack_subgraph[node]['children']:

                    if not child in sub_graph:
                        prefix_global_dist_child = dist_add(nodestack_subgraph[node]['dist'],junctions[child])
                        root_dist = sub_graph[root]['dist']
                        hdiff = abs(root_dist[0]-prefix_global_dist_child[0])
                        vdiff = abs(root_dist[1]-prefix_global_dist_child[1])
                        if hdiff <= h and vdiff <= v:
                            nodestack_subgraph[child] = {'dist':prefix_global_dist_child,'children':graph[child]}
                            
                        dist = dist_diff(child,root)
                        if abs(dist[0])>h or abs(dist[1])>v:
                             nodestack.append(child)
                        else:
                            res['leaf_adds'].append(child)
            return res
            # for node in remove_from_subgraph:
            #     del sub_graph[node]
            #     if node in sub_graph['leaf']:
            #         sub_graph['leaf'].remove(node)

        def update_search_bfs(root):
            res = {'remove_from_subgraph':[],'leaf_adds':[]}
            leaves = sub_graph['leaf']
            for leaf in leaves:
                dist = dist_diff(leaf,root)
                if abs(dist[0])< h and abs(dist[1])<v:

        # root and index are edge graph indicies, not junction coordinates
        
            #check distance root to leaf in sub_graph
            #dist = dist_diff(leaf,root)
            #using distance from picked root relative leaf node when 
            # doing bfs.  Note local (relative) distance allows a break on the bfs 
            # search when computing the search forward.  Distances
            # however for prefix sum structure on the graph is recorded
            # via global coordinate.  This way we don't have to update
            # distances in distance summation data structure given
            # assignment of new root node per local coordinate changes
            # on the bfs.  There will need to be a backwards update bfs 
            # search to eliminate nodes that are no longer on the passed 
            # root structure.


    swqueue = deque(junctions_sorted)
    root = swqueue.pop()
    root_ind = get_index(root)
    sub_graph_dir = {root_ind:0}
    sub_graphs = [{root_ind:{'dist':[0,0],'children':graph[root_ind][0:]}, 'completed':set([tuple(root)]),'leaf':set([root_ind]),
    'finished': set()}]
    #'finished' nodes 
    # maxn = junctions_sorted[-1][0]
    # maxyn = junctions_sortedy[-1][1]
    # junctions_map = {}
    # junctions_mapy = {}
    # for a,b in junctions_sorted:
    #     if a in junctions_map:
    #         junctions_map[a].append((a,b))
    #     else:
    #         junctions_map[a] = [(a,b)]
    # for a,b in junctions_sortedy:
    #     if b in junctions_mapy:
    #         junctions_mapy[b].append((a,b))
    #     else:
    #         junctions_mapy[b] = [(a,b)]
    # # xmap will hold a search position of x range.  If there isn't  an x_i junction point in junctions_map
    # # for an index position on xmap, then forward the previous and last node from xmap index-1 position.
    # # this way we can determine a two dimensional point head and tail for the given xmap for search positions
    # # on the manhattan rectangle.  Note: this hasn't included v constraints.  This is quick search splice
    # # method of the rectangle of junction points. 
    # xmap = [0]*(maxn+1)
    # ymap = [0]*(maxyn+1)
    # for index in range(1,xmap):
    #     if index in junctions_map:
    #         prev = index-1
    #         x,y = junctions_map[index][0]
    #         node = Node(x,y)
    #         if xmap[prev]:
    #             pnode = xmap[prev][-1]
    #             pnode.next = node
    #             node.prev = pnode
    #             xmap[index] = [node]
    #         for i in range(1,len(junctions_map[index])):
    #             x,y = junctions_map[index][i]
    #             pnode = xmap[index][-1]
    #             node = Node(x,y)
    #             pnode.next = node
    #             node.prev = pnode
    #     else:
    #         prev = index-1
    #         xmap[index] = xmap[prev]
                


def solve2(h, v, junctions, edges):
    # Write your code here
    R=[h,v]
 
    # Function to build the graph
    def build_graph():
        
        graph = defaultdict(list)
        
        # Loop to iterate over every
        # edge of the graph
        for edge in edges:
            a, b = edge[0], edge[1]
            
            # Creating the graph
            # as adjacency list
            graph[a].append(b)
            graph[b].append(a)
        return graph
    
    def Is_too_far(p_1,p_2,R):
        res = False
        h_1,v_1 = p_1
        h_2,v_2 = p_2
        h_max, v_max = R
        dh = abs(h_1-h_2)
        dv = abs(v_1-v_2)
        if dh > h_max:
            res = True
        if dv > v_max:
            res = True
        resR = (h_max-dh, v_max-dv)
        return [res, resR]

    def BFS_SP(graph, start):
        explored = []
        Too_far = 0
        # Queue for traversing the
        # graph in the BFS
        queue = [[start]]
        #elements of v of DS consist of ([x_j,...,x_j+k], R)
        # where [x_j,...,x_j+k] represent node indicies
        # and R is (h_r_v, v_r_v) is the remainder distance
        DS = [] ## Distance stack

        
        # Loop to traverse the graph
        # with the help of the queue
        while queue:
            path = queue.pop(0)
            node = path[-1]
            # Condition to check if the
            # current node is not visited
            if node not in explored:
                neighbours = graph[node]
                p1 = junctions[node-1]
                # Loop to iterate over the
                # neighbours of the node
                update_DS = []
                while DS:
                    DSnode = DS.pop()
                    for neighbor in neighbours:
                        if neighbor not in explored:
                            p2 = junctions[neighbor-1]
                            ## iterate DS stack and perform update on DS
                            res = Is_too_far(p1,p2,DSnode[1])
                            if res[0]:
                                Too_far +=1
                            else:
                                update_DS.append(([],res[1]))
                DS = update_DS[0:]    
                for neighbor in neighbours:
                    if neighbor not in explored:
                        p2 = junctions[neighbor-1] 
                        res = Is_too_far(p1,p2,R)
                        if res[0]:
                            Too_far += 1
                        else:
                            DS.append(([],res[1])) 
                        new_path = list(path)
                        new_path.append(neighbor)
                        queue.append(new_path)
                    
                    # Condition to check if the
                    # neighbour node is the goal

                explored.append(node)
        return Too_far

    graph = build_graph()
    return BFS_SP(graph,1)
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

h = int(first_multiple_input[1])

v = int(first_multiple_input[2])

junctions = []

for _ in range(n):
    junctions.append(list(map(int, input().rstrip().split())))

edges = []

for _ in range(n - 1):
    edges.append(list(map(int, input().rstrip().split())))

result = solve(h, v, junctions, edges)

print(str(result) + '\n')

    ##fptr.close()
