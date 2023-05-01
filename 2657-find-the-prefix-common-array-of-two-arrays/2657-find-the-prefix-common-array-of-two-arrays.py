class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        freq = {}
        freq2 = {}
        score = []
        for i in range(1, 51): 
            freq[i] = 0
            freq2[i] = 0
        
        for i in range(len(A)):
            freq[A[i]]+=1
            freq2[B[i]]+=1
            local_score = 0
            for elem in freq:
                if freq[elem] == freq2[elem]: 
                    local_score += freq[elem]
            score.append(local_score)
        return score 
            
            