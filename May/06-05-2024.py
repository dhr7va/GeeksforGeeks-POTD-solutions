#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
def noSibling(root):
    if not root:
        return [-1]  # If the tree is empty, return -1 as per the problem statement
    
    no_sibling = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node.left and not node.right:
            no_sibling.append(node.left.data)
        elif node.right and not node.left:
            no_sibling.append(node.right.data)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return sorted(no_sibling) if no_sibling else [-1]
    



#{ 
 # Driver Code Starts

from collections import deque
# Tree Node
class Node:
   def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree  
def buildTree(s):
   #Corner Case
   if(len(s)==0 or s[0]=="N"):          
       return None
       
   # Creating list of strings from input
   # string after spliting by space
   ip=list(map(str,s.split()))
   
   # Create the root of the tree
#   print(ip)
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
        ans = noSibling(root)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends
