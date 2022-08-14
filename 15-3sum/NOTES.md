```
check ={}
ind = 0
for i in nums:
check[i] = ind
ind += 1
ans = []
for i in range(len(nums)):
for j in range(i + 1, len(nums)):
k = -1*(nums[i] + nums[j])
if (k in check and check[k] not in [i, j]):
ans.append([nums[i], nums[j] ,k])
return ans
```
​
```
check ={}
ind = 0
nums = list(set(nums))
for i in nums:
check[i] = ind
ind += 1
ans = []
for i in range(len(nums)):
for j in range(i + 1, len(nums)):
k = -1*(nums[i] + nums[j])
if (k in check and check[k] not in [i, j]):
ans.append([nums[i], nums[j] ,k])
return ans
```