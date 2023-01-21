n = int(input())
values = [0 for x in range(n)]
parents = [None for x in range(n)]
levels = [0 for x in range(n)]
connections = [[] for x in range(n)]

for i in range(n-1):
    a, b = [int(x)-1 for x in input().split()]
    connections[a].append(b)
    connections[b].append(a)

# iterative with queue
from collections import deque
queue = deque([(0, 0)])
visited = set()
while queue:
    node, level = queue.popleft()
    visited.add(node)
    levels[node] = level
    for i in connections[node]:
        if i not in visited:
            parents[i] = node
            queue.append((i, level+1))



def findcommonancestor(a, b):
    if levels[a] > levels[b]:
        for _ in range(levels[a] - levels[b]):
            a = parents[a]
    elif levels[b] > levels[a]:
        for _ in range(levels[b] - levels[a]):
            b = parents[b]
    while a != b:
        a, b = parents[a], parents[b]
    return a

def findprevvals(a):
    val = 0
    a = parents[a]
    while a is not None:
        val += values[a]
        a = parents[a]
    return val

def findprevmax(a, stop):
    max_a = values[a]
    while a != stop:
        a = parents[a]
        if max_a > 0:
            max_a += values[a]
        else:
            max_a = values[a]
    return max_a

def findmax(a, b):
    common_ancestor = findcommonancestor(a, b)
    ancestor_val = findprevvals(common_ancestor)
    max_a = findprevmax(a, common_ancestor)
    max_b = findprevmax(b, common_ancestor)
    return max(max_a, max_b) + ancestor_val
    
def addtosubtree(root, n):
    values[root] += n

q = int(input())
for i in range(q):
    inp = input().split()
    if inp[0] == 'add':
        addtosubtree(int(inp[1])-1, int(inp[2]))
    else:
        print(findmax(int(inp[1])-1, int(inp[2])-1))