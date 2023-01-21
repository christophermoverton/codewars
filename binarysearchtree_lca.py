import testcase_binarysearchtree_lca
class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def lca(root, v1, v2):
  #Enter your code here
    levset = {}
    nodeset = {}
    an_v1 = set()
    an_v2 = set()
    level = 0
    av1_av2 = [an_v1,an_v2]
    v1_v2 = [v1,v2]

    for i,v in enumerate(v1_v2):
        prev = None
        temp = root
        an_v = av1_av2[i]
        level = 0
        while (temp != None) :
            an_v.add(temp.info)
            levset[temp.info] = level
            nodeset[temp.info] = temp
            if temp.info == v:
                break
            if (temp.info > v) :
                prev = temp
                temp = temp.left
                level+=1

            elif(temp.info < v) :
                prev = temp
                temp = temp.right
                level+=1
    
    iset = an_v1.intersection(an_v2)
    #print(iset)
    lcaval = None
    lcalvlmax = 0
    for i in iset:
        if levset[i] >= lcalvlmax:
            lcaval = i
            lcalvlmax = levset[i]
    return nodeset[lcaval]

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print (ans.info)
