
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for i in s:
            if freq.__contains__(i):
                freq[i] += 1
            else: 
                freq[i] = 1
        print(freq)
        sorted_dict = dict(sorted(freq.items(), key=lambda item: item[1]))

        ans = ""
        print(sorted_dict)
        for i in sorted_dict:
            ans += i*freq[i]
        ans = ans[::-1]
        return ans
        