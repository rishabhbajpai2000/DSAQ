class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            num = 0
            binary = bin(i)[2:]
            for j in binary:
                if j == "1": num += 1
            ans.append(num)
        return ans
        