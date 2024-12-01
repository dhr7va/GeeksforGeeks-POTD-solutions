class Solution:
    def delete_node(self, head, x):
        #code here
        if head is None:
            return None
        
        if x == 1:
            next_node = head.next
            if next_node:
                next_node.prev = None
            return next_node
        
        current = head
        for _ in range(x - 1):
            if current is None:
                return head
            current = current.next
        
        if current is None:
            return head
        
        if current.next is None:
            current.prev.next = None
        else:
            current.prev.next = current.next
            current.next.prev = current.prev
        
        return head

#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    @staticmethod
    def print_list(node):
        while node is not None:
            print(node.data, end=" ")
            node = node.next
        print()


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    t = int(data[index])
    index += 1
    for _ in range(t):
        n = int(data[index])
        index += 1
        head = None
        tail = head

        for i in range(n):
            temp = int(data[index])
            index += 1
            if head is None:
                head = Node(temp)
                tail = head
            else:
                new_node = Node(temp)
                tail.next = new_node
                new_node.prev = tail
                tail = new_node

        x = int(data[index])
        index += 1

        obj = Solution()
        res = obj.delete_node(head, x)

        Node.print_list(res)

# } Driver Code Ends
