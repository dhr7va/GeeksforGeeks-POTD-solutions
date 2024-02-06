#User function Template for python3

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def findDist(self, root, a, b):
        def findDistanceToNode(root, val):
            if not root:
                return -1
            if root.data == val:
                return 0
            left_distance = findDistanceToNode(root.left, val)
            if left_distance >= 0:
                return left_distance + 1
            right_distance = findDistanceToNode(root.right, val)
            if right_distance >= 0:
                return right_distance + 1
            return -1

        def findLCA(root, x, y):
            if not root:
                return None
            if root.data == x or root.data == y:
                return root
            left_LCA = findLCA(root.left, x, y)
            right_LCA = findLCA(root.right, x, y)
            if left_LCA and right_LCA:
                return root
            return left_LCA if left_LCA else right_LCA

        lca = findLCA(root, a, b)

        dist_from_lca_to_a = findDistanceToNode(lca, a)

        dist_from_lca_to_b = findDistanceToNode(lca, b)

        return dist_from_lca_to_a + dist_from_lca_to_b



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(50000)
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root


if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        a, b=map(int, input().split())
        ob = Solution()
        print(ob.findDist(root, a, b))

# } Driver Code Ends
