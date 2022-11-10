#User function Template for python3

class Solution:
	def canPair(self, nums, k):
		# Code here
        for i in range(len(nums)):
            nums[i] = nums[i]%k
        # print(nums)
        dic = {}
        for i in range(k):
            dic[i] = 0
        # print(dic)
        for i in nums:
            dic[i] += 1
        # print(dic)
    
        for i in dic:
            if i == 0 and dic[i]%2 == 1:
                return False
            elif i != 0 and dic[i] != dic[k-i]:
                return False
                
        return True

            		    
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, k = input().split()
		n = int(n)
		k = int(k)
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.canPair(nums, k)
		if(ans):
			print("True")
		else:
			print("False")
# } Driver Code Ends