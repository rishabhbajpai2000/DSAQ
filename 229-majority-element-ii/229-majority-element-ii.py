
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1,c2,num1,num2 = 0,0, "P","P";
        for i in nums:
            if i == num1:
                c1 += 1 
            elif i == num2:
                c2 += 1 
            elif (c1 == 0):
                num1 = i
                c1 = 1
            elif (c2 == 0):
                num2 = i
                c2 = 1
            else: 
                c2-=1
                c1-=1
        l = len(nums)//3
        # we cant be sure if the num1 and num2 are majority or not 
        if nums.count(num1) <= l:
            num1 = "P"
        if nums.count(num2) <= l:
            num2 = "P"
            
        ans = set()
        if num1 != "P":
            ans.add(num1)
        if num2 != "P":
            ans.add(num2)
        return list(ans)
       