class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        count = 0
        total_distinct = len(set(nums))
        for start in range(len(nums)):
            distinct = set()
            for end in range(start, len(nums)):
                distinct.add(nums[end])
                if len(distinct) == total_distinct: count += 1
            
        return count