import testcase_kittyscalconatree
from itertools import combinations
# program to find a mother vertex in O(V+E) time
from collections import defaultdict

# This class represents a directed graph using adjacency list
# representation
class Graph2:

	def __init__(self,vertices):
		self.V = vertices #No. of vertices
		self.graph = defaultdict(list) # default dictionary

	# A recursive function to print DFS starting from v
	def DFSUtil(self, v, visited):

		# Mark the current node as visited and print it
		visited[v] = True

		# Recur for all the vertices adjacent to this vertex
		for i in self.graph[v]:
			if visited[i] == False:
				self.DFSUtil(i, visited)

	# Add w to the list of v
	def addEdge(self, v, w):
		self.graph[v].append(w)

	# Returns a mother vertex if exists. Otherwise returns -1
	def findMother(self):

		# visited[] is used for DFS. Initially all are
		# initialized as not visited
		visited =[False]*(self.V)

		# To store last finished vertex (or mother vertex)
		v=0

		# Do a DFS traversal and find the last finished
		# vertex
		for i in range(self.V):
			if visited[i]==False:
				self.DFSUtil(i,visited)
				v = i

		# If there exist mother vertex (or vertices) in given
		# graph, then v must be one (or one of them)

		# Now check if v is actually a mother vertex (or graph
		# has a mother vertex). We basically check if every vertex
		# is reachable from v or not.

		# Reset all values in visited[] as false and do
		# DFS beginning from v to check if all vertices are
		# reachable from it or not.
		visited = [False]*(self.V)
		self.DFSUtil(v, visited)
		if any(i == False for i in visited):
			return -1
		else:
			return v

# Create a graph given in the above diagram
# g = Graph(7)
# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(1, 3)
# g.addEdge(4, 1)
# g.addEdge(6, 4)
# g.addEdge(5, 6)
# g.addEdge(5, 2)
# g.addEdge(6, 0)
# print ("A mother vertex is " + str(g.findMother()))

# This code is contributed by Neelam Yadav

# Python3 implementation of the approach
N = 100000

# To keep correct and reverse direction
gr1 = {}; gr2 = {};

vis1 = [0] * N; vis2 = [0] * N;

# Function to add edges
def Add_edge(u, v) :

	if u not in gr1 :
		gr1[u] = [];
		
	if v not in gr2 :
		gr2[v] = [];
		
	gr1[u].append(v);
	gr2[v].append(u);

# DFS function
def dfs1(x) :
	vis1[x] = True;
	if x not in gr1 :
		gr1[x] = {};
		
	for i in gr1[x] :
		if (not vis1[i]) :
			dfs1(i)

# DFS function
def dfs2(x) :

	vis2[x] = True;

	if x not in gr2 :
		gr2[x] = {};
		
	for i in gr2[x] :
		if (not vis2[i]) :
			dfs2(i);

def Is_Connected(n) :

	global vis1;
	global vis2;
	
	# Call for correct direction
	vis1 = [False] * len(vis1);
	dfs1(1);
	
	# Call for reverse direction
	vis2 = [False] * len(vis2);
	dfs2(1);
	
	for i in range(1, n + 1) :
		
		# If any vertex it not visited in any direction
		# Then graph is not connected
		if (not vis1[i] and not vis2[i]) :
			return False;
			
	# If graph is connected
	return True;

# Driver code
# if __name__ == "__main__" :

# 	n = 4;

# 	# Add edges
# 	Add_edge(1, 2);
# 	Add_edge(1, 3);
# 	Add_edge(2, 3);
# 	Add_edge(3, 4);

# 	# Function call
# 	if (Is_Connected(n)) :
# 		print("Yes");
# 	else :
# 		print("No");

# # This code is contributed by AnkitRai01


class Node:
    def __init__(self, data):
        self.data = data
        self.parents = None
        self.children = None
    def insert_child(self,childnode):
        if self.children:
            self.children.append(childnode)
        else:
            self.children = [childnode]
    def insert_parent(self,parentnode):
        if self.parents:
            self.parents.append(parentnode)
        else:
            self.parents = [parentnode]
    def bfs_depth_map(self, root):
        nodestack = [root]
        levelstack = [0]
        visited = set()
        pathstack = [[root.data]]
        pathpairs = {(root.data,root.data):{'dist':0,'path':[root.data]}}
        reslevel = 0
        while True:
            if len(nodestack) == 0:
                break
            nroot = nodestack.pop()
            visited.add(nroot.data)
            level = levelstack.pop()
            path = pathstack.pop()
            if nroot.children != None:
                for child in nroot.children:
                    if not child.data in visited:
                        cpath = path[0:]
                        cpath = cpath+[child.data]
                        nodestack.insert(0,child)
                        levelstack.insert(0,level+1)
                        pathstack.insert(0,cpath[0:])  
                        pathpairs[(root.data,child.data)] = {'dist':level+1, 'path':cpath[0:]}
        return pathpairs

    def bfs_depth_map_target(self, root, target):
        target_completed = []
        nodestack = [root]
        levelstack = [0]
        visited = set()
        pathstack = [[root.data]]
        pathpairs = {(root.data,root.data):{'dist':0,'path':[root.data]}}
        
        reslevel = 0
        tsum = 0
        while True:
            if len(nodestack) == 0:
                break
            if len(target_completed) == len(target):
                break
            nroot = nodestack.pop()
            visited.add(nroot.data)
            level = levelstack.pop()
            path = pathstack.pop()
            if nroot.children != None:
                for child in nroot.children:
                    if not child.data in visited:
                        
                        cpath = path[0:]
                        cpath = cpath+[child.data]
                        nodestack.insert(0,child)
                        levelstack.insert(0,level+1)
                        pathstack.insert(0,cpath[0:])
                        if child.data in target:  
                            pathpairs[(root.data,child.data)] = {'dist':level+1, 'path':cpath[0:]}
                            tsum+= root.data*child.data*(level+1)
                            target_completed.append(child.data)
        return [pathpairs,tsum]
