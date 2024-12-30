#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends
#User function Template for python3

class Solution:
    #Complete the below function
    def countPairs(self,arr, target):
        #Your code here
        
        freq = {}
        count = 0
        
        for num in arr:
            complement = target - num  # Find the complement that adds up to target
            # If complement exists in the dictionary, add its frequency to count
            if complement in freq:
                count += freq[complement]
            # Update the frequency of the current number in the dictionary
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
                
        return count


#{ 
 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        k = int(input())
        ob = Solution()
        print(ob.countPairs(A, k))
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
