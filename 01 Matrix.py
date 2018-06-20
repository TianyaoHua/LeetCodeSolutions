class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        X = len(matrix)
        Y = len(matrix[0])
        Q = []
        for i in range(X):
            for j in range(Y):
                if matrix[i][j]:
                    matrix[i][j] = float('inf')
                else:
                    Q.append((i, j))
        i = 0
        while i < len(Q):
            u = Q[i]
            (x, y) = u
            if x - 1 >= 0 and matrix[x][y] + 1 < matrix[x - 1][y]:
                Q.append((x-1, y))
                matrix[x-1][y] = matrix[x][y] + 1
            if x + 1 < X and matrix[x][y] + 1 < matrix[x + 1][y]:
                Q.append((x+1,y))
                matrix[x + 1][y] = matrix[x][y] + 1
            if y - 1 >= 0 and matrix[x][y] + 1 < matrix[x][y - 1]:
                Q.append((x, y-1))
                matrix[x][y-1] = matrix[x][y] + 1
            if y + 1 < Y and matrix[x][y] + 1 < matrix[x][y + 1]:
                Q.append((x, y + 1))
                matrix[x][y + 1] = matrix[x][y] + 1
            i += 1
        return matrix

matrix = [[1, 0, 1, 1, 0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 0, 1, 0, 1, 1], [0, 0, 1, 0, 1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 1, 1, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 0, 1, 1], [1, 0, 0, 0, 1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0, 1, 0], [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]]
print(Solution().updateMatrix(matrix))
