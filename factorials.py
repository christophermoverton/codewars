A = 10**9+7
factorials = [0]*2001

factorials[0] = 1
for i in range(1,2001):
    factorials[i] = i*factorials[i-1]
