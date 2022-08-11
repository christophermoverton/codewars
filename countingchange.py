from pickle import FALSE
from math import gcd
from itertools import permutations
from itertools import combinations
from typing import Set

def are_relatively_prime(n, m):
    return gcd(n, m) == 1

def count_change(money,coins):
    def rel_prime(cset):
        rprimed = {}
        rprimed_rev = {}
        rprimeset = set()
        worked = set()
        for i,c in enumerate(cset):
            for j,d in enumerate(cset):
                if i == j:
                    continue
                if not are_relatively_prime(c,d):
                    m = gcd(c,d)
                    n = max(c,d)
                    if not m in rprimed and not m in worked:
                        rprimed[m] = [max(c,d)]
                        worked.add(c)
                        worked.add(d)
                        rprimeset.add(max(c,d))
                    elif m in rprimed and m in worked:
                        rprimed[m].append(max(c,d))
                        rprimeset.add(max(c,d))
        for rprime in rprimed:
            rset = rprimed[rprime]
            nrset = list(set(rset))
            nrset.sort()
            rprimed[rprime] = nrset
        for rprime in rprimed:
            vals = rprimed[rprime]
            for val in vals:
                if not val in rprimed_rev:
                    rprimed_rev[val] = [rprime]
                else:
                    rprimed_rev[val].append(rprime)
        res = set(cset).difference(rprimeset)
        return [list(res), rprimed,rprimed_rev]

    def combination_sum(msum,cpcoins):
        ans = []
        temp = []
        rec_coins_add(ans,temp,msum, cpcoins, 0)
        return ans
    def rec_coins_add(ans,temp,msum,coins,index):
        if msum == 0:
             ans.append(temp[0:])
        else:
            for i in range(index,len(coins)):
                if (msum - coins[i]) >= 0:
                    temp.append(coins[i])
                    rec_coins_add(ans,temp,msum-coins[i],coins,i)
                    temp.remove(coins[i])

    def generate_sets3(cset,n = 'all'):
        ## n in range all or specific ranges
        rsets = {}
        nrsets = {}
        cpairsets = set()
        x = 0
        if n == 'all':
            x = range(0,len(cset)-1)
        else: 
            x = n
        for i in x:
            rsets[i+1] = set(combinations(cset,i+1))
        if n == 'all':
            nset = set()
            nset.add(tuple(cset))
            rsets[len(cset)] = nset
        print(rsets)
        return rsets  

    def convert_s(adict):
        rset = set()
        for key in adict:
            for s in adict[key]:
                rset.add(s)
        return rset 
    
    def key_combination_sum(csums):
        print(csums)
        rsums = {}
        for sum_c in csums:
            key = []
            keydict = {}
            m = None
            count = 0
            for i in sum_c:
                if i != m:
                    if not m == None:
                        key.append(m)
                        keydict[m] = count
                        
                    m = i
                    count = 1♣
                else:
                    count +=1
            key.append(m)
            keydict[m] = count
            if tuple(key) in rsums:
                rsums[tuple(key)].append(keydict)
            else:
                rsums[tuple(key)] = [keydict] 
        return rsums   
    
    msum = money
    coins_adds = []

    ccoins =  coins[0:]
    ccoins.sort()
    ## build relatively prime set
    rprimeset = rel_prime(ccoins)
    print(rprimeset)
    rpdictsets = generate_sets3(rprimeset[0])
    tdictsets = generate_sets3(ccoins)
    rpsets = convert_s(rpdictsets)
    tsets = convert_s(tdictsets)
    un_counted = tsets.difference(rpsets)
    print(un_counted)
    #print(tsets)
    x = combination_sum(msum, rprimeset[0])
    keyedsums = key_combination_sum(x)
    print(keyedsums)
    return len(x)
    print(len(x))
    print(x)

