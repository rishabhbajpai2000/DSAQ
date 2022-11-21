class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # calculating the prefix sum 
        pre = [arr[0]]
        for i in range(1, len(arr)):
            pre.append(pre[-1] + arr[i])
                
        count_even, count_odd = 0,0
        count = 0
        
        for i in range(len(pre)):
                
            if pre[i] % 2 == 0: # if the prefix sum is even 
                count += count_odd
                count_even += 1
            
            else: # if the prefix sum is odd
                count += count_even + 1
                count_odd += 1
                
        return count%(10**9 + 7)