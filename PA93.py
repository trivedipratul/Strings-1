#Time Complexity - O(n)
#Space Complexity - O(n)
from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if not s:
            return 0
        d = defaultdict(int)
        l = 0
        r = 0
        ans = 0
        while l < len(s) and r < len(s):
            if d[s[r]] == 0:
                d[s[r]] = 1
                r = r + 1
                ans = max(ans,r-l)
            else:
                del d[s[l]]
                l = l + 1
        return ans
            