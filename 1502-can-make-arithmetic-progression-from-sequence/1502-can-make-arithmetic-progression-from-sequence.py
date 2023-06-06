class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        prev = arr[1]
        for i in range(2, len(arr)):
            cur = arr[i]
            if cur - prev != diff: return False
            prev = cur
        return True