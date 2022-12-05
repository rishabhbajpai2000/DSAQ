class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        equal_skill = skill[0] + skill[-1]
        chemistry = 0
        for i in range(len(skill)//2):
            first = skill[i]
            second = skill[len(skill)-1-i]
            s = first + second
            if s != equal_skill: return -1
            
            chemistry += first*second
        return chemistry
    
    

        