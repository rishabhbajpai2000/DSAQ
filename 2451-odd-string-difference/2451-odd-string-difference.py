class Solution:
    def oddString(self, words: List[str]) -> str:
        
        dic = {}

        def diff_arr(word):
            diff = []
            for i in range(len(word)-1):
                diff.append(ord(word[i+1]) - ord(word[i]))
            return diff

        for word in words:
            diff = diff_arr(word)

            if dic.__contains__(str(diff)):
                dic[str(diff)].append(word)
            else:
                a = [word]
                dic[str(diff)] = a
        # print(dic)
        # for i in dic:
        #     print(i + str(dic[i]))


        for i in dic:
            if len(dic[i]) == 1:
                return dic[i][0]
