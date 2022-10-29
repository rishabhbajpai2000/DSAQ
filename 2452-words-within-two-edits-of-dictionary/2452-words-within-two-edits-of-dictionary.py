def edit(word1, word2):
    mistakes = 0
    
    for i in range(len(word1)):
        if word1[i] != word2[i]: mistakes+= 1
            
    if mistakes<3:
        return True
    return False

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        answers = []
        
        for i in queries:
            for j in dictionary:
                if edit(i, j): 
                    answers.append(i)
                    break

        return answers