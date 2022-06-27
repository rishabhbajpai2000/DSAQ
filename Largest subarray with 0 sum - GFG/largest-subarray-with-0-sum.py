#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        prev_sum = {}
        l = 0
        s = 0
        for i in range(n):
            s += arr[i]
            if (s == 0):
                l = i+1
            else:
                if prev_sum.__contains__(s):
                    l = max(l, i - prev_sum[s])
                else:
                    prev_sum[s] = i
        return l
#{ 
#  Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends