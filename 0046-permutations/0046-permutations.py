class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        local = []

        def helper(index):
            if index == len(nums):
                result.append(local.copy())
                return 

            for i in range(len(local) + 1):
                local.insert(i, nums[index])
                helper(index + 1)
                del local[i]
        helper(0)
        return result