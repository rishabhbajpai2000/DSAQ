```
class Solution:
def longestPalindrome(self, s: str) -> str:
if len(s) == 1: return s
curmax = ""
for start in range(len(s)):
for end in range(start, len(s)):
string = s[start:end+1]
if string == string[::-1] and len(string)>len(curmax):
curmax = string
return curmax
```
​
this code is giving tle