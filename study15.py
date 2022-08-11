for i in range(1,5): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(sum([j*10**(2*i-j) for j in range(1,i)]+[j*10**(j) for j in range(i,0,-1)])//10)

for i in range(1,5): 
    print(((10**i)//9)**2)