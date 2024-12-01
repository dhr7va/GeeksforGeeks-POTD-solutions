#User function Template for python3

"""
# Node Class

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""

class Solution:
    def arrangeCV(self, head):
        vowels = set('aeiou')
        
        vowel_head = vowel_tail = None
        consonant_head = consonant_tail = None
        
        current = head
        while current:
            next_node = current.next
            current.next = None
            
            if current.data in vowels:
                if not vowel_head:
                    vowel_head = vowel_tail = current
                else:
                    vowel_tail.next = current
                    vowel_tail = current
            else:
                if not consonant_head:
                    consonant_head = consonant_tail = current
                else:
                    consonant_tail.next = current
                    consonant_tail = current
            
            current = next_node
        
        if vowel_tail:
            vowel_tail.next = consonant_head
        

        return vowel_head if vowel_head else consonant_head


#{ 
 # Driver Code Starts
# Node Class
class Node:

    def __init__(self, val):
        self.data = val
        self.next = None


# Linked List Class
class Linked_List:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next


def printList(head):
    tmp = head
    while tmp:
        print(tmp.data, end=' ')
        tmp = tmp.next
    print()


if __name__ == '__main__':
    for i in range(int(input())):
        n = int(input())
        arr = [str(x) for x in input().split()]

        lis = Linked_List()
        for i in arr:
            lis.insert(i)

        newHead = Solution().arrangeCV(lis.head)
        printList(newHead)

# } Driver Code Ends