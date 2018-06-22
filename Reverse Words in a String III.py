class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s1 = s.split(' ')
        for i in range(len(s1)):
            s1[i] = s1[i][::-1]
        answer = ''
        for word in s1:
            answer += word + ' '
        return answer[:-1]

print(Solution().reverseWords("Let's take LeetCode contest"))
