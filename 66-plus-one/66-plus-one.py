class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if (digits[-1] != 9):
            digits[-1] +=1
            return digits
        else:
            s = ""
            for i in digits:
                s += str(i)
            s = int(s)
            s+= 1
            print(s)
            s = str(s)
            ans = []
            for i in s:
                ans.append(int(i))
            return ans