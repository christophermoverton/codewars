def checkLex(arr, n):
    for j in range(n-1):
        for k in range(n):
            if arr[j][k] > arr[j+1][k]:
                return False
    return True

t = int(input().strip())

for i in range(t):
    n = int(input().strip())
    line = []
    for j in range(n):
        x = list(input().strip())
        x.sort()
        line.append(x)
    
    if checkLex(line, n):
        print("YES")
    else:
        print("NO")