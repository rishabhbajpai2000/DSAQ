class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # making empty arrays first 
        ans = []
        for row in range(1, numRows+1):
            ans.append([0]*row)
            ans[row-1][0] = 1
            ans[row-1][-1] = 1
        
        # for row in ans:
        #     print(row)
        
        for row in range(2, len(ans)):
            for col in range(1, len(ans[row])-1):
                ans[row][col] = ans[row-1][col-1] + ans[row-1][col]
        
        # for row in ans:
        #     print(row)
        return ans