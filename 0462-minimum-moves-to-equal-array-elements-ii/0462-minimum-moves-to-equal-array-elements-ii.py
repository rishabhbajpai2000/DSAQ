class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        to_reach = nums[0]
        if len(nums)%2 == 0:
            to_reach = (nums[len(nums)//2] + nums[(len(nums)//2) - 1])//2
        else:
            to_reach = nums[len(nums)>>1]
            
        print(to_reach)
        count = 0
        for i in nums:
            count += abs(to_reach-i)
            
        return count
            
        
        