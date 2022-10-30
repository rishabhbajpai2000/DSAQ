class Solution:
    def averageValue(self, nums: List[int]) -> int:
        count = 0
        s = 0
        for i in nums:
            if i%3 == 0 and i%2 == 0:
                count += 1
                s += i
        if count!= 0:
            return s//count
        return 0