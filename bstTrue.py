from cgitb import reset


def check_binary_tree(root):
    #inorder traversal 
    global inorder_arr
    def inorder_trav_bst(root):
        res = []
        if root:
            if root.left:
                res.extend(inorder_trav_bst(root.left))
            res.append(root.data)
            if root.right:
                res.extend(inorder_trav_bst(root.right))
        else:
            res=[root.data]
        return res
    arr = inorder_trav_bst(root)
    print(arr)
    arr2 = arr[0:]
    arr2.sort()
    for i,val in enumerate(arr):
        if val != arr2[i]:
            return 0
    if len(set(arr2)) != len(arr2):
        return 0
    return 1

class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

root = Node(3)
root.left = Node(2)
root.left.right = Node(4)
root.right = Node(5)
root.right.right = Node(6)
root.right.left = Node(7)
print(check_binary_tree(root))
root = Node(3)
root.left = Node(2)
root.left.left = Node(1)
root.right = Node(4)
root.right.right = Node(5)
print(check_binary_tree(root))
root = Node(7)
root.left = Node(4)
root.left.left = Node(3)
root.left.right = Node(5)
root.right = Node(10)
root.right.left = Node(8)
root.right.right = Node(12)
print(check_binary_tree(root))

