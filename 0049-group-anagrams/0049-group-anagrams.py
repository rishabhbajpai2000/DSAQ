class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def anagram_signature(string):
            sig = []
            for i in range(26):sig.append(0)
            
            for i in string:
                sig[ord(i) - ord('a')] += 1
            
            s = ""
            for i in sig: s+= str(i) + "*"
            
            return s
        dic = {} # signature: [one, two, three]
        
        
        for i in strs:
            sign = anagram_signature(i)
            if dic.__contains__(sign):
                dic[sign].append(i)
            else:
                dic[sign] = [i]
        
        ans = []
        for i in dic:
            ans.append(dic[i])
        
        return ans
        
            