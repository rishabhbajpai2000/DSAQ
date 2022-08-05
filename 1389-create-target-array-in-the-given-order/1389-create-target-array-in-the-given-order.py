class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = []
        counter = 0
        for i in index:
            ans.insert(i, nums[counter])
            counter += 1
        return ans