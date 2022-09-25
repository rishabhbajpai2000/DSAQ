class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        dic = {}
        ans = len(cards) + 1
        for i in range(len(cards)):
            if dic.__contains__(cards[i]):
                l = i - dic[cards[i]] + 1
                ans = min(l,ans)
                dic[cards[i]] = i
            else:
                dic[cards[i]] = i
        
        if ans == len(cards) + 1: return -1
        return ans