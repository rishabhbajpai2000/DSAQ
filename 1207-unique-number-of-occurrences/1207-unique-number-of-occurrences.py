class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        for i in arr:
            if freq.__contains__(i): freq[i] += 1
            else: freq[i] = 1
        s = set()
        for i in freq:
            if freq[i] in s:
                return False
            else: s.add(freq[i])
        return True