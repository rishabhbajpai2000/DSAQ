def func(i, set1, set2, set3):
    
    def_set = set1
    if i[0].lower() in set2: def_set = set2
    elif i[0].lower() in set3: def_set = set3
    
    for elem in i:
        elem = elem.lower()
        if elem not in def_set: return False
        
    return True
    
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        set1 = set(list("qwertyuiop"))
        set2 = set(list("asdfghjkl"))
        set3 = set(list("zxcvbnm"))

        ans = []
        for i in words:
            if func(i, set1, set2, set3):
                ans.append(i)
        return ans
        
        