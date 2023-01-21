# Enter your code here. Read input from STDIN. Print output to STDOUT
import testcase_mergecommunities3
n,q = list(map(int,input().split()))
comms = [1 for i in range(n+1)]
merge = [None for i in range(n+1)]
#graph = {i:[] for i in range(n+1)}
#res = []
from collections import deque
for i in range(q):
    qlist = input().split()
    qt = qlist[0]
    temp = deque([])
    if qt == 'M':
        ij = qlist[1:]
        i,j = list(map(int,ij))
        if i == j:
            continue
        while merge[i] != None:
            i = merge[i]
        while merge[j] != None:
            temp.append(j)
            j = merge[j]
        if i != j:
            merge[j] = i
            for key in temp:
                merge[key] = i
            comms[i]+=comms[j]
    if qt == 'Q':
        ij = qlist[1:][0]
        i = int(ij)
        while merge[i] != None:
            temp.append(i)
            i = merge[i]
        for j in temp:
            merge[j] = i
        print(comms[i])
        #res.append(comms[i])

# import testcase_mergecommunities3_out
# for i in range(len(res)):
#     a = res[i]
#     ea = int(input())
#     if a != ea:
#         print('ea: '+str(ea))
#         print('a: '+str(a))
#         print(i)

            
