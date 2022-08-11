import itertools
import testcase_study19
N = int(input())

listn = input().split()
print(listn)
K = int(input())
k = 'a'
print(k)
plistn = list(itertools.combinations(listn,K))
print(plistn)
print(K)
permnf = []
for i in plistn:
    for j in list(i):
        if j == k:
            permnf.append(i)
            break
#permnf = [i for i in plistn if ]
print(permnf)
print('{:.12f}'.format(len(permnf)/len(plistn)))
