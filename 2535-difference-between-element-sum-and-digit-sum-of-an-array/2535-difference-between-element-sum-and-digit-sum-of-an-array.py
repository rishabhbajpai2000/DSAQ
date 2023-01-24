class Solution:
    def di(self, i:int):
        i = str(i)
        s = 0
        for dig in i:
            s += int(dig)
        return s
    def differenceOfSum(self, nums: List[int]) -> int:
        numsum = sum(nums)
        disum = 0
        for i in nums:
            if i>9:disum += self.di(i)
            else: disum += i
        return abs(disum - numsum)