class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        n = len(board)
        m = len(board[0])
        answer = 0
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'X':
                    if i == 0 and j == 0:
                        answer += 1
                    elif i == 0 and board[i][j-1]=='.':
                        answer += 1
                    elif j == 0 and board[i-1][j] == '.':
                        answer += 1
                    elif (board[i-1][j] == '.' and board[i][j-1]=='.'):
                        answer += 1
        return answer



solution = Solution()
print(solution.countBattleships([["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]))