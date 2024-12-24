
#User function Template for python3

class Solution:
    
    #Function to search a given number in row-column sorted matrix.
    def searchMatrix(self, mat, x): 
    	# code here 
        if not mat or not mat[0]:
            return False
        
        rows = len(mat)
        cols = len(mat[0])
        


        left, right = 0, rows * cols - 1
        while left <= right:
            mid = (left + right) // 2
            mid_value = mat[mid // cols][mid % cols]
            
            if mid_value == x:
                return True
            elif mid_value < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return False   	



#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    for _ in range(t):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        matrix = []
        for i in range(r):
            row = list(map(int, data[index:index + c]))
            matrix.append(row)
            index += c
        x = int(data[index])
        index += 1
        ob = Solution()
        if ob.searchMatrix(matrix, x):
            print("true")
        else:
            print("false")
        print("~")
# } Driver Code Ends
