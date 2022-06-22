class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for elem in nums:
            if freq.__contains__(elem):
                freq[elem] += 1
            else:
                freq[elem] = 1

        list = sorted(freq.items(), key = lambda kv:(kv[1], kv[0]))

        print(list)
        ans = []
        for i in list[-k:]:
            ans.append(i[0])
        return ans