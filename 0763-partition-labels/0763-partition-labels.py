def break_here(post_freq, pre_freq):
    s1 = set(post_freq.keys())
    s2 = set(pre_freq.keys())

    return True if len(s1.intersection(s2)) == 0 else False
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # making a frequency list first

        post_freq = dict()
        pre_freq = dict()

        for i in s:
            if post_freq.__contains__(i):
                post_freq[i] += 1
            else:
                post_freq[i] = 1

#         post_freq[s[0]] -= 1
#         pre_freq[s[0]] = 1

        ans = []
        for i in range(len(s)):

            post_freq[s[i]] -= 1
            if post_freq[s[i]] == 0:
                del post_freq[s[i]]
            if pre_freq.__contains__(s[i]):
                pre_freq[s[i]] += 1
            else:
                pre_freq[s[i]] = 1


            if break_here(post_freq, pre_freq):
                ans.append(i)

        # print(ans)
        for i in range(len(ans)-1,0,-1):
            ans[i] = ans[i] - ans[i-1]
        
        ans[0] += 1
        return ans