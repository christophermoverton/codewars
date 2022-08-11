import math
def find_nb(m):
    # your code
    ## see Faulhaber polynomials
    ## cubic summation series 1^3 +...+n^3 = (n(n+1)/2)^2
    ## means 2*sqrt(m) = n*(n+1)
    ## solve for characteristic roots of n^2 + n - 2*sqrt(m)
    ## (-1 +/- sqrt(1 + 4*1*2*sqrt(m))/ 2
    n = (-1+math.sqrt(1 + 4*2*math.sqrt(m)))/2
    b = str(n).split('.')
    if len(b[1]) > 1:
        return -1
    return (-1+math.sqrt(1 + 4*2*math.sqrt(m)))/2

def testval(n):
    sum = 0
    for i in range(1,n+1):
        sum += i**3
    return sum

m = 2016377240304224197
n = find_nb(m)
nm = testval(int(n))
print(nm)
print(m)
print (n == nm)