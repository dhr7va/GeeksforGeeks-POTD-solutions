#User function Template for python3
class Solution:

	def constructLowerArray(self,arr):
		# code here
        def merge_sort(arr, indices, result):
            if len(arr) < 2:
                return arr, indices
            
            mid = len(arr) // 2
            left, left_indices = merge_sort(arr[:mid], indices[:mid], result)
            right, right_indices = merge_sort(arr[mid:], indices[mid:], result)
            
            return merge(left, right, left_indices, right_indices, result)

        def merge(left, right, left_indices, right_indices, result):
            i = j = 0
            len_left = len(left)
            len_right = len(right)
            sorted_arr = []
            sorted_indices = []
            
            while i < len_left and j < len_right:
                if left[i] <= right[j]:
                    result[left_indices[i]] += j
                    sorted_arr.append(left[i])
                    sorted_indices.append(left_indices[i])
                    i += 1
                else:
                    sorted_arr.append(right[j])
                    sorted_indices.append(right_indices[j])
                    j += 1
            
            while i < len_left:
                result[left_indices[i]] += j
                sorted_arr.append(left[i])
                sorted_indices.append(left_indices[i])
                i += 1

            while j < len_right:
                sorted_arr.append(right[j])
                sorted_indices.append(right_indices[j])
                j += 1
                
            return sorted_arr, sorted_indices

        n = len(arr)
        indices = list(range(n))
        result = [0] * n
        
        merge_sort(arr, indices, result)
        
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.constructLowerArray(arr)
        for x in ans:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends
