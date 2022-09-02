class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        print(nums)
        # nums = list(set(nums))
        print(nums)
        
        return nums[-k]