class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = ' '+s
        n = len(s)
        start = 0
        end = 0
        for i in range(n-1, -1, -1):
            if start == 0 and s[i] != ' ':
                start = i
            if start != 0 and s[i] == ' ':
                end = i
                break
        return start-end

if __name__ == "__main__":
    s = ''
    solution = Solution()
    print(solution.lengthOfLastWord(s))