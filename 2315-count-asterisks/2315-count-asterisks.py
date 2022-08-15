class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0
        count_pipe = 0
        for i in s:
            if count_pipe %2 == 0:
                if i == "*":
                    count += 1
            if i == "|":
                count_pipe += 1
        return count
        