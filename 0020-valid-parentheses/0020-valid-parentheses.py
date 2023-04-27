class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ["(", "[", "{"]:
                stack.append(i)
                # print (stack)
            elif i in [")", "]", "}"]:
                if len(stack) == 0: return False
                elif i == "}" and stack[-1] == "{":
                    stack.pop()
                elif i == "]" and stack[-1] == "[":
                    stack.pop()
                elif i == ")" and stack[-1] == "(":
                    # print(stack)
                    stack.pop()
                else: return False
        # print(stack)
        if len(stack) != 0: return False
        return True