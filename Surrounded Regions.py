class Solution(object):
    def BFS(self, s, board, m, n):
        Q = [s]
        safe_flag = 0
        result = {s}
        while Q:
            u = Q.pop(0)
            [x, y] = u.split(',')
            x = int(x)
            y = int(y)
            result.update({u})
            if x == 0 or x == m-1 or y == 0 or y == n-1:
                safe_flag = 1
            adj = [[x-1,y],[x+1,y],[x, y-1], [x, y+1]]
            for v in adj:
                i = v[0]
                j = v[1]
                v_ = str(i)+','+str(j)
                if 0 <= i <= m-1 and 0 <= j <= n-1 and board[i][j] == 'O' and v_ not in result and u not in Q:
                    Q.append(v_)
        return safe_flag, result

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        safe = set()
        for i in range(m):
            for j in range(n):
                s = str(i)+','+str(j)
                if board[i][j] == 'O' and s not in safe:
                    safe_flag, result = self.BFS(s, board, m, n)
                    if safe_flag:
                        safe.update(result)
                    else:
                        for node in result:
                            [x, y] = node.split(',')
                            board[int(x)][int(y)] = 'X'
        return board

solution = Solution()
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
print(solution.solve(board))