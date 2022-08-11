import itertools
import testcase_study20
K,M = map(int,input().split())
Klists = []
for i in range(K):
    l = list(map(int,input().split()))
    # l = list(set(l))
    l=l[1:]
    Klists.append(l)
# NKlists = []
# for i in Klists:
#     NKlists+=i[0:]
# NKlists = list(set(NKlists))
Klistpicks=list(itertools.product(*Klists))
#Klistpicks = {}
# print(Klists)
# def recursion_Klist(k_index,pick_indicies):
#     # print(pick_indicies)

#     if len(pick_indicies) < K:
#         for i in Klists[k_index]:
#             pinew = pick_indicies.copy()
#             pinew.append(i)
#             recursion_Klist(k_index+1,pinew)
#     else:
#         # print(pick_indicies)
#         if not tuple(pick_indicies) in Klistpicks:
#             Klistpicks[tuple(pick_indicies)] = 1
# pindex = []
# recursion_Klist(0,pindex)

print(len(Klistpicks))
sumdict = {}
def K_pick_sum_square_mod_M(kpick,M): 
    sumk = 0
    for xi in kpick:
        sumk+=xi**2
    return sumk%M
Sumlist=[]
for kpick in Klistpicks:
    # smt = 0
    # if kpick in sumdict:
    #     smt = sumdict[kpick]
    # else:
    smt = K_pick_sum_square_mod_M(kpick,M)
    if smt == 766:
        print('smt: '+ str(smt))
        print('kpick: '+str(kpick))
    elif smt == 763:
        print('smt: '+ str(smt))
        print('kpick: '+str(kpick))
    # if not kpick in sumdict:
    #     sumdict[kpick] = smt
    Sumlist.append(smt)
print(max(Sumlist))