import testcase_scalarproducts2
def fib_gen(mod):
    f0,f1=0,1
    while True:
        yield f0
        f0,f1=f1,f0+f1 % mod
        
# if ...== main bla bla

c,m,n = map(int,input().split())

fib_it = fib_gen(m)
for _ in range(7): next(fib_it) # discard f0,f1,..f6

ret = len(set(c*c* fi % m for fi,_1,_2 in zip(fib_it,fib_it, range(3,2*n))))
print(ret)

#faster 
# Enter your code here. Read input from STDIN. Print output to STDOUT
# c, m, n = map(int,input().split())
# if n == 1:
#     print("0")
# else:
#     arr = [0 for i in range(2 * n + 2)]
#     arr[0] = 0
#     arr[1] = c
#     l = []
#     for i in range(2, 2 * n + 2):
#         arr[i] = (arr[i - 1] + arr[i - 2]) % m
#     for i in range(2, 2 * n - 2, 2):
#         temp = (arr[i] * arr[i + 2] + arr[i + 1] * arr[i + 3]) % m
#         l.append(temp)
#         temp=(arr[i] * arr[i + 4] + arr[i + 1] * arr[i + 5]) % m
#         l.append(temp)
#     temp = (arr[2 * n - 2] * arr[2 * n] + arr[2 * n - 1] * arr[2 * n + 1]) % m
#     l.append(temp)
#     l = set(l)
#     print(len(l))

#too slow
# C,M,n = list(map(int,input().split()))
# s = [0]*(2*n+2)
# V = [[0,0] for i in range(n)]
# s[1] = C
# for i in range(2,2*n+2):
#     s[i] = (s[i-1]+s[i-2])%M
#     j = i//2-1
#     V[j][i%2] = s[i]
# V = [tuple(i) for i in V]
# if len(V) > 2:
#     V = list(set(V))
# V.sort()
# n = len(V)
# equiv_set = {}
# nodes = []
# for i in range(n):
#     a,b = V[i]
#     j = 0
#     k = len(nodes)
#     while j < k:
#         c,d = nodes[j]
#         equiv_set[(a*c+b*d)%M] = 1
#         j+=1
#     nodes.append(V[i])
# count = len(equiv_set)
# print(count%M)
