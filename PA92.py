#Time Complexity - O(s + t)
#Space Complexity - O(s)
class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        d2 = {}
        ans = ""
        for i in T:
            if i not in S:
                ans = ans + i
            else:
                 d2[i] = d2[i] + 1 if i in d2.keys() else 1
        for i in S:
            if i in d2.keys():
                num = d2[i]
                while num > 0:
                    ans = ans + i
                    num = num - 1
        return(ans)