#User function Template for python3
class Solution:

	def print2largest(self,arr, n):
		# code here
		lar = arr[0]
		seclar = -1
		change = 0
		
		for i in arr:
		    if i > lar:
		        seclar = lar
		        lar = i
		      #  change = 1
		    if i < lar:
		        if i > seclar:
		            seclar = i
		          #  change = 1
		        else:
		            pass
	    return seclar if seclar != -1 else -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends