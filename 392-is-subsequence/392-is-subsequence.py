import re
class Solution(object):
    def isSubsequence(self, s, t):
        return re.match(".*" + ".*".join(s) + ".*", t)    