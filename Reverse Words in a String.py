class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split(' ')
        s = s[::-1]
        answer = ''
        for word in s:
            if word:
                answer += word
                answer += ' '
        return answer[:-1]

solution = Solution()
s = ' '
print(solution.reverseWords(s))