# def count_change2(money, coins):
#     # your implementation here
#     def factors(x):
#         rfac = set()
#         for i in range(1, x + 1):
#             if x % i == 0:
#                 rfac.add(i)
#         return rfac
#     def generate_sets(cset):
#         rsets = {}
#         for i,c in enumerate(cset):
#             rsets[i+1] = [[]]
#         for i,c in enumerate(cset):
#             for j,rset in enumerate(rsets):
#                 rarrs = rsets[rset]
#                 # rarr = rarrs[len(rarrs)-1]
#                 for arr in rarrs:
#                     if len(arr) < rset:
#                         arr.append(c)
#                 if i != 0:
#                     narr = [c]
#                     rarrs.append(narr)
#         for rid in rsets:
#             rset = rsets[rid]
#             nrset = []
#             for i, arr in enumerate(rset):
#                 if len(arr) == rid:
#                     nrset.append(arr)
#             rsets[rid] = nrset
#         return rsets

#     def generate_sets2(cset,n = 'all'):
#         ## n in range all or specific ranges
#         rsets = {}
#         nrsets = {}
#         cpairsets = set()
#         x = 0
#         if n == 'all':
#             x = range(0,len(cset)-1)
#         else: 
#             x = n
#         for i in x:
#             rsets[i+1] = set(permutations(cset,i+1))
#         for i,c in enumerate(rsets):
#             tset = rsets[c]
#             nset = set()
#             for pair in tset:
#                 if not pair in cpairsets and not pair[::-1] in cpairsets:
#                     nset.add(pair)
#                     cpairsets.add(pair)
#             nrsets[c] = nset
#         if n == 'all':
#             nset = set()
#             nset.add(tuple(cset))
#             nrsets[len(cset)] = nset
#         print(nrsets)
#         return nrsets

#     def generate_sets3(cset,n = 'all'):
#         ## n in range all or specific ranges
#         rsets = {}
#         nrsets = {}
#         cpairsets = set()
#         x = 0
#         if n == 'all':
#             x = range(0,len(cset)-1)
#         else: 
#             x = n
#         for i in x:
#             rsets[i+1] = set(combinations(cset,i+1))
#         # for i,c in enumerate(rsets):
#         #     tset = rsets[c]
#         #     nset = set()
#         #     for pair in tset:
#         #         if not pair in cpairsets and not pair[::-1] in cpairsets:
#         #             nset.add(pair)
#         #             cpairsets.add(pair)
#         #     nrsets[c] = nset
#         if n == 'all':
#             nset = set()
#             nset.add(tuple(cset))
#             nrsets[len(cset)] = nset
#         print(nrsets)
#         return nrsets         

#     def compute_count(lset, money):
#         ans = []
#         temp = [1 for i in lset]
#         for i in range(0,len(lset)):


#     def check_set_factor(cset, mfacs, money):
        
#         checkset = {}
#         for cid in cset:
#             checkset[cid] = False
#         if len(cset) == 1:
#             if cset[0] in mfacs:
#                 return True
#             else:
#                 return False
#         # csubsets = generate_sets(cset)
        
#         # for cid in csubsets:
#         #     arrs = csubsets[cid]
#         #     for arr in arrs:
#         if 1 in cset:
#             for id in cset:
#                 checkset[id] = True
#         sarr = sum(cset)
#         if sarr <= money and sarr in mfacs:
#             for id in cset:
#                 checkset[id] = True
#         rbool = True
#         for id in checkset:
#             if not checkset[id]:
#                 rbool = False
#                 break
#         return rbool
            
#     mfacs = factors(money)        
#     print (mfacs)
#     c2 = generate_sets2(coins)
#     print(c2)
#     rcount = 0
#     for id in c2:
#         coin_set = c2[id]
#         for coins in coin_set:
#             if check_set_factor(coins,mfacs,money):
#                 rcount+=1
#     return rcount

print(count_change(4,[1,2]))
print(count_change(10, [5,2,3]))
print(count_change(11, [5,7]))
count_change(98, [3,8,14])
print(count_change(200, [2,3,5,10,15,20]))