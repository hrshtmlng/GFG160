#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr):
		# code here
        n = len(arr)
        currMaxx = arr[0]
        currMin = arr[0]
        maxProd = arr[0]
        
        for i in range(1,n):
            temp = max(arr[i],arr[i]*currMaxx,arr[i]*currMin)
            currMin = min(arr[i],arr[i]*currMaxx,arr[i]*currMin)
            currMaxx = temp
            
            maxProd = max(maxProd,currMaxx)
        return maxProd    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends
