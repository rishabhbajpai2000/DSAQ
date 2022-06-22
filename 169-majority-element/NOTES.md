```
class Solution:
def majorityElement(self, nums: List[int]) -> int:
# making a dictionary to store the frequency of integers
d = {}
for elem in nums:
if d.has_key(elem):
d[elem] += 1
else:
d[elem] = 1
l = len(nums)
# now we are checking:
# if element has frequency greater than half,
# then it will return the element
for elem in d:
if d[elem] > l//2:
return elem
```