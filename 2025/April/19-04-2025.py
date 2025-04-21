#User function Template for python3

class TrieNode:
    def __init__(self):
        self.child = [None, None]

class Solution:
    def insert(self, root, num):
        node = root
        for i in range(31, -1, -1):  # 32 bits
            bit = (num >> i) & 1
            if not node.child[bit]:
                node.child[bit] = TrieNode()
            node = node.child[bit]

    def findMaxXor(self, root, num):
        node = root
        maxXor = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            opposite = 1 - bit
            if node.child[opposite]:
                maxXor |= (1 << i)
                node = node.child[opposite]
            else:
                node = node.child[bit]
        return maxXor

    def maxXor(self, arr):
        root = TrieNode()
        maxResult = 0
        self.insert(root, arr[0])  

        for num in arr[1:]:
            maxResult = max(maxResult, self.findMaxXor(root, num))
            self.insert(root, num)
        return maxResult


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.maxXor(arr))
        print("~")

# } Driver Code Ends
