class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        j = 0
        nt = len(t)
        ns = len(s)
        while j < ns and i < nt:
            target = s[j]
            while i < nt and t[i] != target:
                i += 1
            i += 1
            j += 1
        if j == ns:
            return True
        else:
            return False

solution = Solution()
s = "acb"
t = "ahbgdc"
print(solution.isSubsequence(s,t))