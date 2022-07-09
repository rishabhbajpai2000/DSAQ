def l_s(start_ind, string):
    l = len(string)
    s = set()
    max_l = 0
    for i in range(start_ind, l):
        if string[i] in s:
            return max_l
        s.add(string[i])
        max_l += 1
        
    return max_l
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = 0
        l = len(s)
        for i in range(l):
            m = max(m, l_s(i, s))
        return m