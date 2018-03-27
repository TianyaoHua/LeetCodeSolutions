class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        n = len(matrix)
        m = len(matrix[0])
        table = [[0 for i in range(m+1)] for i in range(n+1)]
        answer = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                a = i - 1
                b = j - 1
                if matrix[a][b] == '1':
                    k = 0
                    limit = -1
                    max_area = 1
                    while k <= a:
                        t = 0
                        while t < b - limit:
                            if matrix[a - k][b - t] == '1':
                                s = (t+1)*(k+1)
                                max_area = (max_area > s) * max_area + (max_area <= s) * s
                                t += 1
                            else:
                                limit = b - t
                        k += 1
                    table[i][j] = max(table[i][j-1], table[i-1][m],max_area)
                else:
                    table[i][j] = max(table[i][j-1], table[i-1][m])
        return table[n][m]

if __name__ == "__main__":
    solution = Solution()
    matrix =[["1","1","0","1"],["1","1","0","1"],["1","1","1","1"]]
    print(solution.maximalRectangle(matrix))






