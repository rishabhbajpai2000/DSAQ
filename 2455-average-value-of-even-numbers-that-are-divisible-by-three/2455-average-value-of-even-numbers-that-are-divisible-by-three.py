class Solution:
    def averageValue(self, nums: List[int]) -> int:
        count = 0
        s = 0
        for i in nums:
            if i%6 == 0:
                count += 1
                s += i
        if count!= 0:
            return s//count
        return 0