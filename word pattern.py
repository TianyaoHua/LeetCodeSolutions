class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        match1 = {}
        match2 = {}
        str = str.split(' ')
        n = len(pattern)
        if n != len(str):
            return False
        for i in range(n):
            if pattern[i] not in match1 and str[i] not in match2:
                match1.update({pattern[i]: str[i]})
                match2.update({str[i]: pattern[i]})
            elif pattern[i] in match1 and str[i] in match2:
                if match1[pattern[i]] != str[i] or match2[str[i]] != pattern[i]:
                    return False
            else:
                return False
        return True

solution = Solution()
pattern = 'abba'
str = 'cat dog dog dog'
print(solution.wordPattern(pattern, str))