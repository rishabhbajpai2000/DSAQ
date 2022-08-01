class Solution:
    def balancedStringSplit(self, s: str) -> int:
        score, count = 0,0
        for i in s:
            score += 1 if i == "R" else -1
            count += 1 if score == 0 else 0
        return count
#         l = len(s)
#         count = 0
#         for i in range(l):
#             left, right = 0,0
#             for j in range(i, l):
#                 if (s[j] == "L"):
#                     left += 1
#                 else:
#                     right += 1
#             if right == left:
#                 count += 1
                
#         return count

                
        