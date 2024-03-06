#User function Template for python3

class Solution:
    def search(self, pattern, text):
        prime = 101  
        pattern_length = len(pattern)
        text_length = len(text)

        def calculate_hash(string, length):
            hash_value = 0
            for i in range(length):
                hash_value = (hash_value * 26 + ord(string[i]) - ord('a')) % prime
            return hash_value

        pattern_hash = calculate_hash(pattern, pattern_length)
        text_hash = calculate_hash(text, pattern_length)

        result = []
        for i in range(text_length - pattern_length + 1):
            if pattern_hash == text_hash and pattern == text[i:i+pattern_length]:
                result.append(i+1)  
            if i < text_length - pattern_length:
                text_hash = (text_hash - (ord(text[i]) - ord('a')) * pow(26, pattern_length - 1, prime)) * 26 \
                            + (ord(text[i + pattern_length]) - ord('a'))
                text_hash %= prime

        return result
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        for value in ans:
            print(value,end = ' ')
        print()
# } Driver Code Ends
