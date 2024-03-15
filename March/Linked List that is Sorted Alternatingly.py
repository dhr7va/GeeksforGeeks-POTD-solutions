class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def sort(self, head):
        if not head or not head.next:
            return head

        asc = head
        des = head.next
        rev_start = des

        while des and des.next:
            asc.next = des.next
            asc = asc.next

            des.next = asc.next
            des = des.next

        rev_start = self.reverse(rev_start)

        asc.next = rev_start

        current = head
        while current:
            ptr = current.next
            while ptr:
                if current.data > ptr.data:
                    current.data, ptr.data = ptr.data, current.data
                ptr = ptr.next
            current = current.next

        return head




#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Llist:
    def __init__(self):
        self.head=None
    
    def insert(self,data,tail):
        node=Node(data)
        
        if not self.head:
            self.head=node
            return node
        
        tail.next=node
        return node
        

def printList(head):
    while head:
        print(head.data,end=' ')
        head=head.next
        
if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        
        n1=int(input())
        arr1=[int(x) for x in input().split()]
        ll1=Llist()
        tail=None
        for nodeData in arr1:
            tail=ll1.insert(nodeData,tail)
            
        
        ob = Solution()
        resHead=ob.sort(ll1.head)
        printList(resHead)
        print()
        
    
    
# } Driver Code Ends
