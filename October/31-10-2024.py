#User function Template for python3
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
'''
class Solution:
    def sortedInsert(self, head, x):
        new_node = Node(x)

        if head is None or x < head.data:
            new_node.next = head
            if head:
                head.prev = new_node
            return new_node

        current = head
        while current.next and current.next.data < x:
            current = current.next

        new_node.next = current.next
        if current.next:
            current.next.prev = new_node
        current.next = new_node
        new_node.prev = current

        return head



#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def print_list(head):
    current = head
    while current:
        print(current.data, end=' ')
        current = current.next
    print()


if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        values = list(map(int, input().strip().split()))
        head = None
        tail = None

        for value in values:
            if head is None:
                head = Node(value)
                tail = head
            else:
                tail.next = Node(value)
                tail.next.prev = tail
                tail = tail.next

        value_to_insert = int(input().strip())
        solution = Solution()
        head = solution.sortedInsert(head, value_to_insert)
        print_list(head)

        print("~")

# } Driver Code Ends
