class Solution(object):
    def isAdjacentToMine(self, X, Y, board, u):
        numberMine = 0
        for i in range(u[0]-1, u[0]+2):
            for j in range(u[1]-1, u[1] + 2):
                if 0 <= i < X and 0 <= j < Y and board[i][j] == 'M':
                    numberMine += 1
        return numberMine
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        X = len(board)
        Y = len(board[0])
        x, y = click[0], click[1]
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        else:
            Q = [(x, y)]
            while Q:
                u = Q.pop()
                numberMine = self.isAdjacentToMine(X,Y,board,u)
                if numberMine:
                    board[u[0]][u[1]] = str(numberMine)
                else:
                    board[u[0]][u[1]] = 'B'
                    for i in range(u[0] - 1, u[0] + 2):
                        for j in range(u[1] - 1, u[1] + 2):
                            if 0 <= i < X and 0 <= j < Y and board[i][j] == 'E':
                                Q.append((i,j))
        return board

board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
click = [3,0]
print(Solution().updateBoard(board, click))


