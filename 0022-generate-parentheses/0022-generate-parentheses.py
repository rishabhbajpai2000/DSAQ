class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
    
        def helper(curr, ob, cb):

            if ob == cb == n:
                ans.append("".join(curr))
                return
            if cb>ob:
                return

            if ob<n:
                curr.append("(")
                helper(curr, ob+1, cb)
                curr.pop()

            curr.append(")")
            helper(curr, ob, cb+1)
            curr.pop()

        helper([], 0, 0)
        return ans