distmap = {}
def compute_distance2(nodemap, query):
    qs = query[0:]
    qs.sort()
    tsum = 0
    while True:
        if len(qs) == 1:
            break
        qroot_i_val = qs.pop()
        qroot_i = nodemap[qroot_i_val]
        dmap,ts = qroot_i.bfs_depth_map_target(qroot_i, qs)
        tsum+=ts
    return tsum%(7+1e9)

def compute_distance3(rootd,dmap,query):
    qs = query[0:]
    qroot_i_val = qs.pop()


def compute_distance(rootd, dmap, query):
    def compute_combs(combs):
        tsum = 0
        for comb in combs:
            if not comb in distmap:
                a,b = comb
                patha = set(dmap[(rootd,a)]['path'])
                pathb = set(dmap[(rootd,b)]['path'])
                iab = list(patha.intersection(pathb))
                dfac = 0
                if len(iab)> 1:
                    dfac = 2*(len(iab)-1)
                dista = len(dmap[(rootd,a)]['path'])-1
                distb = len(dmap[(rootd,b)]['path'])-1
                distab = dista+distb-dfac#dmap[(rootd,a)]['dist']+dmap[(rootd,b)]['dist'] - dfac
                distmap[(a,b)] = a*b*distab
                distmap[(b,a)] = a*b*distab
                tsum+=a*b*distab
            else:
                tsum+=distmap[comb]
        return tsum
    if len(query)<2:
        return 0
    tsum = 0      
    # else:
    combs = list(combinations(query,2))
    tsum=compute_combs(combs)
    
    return tsum%(7+1e9)

def find_root(nodemap):
    res = []
    for node in nodemap:
        gnode = nodemap[node]
        if not gnode.parents:
            res.append([node, gnode])
    return res

n,q = map(int,input().split())
nodemap = {}
g = Graph2(n-1)
#rootd,b = map(int,input().split())
#root = Node(rootd)
#root.insert(b)
#nodemap[rootd] = root
#nodemap[b] = root.children[-1]
for _ in range(n-1):
    a, b = list(map(int,input().split()))
    g.addEdge(a,b)
    Add_edge(a,b)
    na = None
    if not a in nodemap:
        na = Node(a)
        nodemap[a] = na
        if not b in nodemap:
            nb = Node(b)
            na.insert_child(nb)
            nb.insert_child(na)
            nodemap[b] = nb
        else: 
            nb = nodemap[b]
            na.insert_child(nb)
            nb.insert_child(na)
    else:
        na = nodemap[a]
        if not b in nodemap:
            nb = Node(b)
            na.insert_child(nb)
            nb.insert_child(na)
            nodemap[b] = nb
        else:
            nb = nodemap[b]
            na.insert_child(nb)
            nb.insert_child(na)
queries = []
#roots = find_root(nodemap)
root = g.findMother()
print(g)
print(root)
# 	# Function call
if (Is_Connected(n-1)) :
    print("Yes")
else :
    print("No")
#print(roots)

rootd = list(nodemap.keys())[0]
root = nodemap[rootd]
#root = roots[rootd]
states = [[] for i in range(n+1)]
dmap = root.bfs_depth_map(root)
print(dmap)
print(len(dmap))
pathstring = 'C:\\Users\\chris\\Documents\\'

for _ in range(q):
    n = int(input())
    query = list(map(int,input().split()))
    queries.append(query)
#queries = sorted(queries,key=lambda x: len(x),reverse=True)
import testcase_kittyscountonatree_out
for i,query in enumerate(queries):
    ans = int(input())
    res = int(compute_distance(rootd,dmap,query))#int(compute_distance2(nodemap,query))#
    #print(distmap)
    if ans != res:
        print('ans: ' +str(ans))
        print('res: '+str(res))
        print(i)
        print(query)
        break
#print(queries) 
#print(nodemap)
file = open(pathstring+'kitty.txt', 'w')
#file.write(str(dmap))
file.write(str(distmap))
file.close()
#print(dmap)
