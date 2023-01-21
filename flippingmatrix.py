import math
q = int(input().strip())

for a0 in range(q):
    n = int(input().strip())
    a =[[0 for j in range(2*n)] for i in range(2*n)]
    
    for x in range(2 * n):
        c = [int(c_temp) for c_temp in input().strip().split(' ')]        
        a[x] = c
     
    
    v = 0
    for i in range(n):
        for j in range(n):
            l = []
            l.append(a[i][j]) # current matrix
            l.append(a[2 * n - 1 - i][j])  # bottom left
            l.append(a[i][2 * n - 1- j]) # top right
            l.append(a[2* n - 1 - i][2 * n - 1- j]) # bottom right
    
            maxv = max(l)
            #print(l)
            #print(max(l))
            
            v += maxv

    print(v)