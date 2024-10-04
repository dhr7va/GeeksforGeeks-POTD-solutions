#User function Template for python3
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def deleteNode(self, head, key):
        if not head:
            return None
        
        current = head
        prev = None
        
        if head.data == key:
            if head.next == head:
                return None
            
            temp = head
            while temp.next != head:
                temp = temp.next
            temp.next = head.next
            head = head.next
            return head
        
        prev = head
        current = head.next
        while current != head:
            if current.data == key:
                prev.next = current.next
                return head
            prev = current
            current = current.next
        
        return head
    
    def reverse(self, head):
        if not head or head.next == head:
            return head
        
        prev = None
        current = head
        next_node = None
        original_head = head
        
        while True:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            if current == original_head:
                break
        
        original_head.next = prev
        
        return prev

#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def printList(head):
    if head is None:
        print("empty")
        return

    temp = head
    while True:
        print(temp.data, end=" ")
        temp = temp.next
        if temp == head:
            break
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        key = int(input())

        head = Node(arr[0])
        tail = head
        for i in range(1, len(arr)):
            tail.next = Node(arr[i])
            tail = tail.next
        tail.next = head  # Make the list circular

        ob = Solution()
        head = ob.deleteNode(head, key)
        head = ob.reverse(head)
        printList(head)

# } Driver Code Ends
