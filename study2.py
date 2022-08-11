# Enter your code here. Read input from STDIN. Print output to STDOUT
import testcase
from collections import defaultdict
d = defaultdict(list)
A=[]
B=[]
m, n = map(int, input().split())
for i in range(m):
    val = str(input())
    d[m].append(val)
    A.append(val)
for i in range(n):
    val = str(input())
    d[n].append(val)
    B.append(val)
ostr = ""
B = list(B)
#B.sort()
for val in B:
    if val in A:
        indval = [i for i,el in enumerate(d[m]) if el == val]
        
        for i,el in enumerate(indval):
            if i == len(indval)-1:
                ostr+=str(el+1)
            else:
                ostr+=str(el+1)+" "
        print(ostr)
        ostr=""
    else:
        print("-1")  