class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic = {}
        for i in range(len(names)):
            dic[heights[i]] = names[i]
        heights.sort()
        
        ans = []
        for i in range(len(heights)-1,-1,-1):
            ans.append(dic[heights[i]])
            
        return ans