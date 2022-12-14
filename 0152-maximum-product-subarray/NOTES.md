```
class Solution:
def maxProduct(self, nums: List[int]) -> int:
maxi = nums[0]
for start in range(len(nums)):
local = nums[start]
maxi = max(local, maxi)
for end in range(start + 1, len(nums)):
local *= nums[end]
maxi = max(local, maxi)
return maxi
```