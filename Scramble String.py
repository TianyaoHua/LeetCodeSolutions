class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n  = len(s1)
        if n != len(s2):
            return False
        if not n:
            return True
        else:
            table = [[False for i in range(n)] for i in range(n)]
            for i in range(n):
                if s1[i] == s2[i]:
                    table[i][i] = True
            for t in range(1, n):
                for i in range(n-t):
                    j = i + t
                    for k in range(i, j):
                        table[i][j] = table[i][j] or (table[i][k] and table[k+1][j])
                    table[i][j] = table[i][j] or (s1[i: j+1] == s2[i: j+1][::-1])
            return table[0][n-1]

if __name__ == "__main__":
    solution = Solution()
    str1 = ""
    str2 = ""
    print(solution.isScramble(str1,str2))

