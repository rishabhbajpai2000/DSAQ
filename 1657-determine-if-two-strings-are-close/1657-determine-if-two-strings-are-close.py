class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): return False
        
        count1 = Counter(word1)
        count2 = Counter(word2)
        
        l1 = list(count1.values())
        l2 = list(count2.values())
        
        l1.sort()
        l2.sort()
        s1= set(count1.keys())
        s2 = set(count2.keys())
        
        for i in s1:
            if i not in s2:return False
            
        for i in range(len(l1)):
            try: 
                if l1[i] != l2[i]: return False
            except:
                return False
        
        return True