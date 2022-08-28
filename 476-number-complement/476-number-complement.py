class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]
        ans = ""
        for i in binary:
            if i == "0":
                ans += "1"
            else:
                ans+= "0"
        return int(ans, 2)