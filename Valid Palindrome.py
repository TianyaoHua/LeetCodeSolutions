import re
rule=re.compile(r'[^a-zA-Z0-9]')


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = rule.sub('', s)
        a = a.lower()
        return a == a[::-1]

solution = Solution()
s = ""
print(solution.isPalindrome(s))