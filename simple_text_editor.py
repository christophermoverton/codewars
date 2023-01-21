# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import testcase_simple_text_editor
prev = []
def operation(op, S):
    res = S
    op_i = int(op[0])
    if op_i == 1:
        prev.append(S)
        W = op[1]
        W = list(map(str,W))
        res = list(map(str,res))
        while W:
            w = W.pop(0)
            res.append(w)
            
        res = ''.join(res)

    elif op_i == 2:
        k = int(op[1])
        prev.append(S)
      
        res = list(map(str,res))
        while k:
            delv = res.pop()
        
            k-=1
        res = ''.join(res)

    elif op_i == 3:
        k = int(op[1])-1
        
        print(res[k])
        #prev.append(['3'])
    elif op_i == 4:
        prev_state = prev.pop()
        res = prev_state
        #prev_op = prev_op.split()
        #operation(prev_op,res,True)
    return res
        
Q =  int(input())
S = ""
for _ in range(Q):
    oper = input().split()
    S = operation(oper,S)        
        