class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        n = len(s)
        i = 0
        while i < n:
            if s[i] == '[':
                stack.append(i)
                i += 1
            elif s[i] == ']':
                index = stack.pop()
                t = s[index+1: i]
                j = index-1
                while '0' <= s[j] <= '9':
                    j -= 1
                number = int(s[j+1:index])
                s = s[0:j+1] + number*t + s[i+1:]
                n = n-i+j+number*(i-index-1)
                i = i-i+j+number*(i-index-1)
            i += 1
        return s


solution = Solution()
print(solution.decodeString('3[a]2[bc]'))