class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for i in s:
            if freq.__contains__(i):
                freq[i] += 1
            else:
                freq[i] = 1
        probable = []
        for i in freq:
            if freq[i] == 1:
                probable.append(i)

        minm = len(s)
        for i in probable:
            for j in range(len(s)):
                if i == s[j]:
                    minm = min(j,minm)
                    break
        if minm == len(s):
            return -1 
        return minm