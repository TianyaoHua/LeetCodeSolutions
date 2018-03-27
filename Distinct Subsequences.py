class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        n = len(s)
        m = len(t)
        table = [[0 for i in range(n+1)] for j in range(m+1)]
        for j in range(n + 1):
            table[0][j] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[j-1] == t[i-1]:
                    table[i][j] = table[i][j-1] + table[i-1][j-1]
                else:
                    table[i][j] = table[i][j-1]
        return table[m][n]

if __name__ == "__main__":
    solution = Solution()
    s = "rabbbit"
    t = "rabbit"
    print(solution.numDistinct(s,t))