N-squared solution
```
class Solution:
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
def anagram_check(str1, str2):
first_freq = []
second_freq = []
for i in range(27):
first_freq.append(0)
second_freq.append(0)
for i in str1:
first_freq[ord(i) - ord("a")] += 1
for i in str2:
second_freq[ord(i)-ord("a")] += 1
for i in range(len(first_freq)):
if first_freq[i] != second_freq[i]:
return False
return True
counter = 0
ans = []
marking = []
for i in range(len(strs)):
marking.append(0)
for i in range(len(strs)):
if marking[i] == 0:
ans.append([strs[i]])
for j in range(i+1, len(strs)):
if anagram_check(strs[i],strs[j]):
ans[counter].append(strs[j])
marking[j] = 1
marking[i] = 1
counter+= 1
return ans
```