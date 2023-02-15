class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        int_string = ""
        for i in num:
            int_string += str(i)
        n = int(int_string)
        n += k
        n = str(n)
        result = []
        for i in n:
            result.append(int(i))
        return result