my solution
```
def check(x, y, arr):
xi = arr[0]
yi = arr[1]
r = arr[2]
return (xi-x)*(xi-x) + (yi-y)*(yi-y) <= r*r
​
def points(arr): # list of co ordinates, that are in circle
ans = set()
xi = arr[0]
yi = arr[1]
r = arr[2]
for x in range(xi-r, xi+r+1):
for y in range(yi-r, yi+r+1):
if check(x,y, arr):
ans.add((x,y))
return ans
class Solution:
def countLatticePoints(self, circles: List[List[int]]) -> int:
ans = set()
for arr in circles:
c = points(arr)
for elem in c:
ans.add(elem)
return len(ans)
```