class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels= {"a","e","i","o","u","A","E","I","O","U"}
        count_first, count_second = 0,0
        for i in range(len(s)):
            if s[i] in vowels:
                if i < len(s)//2: count_first += 1
                else: count_second+=1
                
        return count_first == count_second
            