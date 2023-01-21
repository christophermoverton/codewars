# Enter your code here. Read input from STDIN. Print output to STDOUT
import testcase_arraysqueries3
import array
n,m = list(map(int,input().split()))
arr = array.array('i',map(int,input().split()))
queries = []

for _ in range(m):
    typ,start,end = list(map(int,input().split()))
    if typ == 1:
        arr = arr[start-1:end] + arr[:start-1] + arr[end:]
    elif typ == 2:
        arr = arr[:start-1] + arr[end:] + arr[start-1:end]
        #arr.extend(subarr.copy())
line1 = abs(arr[0]-arr[-1])
print(abs(arr[0]-arr[-1]))
ostr = ''
for i in arr:
    ostr+=str(i)+' '
print(ostr)
import testcase_arraysqueries3_out
eline1 = int(input())
earr = list(map(int,input().split()))
for i,v in enumerate(earr):
    if v!=arr[i]:
        print('eans: '+str(v))
        print('ans: '+ str(arr[i]))
        print(i)
    