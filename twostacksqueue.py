# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
import testcase_twostacksqueue
stack = deque()
q = int(input())
for _ in range(q):
    vals = list(map(int,input().rstrip().split()))
    typ, val = None,None
    if len(vals)>1:
        typ,val = vals
    else:
        typ = vals[0]
    if typ == 1:
        stack.append(val)
    elif typ == 2:
        stack.popleft()
    elif typ == 3:
        print(stack[0])
