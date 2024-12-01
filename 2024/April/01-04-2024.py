
from typing import Optional
from collections import deque

class Solution:
    def pairsViolatingBST(self, n, root):
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.data] + inorder(node.right)

        def merge(arr, low, mid, high):
            temp = []
            i, j, count = low, mid + 1, 0
            while i <= mid and j <= high:
                if arr[i] <= arr[j]:
                    temp.append(arr[i])
                    i += 1
                else:
                    count += (mid - i + 1)
                    temp.append(arr[j])
                    j += 1
            while i <= mid:
                temp.append(arr[i])
                i += 1
            while j <= high:
                temp.append(arr[j])
                j += 1
            arr[low:high+1] = temp

            return count

        def merge_sort(arr, low, high):
            if low < high:
                mid = (low + high) // 2
                left_count = merge_sort(arr, low, mid)
                right_count = merge_sort(arr, mid + 1, high)
                inv_count = merge(arr, low, mid, high)
                return left_count + right_count + inv_count
            return 0

        sorted_arr = inorder(root)
        return merge_sort(sorted_arr, 0, len(sorted_arr) - 1)
#{ 
 # Driver Code Starts

class Node:
    def __init__(self,val):
        self.data=val
        self.right=None
        self.left=None

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

def inputTree():
    treeString=input().strip()
    root = buildTree(treeString)
    return root
def inorder(root):
    if (root == None):
       return
    inorder(root.left);
    print(root.data,end=" ")
    inorder(root.right)

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        root = inputTree();
        
        obj = Solution()
        res = obj.pairsViolatingBST(n, root)
        
        print(res)
        

# } Driver Code Ends