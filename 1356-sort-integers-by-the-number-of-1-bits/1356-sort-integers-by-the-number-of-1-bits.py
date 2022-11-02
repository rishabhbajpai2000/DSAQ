class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        second_l = []
        dic = {}
        for i in arr:
            bits = bin(i).count("1")
            if dic.__contains__(bits):
                dic[bits].append(i)
            else:
                dic[bits] = [i]
        for i in dic:
            second_l.append(i)
            dic[i].sort()

        second_l.sort()
        ans = []
        for i in second_l:
            for elem in dic[i]:
                ans.append(elem)
        return ans