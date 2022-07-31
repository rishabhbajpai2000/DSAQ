class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        m = 0
        for i in sentences:
            spaces = 0
            for j in i:
                if j == " ": spaces += 1
            m = max(m, spaces+1)
        return m
            
        