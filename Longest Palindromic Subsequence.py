class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        table = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            table[i][i] = 1
        for l in range(1, n):
            for i in range(n-l):
                j = i+l
                if s[i] == s[j]:
                    table[i][j] = 2+table[i+1][j-1]
                else:
                    table[i][j] = max(table[i+1][j], table[i][j-1])
        return table[0][n-1]


solution = Solution()
print(solution.longestPalindromeSubseq('bbab'))