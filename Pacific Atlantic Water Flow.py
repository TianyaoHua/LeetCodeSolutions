class Solution(object):
    def DFS(self, matrix, u, visited,n,m):
        visited[u[0]][u[1]] = 1
        if u[0]-1 >= 0 and matrix[u[0]-1][u[1]] >= matrix[u[0]][u[1]] and visited[u[0]-1][u[1]] != 1:
            self.DFS(matrix,(u[0]-1,u[1]),visited,n,m)
        if u[0] + 1 < n and matrix[u[0] + 1][u[1]] >= matrix[u[0]][u[1]] and visited[u[0]+1][u[1]] != 1:
            self.DFS(matrix, (u[0] + 1, u[1]), visited, n, m)
        if u[1] - 1 >= 0 and matrix[u[0]][u[1] - 1] >= matrix[u[0]][u[1]]and visited[u[0]][u[1]-1] != 1:
            self.DFS(matrix, (u[0], u[1] - 1), visited, n, m)
        if u[1] + 1 < m and matrix[u[0]][u[1] + 1] >= matrix[u[0]][u[1]] and visited[u[0]][u[1]+1] != 1:
            self.DFS(matrix, (u[0], u[1] + 1), visited, n, m)

    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(matrix)
        m = len(matrix[0])
        a = [[0 for i in range(m)] for j in range(n)]
        p = [[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            if p[i][0] != 1:
                self.DFS(matrix, (i,0), p, n, m)
        for j in range(m):
            if p[0][j] != 1:
                self.DFS(matrix, (0,j), p, n, m)
        for i in range(n):
            if a[i][m-1] != 1:
                self.DFS(matrix, (i, m-1), a, n, m)
        for j in range(m):
            if a[n-1][j] != 1:
                self.DFS(matrix, (n-1, j), a, n, m)
        answer = []
        for i in range(n):
            for j in range(m):
                if p[i][j] and a[i][j]:
                    answer.append([i,j])
        return answer


# class Solution(object):
#     def dfs(self, matrix, u, visited, p, a, n, m):
#         in_p = False
#         in_a = False
#         if u in visited:
#             if u in p:
#                 in_p = True
#             if u in a:
#                 in_a = True
#             return in_a, in_p
#         else:
#             visited.add(u)
#             if 0 <= u[0] - 1 and matrix[u[0] - 1][u[1]] <= matrix[u[0]][u[1]]:
#                 x, y = self.dfs(matrix, (u[0] - 1, u[1]), visited, p, a, n, m)
#                 in_a = in_a or x
#                 in_p = in_p or y
#             if n > u[0] + 1 and matrix[u[0] + 1][u[1]] <= matrix[u[0]][u[1]]:
#                 x, y = self.dfs(matrix, (u[0] + 1, u[1]), visited, p, a, n, m)
#                 in_a = in_a or x
#                 in_p = in_p or y
#             if 0 <= u[1] - 1 and matrix[u[0]][u[1] - 1] <= matrix[u[0]][u[1]]:
#                 x, y = self.dfs(matrix, (u[0], u[1] - 1), visited, p, a, n, m)
#                 in_a = in_a or x
#                 in_p = in_p or y
#             if 0 <= u[1] - 1 and matrix[u[0]][u[1] - 1] <= matrix[u[0]][u[1]]:
#                 x, y = self.dfs(matrix, (u[0], u[1] - 1), visited, p, a, n, m)
#                 in_a = in_a or x
#                 in_p = in_p or y
#             if m > u[1] + 1 and matrix[u[0]][u[1] + 1] <= matrix[u[0]][u[1]]:
#                 x, y = self.dfs(matrix, (u[0], u[1] + 1), visited, p, a, n, m)
#                 in_a = in_a or x
#                 in_p = in_p or y
#             if u[0] - 1 < 0 or u[1] - 1 < 0:
#                 in_p = True
#             if u[0] + 1 == n or u[1] + 1 == m:
#                 in_a = True
#             if in_a:
#                 a.add(u)
#             if in_p:
#                 p.add(u)
#         return in_a, in_p
#
#     def pacificAtlantic(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: List[List[int]]
#         """
#         if not matrix:
#             return []
#         visited = set()
#         n = len(matrix)
#         m = len(matrix[0])
#         p = {(-1, i) for i in range(m)}.union({(i, -1) for i in range(n)})
#         a = {(n, i) for i in range(m)}.union({(i, m) for i in range(n)})
#         visited = p.union(a)
#         for i in range(n):
#             for j in range(m):
#                 if (i, j) not in visited:
#                     self.dfs(matrix, (i, j), visited, p, a, n, m)
#         return [[u[0], u[1]] for u in p.intersection(a)]


soluiton = Solution()
print(soluiton.pacificAtlantic([[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18],[68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,19],[67,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,85,20],[66,127,180,181,182,183,184,185,186,187,188,189,190,191,192,143,86,21],[65,126,179,224,225,226,227,228,229,230,231,232,233,234,193,144,87,22],[64,125,178,223,260,261,262,263,264,265,266,267,268,235,194,145,88,23],[63,124,177,222,259,288,289,290,291,292,293,294,269,236,195,146,89,24],[62,123,176,221,258,287,308,309,310,311,312,295,270,237,196,147,90,25],[61,122,175,220,257,286,307,320,321,322,313,296,271,238,197,148,91,26],[60,121,174,219,256,285,306,319,324,323,314,297,272,239,198,149,92,27],[59,120,173,218,255,284,305,318,317,316,315,298,273,240,199,150,93,28],[58,119,172,217,254,283,304,303,302,301,300,299,274,241,200,151,94,29],[57,118,171,216,253,282,281,280,279,278,277,276,275,242,201,152,95,30],[56,117,170,215,252,251,250,249,248,247,246,245,244,243,202,153,96,31],[55,116,169,214,213,212,211,210,209,208,207,206,205,204,203,154,97,32],[54,115,168,167,166,165,164,163,162,161,160,159,158,157,156,155,98,33],[53,114,113,112,111,110,109,108,107,106,105,104,103,102,101,100,99,34],[52,51,50,49,48,47,46,45,44,43,42,41,40,39,38,37,36,35]]))

