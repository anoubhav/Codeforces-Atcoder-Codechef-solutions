from sys import stdin
from collections import defaultdict as dd

class Node: 
  
    # Constructor to create a new node 
    def __init__(self, key): 
        self.key = key  
        self.left = None
        self.right = None
  
# A utility function to insert a new node with given key in BST 
def insert(node, key): 
  
    # If the tree is empty, return a new node 
    if node is None: 
        return Node(key) 
  
    # Otherwise recur down the tree 
    if key < node.key: 
        node.left = insert(node.left, key) 
    else: 
        node.right = insert(node.right, key) 
  
    # return the (unchanged) node pointer 
    return node 
  
# A utility function to find the node containing the minimum key in BST.
def minValueNode( node): 
    current = node 
  
    # loop down to find the leftmost leaf 
    while(current.left is not None): 
        current = current.left  
  
    return current  
  
# A utility function to delete a node with given key in BST
def deleteNode(root, key): 
  
    # Base Case 
    if root is None: 
        return root  
  
    # If the key to be deleted is smaller than the root's 
    # key then it lies in  left subtree 
    if key < root.key: 
        root.left = deleteNode(root.left, key) 
  
    # If the kye to be delete is greater than the root's key 
    # then it lies in right subtree 
    elif(key > root.key): 
        root.right = deleteNode(root.right, key) 
  
    # If key is same as root's key, then this is the node 
    # to be deleted 
    else: 
          
        # Node with only one child or no child 
        if root.left is None : 
            temp = root.right  
            root = None 
            return temp  
              
        elif root.right is None : 
            temp = root.left  
            root = None
            return temp 
  
        # Node with two children: Get the inorder successor 
        # (smallest in the right subtree) 
        temp = minValueNode(root.right) 
  
        # Copy the inorder successor's content to this node 
        root.key = temp.key 
  
        # Delete the inorder successor 
        root.right = deleteNode(root.right , temp.key) 
  
  
    return root

############################### ABOVE ONLY BST IMPLEMENTATION ########################
# The BST stores the maximum rating of each KG. We update the BST, if the maximum rating changes for any KG. 

n, q = map(int, stdin.readline().split())

# set of infants belonging to each KG
kinder = dd(set) 

# the maximum rate of a KG
kindermaxrate = dd(int)

# The KG infant i belongs to is infant[i]
infant = [0]*(n+1)

# The rating of infant i is rating[i]
rating = [0]*(n+1)

# root of BST, I had to follow the API of copy pasted code.
root = None

# Get the initial arrangement of infants and KGs
for i in range(n):
    a, b = map(int, stdin.readline().split())

    # to KG b and infant a.
    kinder[b].add(i+1)

    # location of infant
    infant[i+1] = b 

    # rating of infant
    rating[i+1] = a 

    # get the maximum rating in KG
    t = kindermaxrate[b]

    # if max rating is 0, i.e., empty KG. Else If > 0, it has elements.
    if t > 0:
        # if new infant rating is higher than current max
        if a > t:
            # update max for that KG
            kindermaxrate[b] = a
            # insert new max
            root = insert(root, a)
            # delete previous max
            root = deleteNode(root, t)
        # if lower than current max, do nothing
        else:
            pass
    else:
        # add new max rating for the KG and add this max rating to BST
        kindermaxrate[b] = a
        root = insert(root, kindermaxrate[b])

for _ in range(q):
    c, d = map(int, stdin.readline().split())

    # remove from current KG
    curr = infant[c]
    kinder[curr].remove(c)

    # if transferred infant is the maximum rated infant of current KG: update max rating of KG. Update BST with removal of max rating and addition of new max.
    if kindermaxrate[curr] == rating[c]:
        if len(kinder[curr]) > 0:
            mx = max((rating[i] for i in kinder[curr]))
            kindermaxrate[curr] = mx
            root = deleteNode(root, rating[c]) 
            root = insert(root, mx) 
        else:
            root = deleteNode(root, rating[c])
            kindermaxrate[curr] = -1
    else:
        # do nothing
        pass
        
    # add infant C to new KG D
    infant[c] = d
    kinder[d].add(c)

    # update max rating and update bst because of this addition to D if rating of C more than max rating of D
    t = kindermaxrate[d]
    if rating[c]>t:
        if t!=0:
            root = deleteNode(root, t) 
        root = insert(root, rating[c])
        kindermaxrate[d] = rating[c]
    else:
        # do nothing
        pass

    print(minValueNode(root).key)




