# Enter your code here. Read input from STDIN. Print output to STDOUT
import testcase_study3
from collections import deque
from collections import OrderedDict
blocks = deque()
def checkStack(blocks,lastb):
    ## set check for shortcut
    blockset = list(OrderedDict.fromkeys(blocks))
    if len(blockset)==1:
        return 'Yes'
    if len(blocks) == 0:
        return 'Yes'
    else:
        n = len(blocks)//2
        res = 'No'
        # resl = 'No'
        # resr = 'No'
        tblocks = blocks.copy()
        while len(tblocks)> 0:
            blocks_tl = tblocks.copy()
            blocks_tr = tblocks.copy()
            popl = blocks_tl.popleft()
            popr = blocks_tr.pop()
            # print(popl)
            # print(popr)
            # print('lastb: '+str(lastb))
            # if popl <= blocks[n] and popr <= blocks[n]:
            #     return 'No'
            #print(lastb)
            if popl <= lastb and popl >= popr:
                lastb = popl
                tblocks = blocks_tl.copy()
                #print('popl: '+str(popl))
                #resl = checkStack(blocks_tl,popl)
            if popr <= lastb and popl <= popr:
                lastb = popr
                tblocks = blocks_tr.copy()
                #print('popr: '+str(popr))
                #resr = checkStack(blocks_tr,popr)
            if popr > lastb and popr > popl:
                return 'No'
            if popl > lastb and popr > lastb:
                return 'No'
            if popl > lastb and popl > popr:
                return 'No'
            if len(tblocks)==0:
                return 'Yes'
            # if resr == 'Yes':
            #     res = 'Yes'
            # if resl == 'Yes':
            #     res = 'Yes'
        return res

T = int(input())
for i in range(T):
    n = int(input())
    bls = list(map(int,input().split()))
    bls = list(OrderedDict.fromkeys(bls))
    blocks = deque(bls)
    start = max(blocks[0],blocks[-1])
    print(checkStack(blocks,start))