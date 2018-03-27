class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)
        m = len(word2)
        if not n:
            return m
        if not m:
            return n
        table = [[0 for i in range(n)] for j in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    if word1[j] == word2[i]:
                        table[i][j] = 0
                    else:
                        table[i][j] = 1
                elif j == n-1:
                    if word1[j] == word2[i]:
                        table[i][j] = m-1-i
                    else:
                        table[i][j] = min(m - 1 - i + 1, table[i+1][j] + 1)
                elif i == m-1:
                    if word1[j] == word2[i]:
                        table[i][j] = n-1-j
                    else:
                        table[i][j] = min(n - 1 - j + 1, table[i][j+1] + 1)
                else:
                    if word1[j] == word2[i]:
                        table[i][j] = table[i+1][j+1]
                    else:
                        table[i][j] = min(table[i+1][j], table[i][j+1], table[i+1][j+1])+1
        return table[0][0]

if __name__ == "__main__":
    solution = Solution()
    word1 = 'horse'
    word2 = 'ros'
    print(solution.minDistance(word1,word2))