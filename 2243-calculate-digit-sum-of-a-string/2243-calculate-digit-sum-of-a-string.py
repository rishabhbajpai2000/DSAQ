class Solution:
    def digitSum(self, s: str, k: int) -> str:
        def sum_s(s):
            sum_1 = 0
            num = int(s)
            while (num!= 0):
                rem = num%10
                sum_1 += rem
                num //= 10
            return str(sum_1)

        while (len(s)>k):
            n = ""
            for i in range(0,len(s), k):
                # print("i = ", i)
                # print("min  =",  min(i+k, len(s)))
                a = s[i:min(i+k, len(s))]
                n += sum_s(a)
            s = n
        return s


