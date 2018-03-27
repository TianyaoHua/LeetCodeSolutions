class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        vowels = {'a','e','i','o','u'}
        i = 0
        j = len(s)-1
        while j > i:
            if s[i] in vowels and s[j] in vowels:
                temp = s[i]
                s[i] = s[j]
                s[j] = temp
                i += 1
                j -=1
            elif s[i] in vowels:
                j -= 1
            elif s[j] in vowels:
                i += 1
            else:
                i += 1
                j -= 1
        return ''.join(s)

solution = Solution()
print(solution.reverseVowels('aA'))