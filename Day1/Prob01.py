class Solution:
    def getSecondLargest(self, arr):
        # Code Here+
        n = len(arr)
        largest = -1
        secondLargest = -1
        
        for i in range(n):
            if arr[i] > largest:
                secondLargest = largest
                largest = arr[i]
            elif arr[i] < largest and arr[i] >secondLargest:
                secondLargest = arr[i]
        return secondLargest
        
            

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends
