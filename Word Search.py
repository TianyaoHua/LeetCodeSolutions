class Solution(object):
    def dfs(self, board, word,  visited, n_v, k, solution):
        if n_v < k:
            c = word[n_v]
            tail = visited[-1]
            lv = len(visited)
            m = len(board)
            n = len(board[0])
            if [tail[0] + 1, tail[1]] not in visited and tail[0] + 1 < m and board[tail[0] + 1][tail[1]] == c:
                visited.append([tail[0] + 1, tail[1]])
                if self.dfs(board, word, visited, n_v+1, k, solution):
                    return True
                visited = visited[0:lv]
            if [tail[0] - 1, tail[1]] not in visited and tail[0] - 1 > -1 and board[tail[0] - 1][tail[1]] == c:
                visited.append([tail[0] - 1, tail[1]])
                if self.dfs(board, word, visited, n_v + 1, k, solution):
                    return True
                visited = visited[0:lv]
            if [tail[0], tail[1] + 1] not in visited and tail[1] + 1 < n and board[tail[0]][tail[1] + 1] == c:
                visited.append([tail[0], tail[1] + 1])
                if self.dfs(board, word, visited, n_v + 1, k, solution):
                    return True
                visited = visited[0:lv]
            if [tail[0], tail[1] - 1] not in visited and tail[1] - 1 > -1 and board[tail[0]][tail[1] - 1] == c:
                visited.append([tail[0], tail[1] - 1])
                if self.dfs(board, word, visited, n_v + 1, k, solution):
                    return True
                #visited = visited[0:lv]
            return False
        else:
            return True

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        solution = []
        c = word[0]
        m = len(board)
        n = len(board[0])
        visited = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == c:
                    visited.append([i,j])
        for v in visited:
            if self.dfs(board, word, [v], 1, len(word), solution):
                return True
        return False

if __name__ == "__main__":
    solution = Solution()
    board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
    word = "ABCED"
    answer = solution.exist(board, word)
    print(answer)
