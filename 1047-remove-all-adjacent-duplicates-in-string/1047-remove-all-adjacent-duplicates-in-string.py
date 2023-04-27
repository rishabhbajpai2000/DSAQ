class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
            if len(stack)>0 and stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        print(stack)
        return "".join(stack)
                