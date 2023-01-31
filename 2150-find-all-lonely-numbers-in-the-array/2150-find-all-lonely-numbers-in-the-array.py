class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        nums = set(nums)
        ans = []
        for i in nums:
            if i - 1 not in nums and i + 1 not in nums and freq[i] == 1: ans.append(i)
        return ans