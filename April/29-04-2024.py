#Your task is to complete this function
#Your function should return the new head pointer
class node:
    def __init__(self, x):
        self.data = x
        self.next = None

class Solution:
    def deleteK(self, head, k):
        if k <= 1:
            return None
        
        current = head
        prev = None
        
        count = 1
        
        while current:
            if count % k == 0:
                if prev:
                    prev.next = current.next  
                else:
                    head = current.next
                    
            else:
                prev = current
            
            current = current.next
            
            count += 1
        
        return head

#{ 
 # Driver Code Starts
class node:

    def __init__(self, x):
        self.data = x
        self.next = None


def createLinkedList(arr):
    head = node(arr[0])
    curr = head
    for i in range(1, len(arr)):
        new_node = node(arr[i])
        curr.next = new_node
        curr = curr.next

    return head


def printlist(ptr):
    while ptr != None:
        print(ptr.data, end=" ")
        ptr = ptr.next
    print()


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())

        obj = Solution()
        head = createLinkedList(arr)
        new_head = obj.deleteK(head, k)
        printlist(new_head)

# } Driver Code Ends