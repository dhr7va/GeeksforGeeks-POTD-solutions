"""
class TrieNode: 
      
    def __init__(self): 
        self.children = [None]*26
        self.isEndOfWord = False
"""

class Solution:
    def insert(self, root, key):
        node = root
        for char in key:
            index = ord(char) - ord('a')
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]

        node.isEndOfWord = True

    def search(self, root, key):
        node = root

        for char in key:
            index = ord(char) - ord('a')
            if not node.children[index]:
                return False
            node = node.children[index]

        return node and node.isEndOfWord



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
class TrieNode: 
      
    def __init__(self): 
        self.children = [None]*26
  
        # isEndOfWord is True if node represent the end of the word 
        self.isEndOfWord = False
  
class Trie: 
      
    # Trie data structure class 
    def __init__(self): 
        self.root =TrieNode()
        

if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=input().strip().split()
        strs=input()
        
        t=Trie()
        ob = Solution()
        
        for s in arr:
            ob.insert(t.root,s)
        
        if ob.search(t.root,strs):
            print(1)
        else:
            print(0)
# } Driver Code Ends
