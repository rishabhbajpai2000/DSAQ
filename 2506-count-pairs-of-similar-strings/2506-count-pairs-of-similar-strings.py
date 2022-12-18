def word2num(word):
    num = [0]*26
    
    for i in word:
        num[ord(i) - ord("a")] = 1
        
    ans = ""
    for i in num:
        ans += str(i)
    return ans

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        
        nums = []
        for i in words:
            nums.append(word2num(i))
        print(nums)
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i]==nums[j]:count += 1
        return count
        