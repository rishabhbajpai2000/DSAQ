
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        stack.append(s[0])
        for i in s[1:]:
            if len(stack) >0  and i.lower() == stack[-1].lower() and i != stack[-1]:
                stack.pop()
            else:
                stack.append(i)
                
                
        string = "".join(stack)
        return string