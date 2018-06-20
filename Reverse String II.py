class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        n = len(s)
        for i in range(0, n, 2*k):
            if i + k < n:
                s[i: i+k] = s[i: i+k][::-1]
            else:
                s[i: n] = s[i: n][::-1]
        return ''.join(s)

print(Solution().reverseStr("abcdefg", 2))
