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
def main():
    t = int(input())
    for _ in range(t):
        q = int(input())
        ans = []
        trie = Trie()

        for _ in range(q):
            x, s = input().split()
            x = int(x)

            if x == 1:
                trie.insert(s)
            elif x == 2:
                ans.append(trie.search(s))
            elif x == 3:
                ans.append(trie.isPrefix(s))

        # Print results as lowercase true/false
        print(" ".join(["true" if res else "false" for res in ans]))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
