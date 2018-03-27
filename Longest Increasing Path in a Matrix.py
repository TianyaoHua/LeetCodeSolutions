class Solution(object):
    def DFS(self, i, j, matrix, lengths,n,m):
        neighbours = [[i, j - 1], [i, j + 1], [i - 1, j], [i + 1, j]]
        for v in neighbours:
            if 0 <= v[0] < n and 0 <= v[1] < m and matrix[v[0]][v[1]] > matrix[i][j]:
                if lengths[v[0]][v[1]] > -1:
                    lengths[i][j] = max(lengths[i][j], 1 + lengths[v[0]][v[1]])
                else:
                    lengths[i][j] = max(lengths[i][j], 1 + self.DFS(v[0],v[1],matrix,lengths,n,m))
        lengths[i][j] = max(1, lengths[i][j])
        return lengths[i][j]

    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n = len(matrix)
        m = len(matrix[0])
        lengths = [[-1 for j in range(m)] for i in range(n)]
        max_length = 0
        for i in range(n):
            for j in range(m):
                if lengths[i][j] != -1:
                    max_length = max(max_length, lengths[i][j])
                else:
                    max_length = max(max_length, self.DFS(i,j,matrix,lengths,n,m))
        return max_length



solution = Solution()
matrix = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
print(solution.longestIncreasingPath(matrix))