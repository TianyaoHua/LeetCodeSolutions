class Solution(object):
    def findWord(self, board, n, m, word):
        l_word = len(word)
        for i in range(n):
            for j in range(m):
                k = 0
                if board[i][j] == word[0]:
                    Q = [[i, j]]
                    k += 1
                    used = set()
                    while Q and k < l_word:
                        n_Q = len(Q)
                        for a in range(n_Q):
                            [u_x, u_y] = Q.pop(0)

                            flag = 0
                            if u_x-1 > -1 and str(u_x-1)+','+str(u_y) not in used and board[u_x-1][u_y] == word[k]:
                                Q.append([u_x-1, u_y])
                                flag = 1
                                #used.update({str(u_x-1)+','+str(u_y)})
                            if u_x+1 < n and str(u_x+1)+','+str(u_y) not in used and board[u_x+1][u_y] == word[k]:
                                Q.append([u_x+1, u_y])
                                flag = 1
                                #used.update({str(u_x + 1) + ',' + str(u_y)})
                            if u_y - 1 > -1 and str(u_x)+','+str(u_y-1) not in used and board[u_x][u_y-1] == word[k]:
                                Q.append([u_x, u_y-1])
                                flag = 1
                                #used.update({str(u_x) + ',' + str(u_y - 1)})
                            if u_y + 1 < m and str(u_x)+','+str(u_y+1) not in used and board[u_x][u_y + 1] == word[k]:
                                Q.append([u_x, u_y+1])
                                flag = 1
                                #used.update({str(u_x) + ',' + str(u_y + 1)})
                            if flag:
                                used.update({str(u_x) + ',' + str(u_y)})
                        k += 1
                    if Q and k == l_word:
                        return True
        return False

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        n = len(board)
        m = len(board[0])
        answer = []
        searched = set()
        for word in words:
            if word not in searched:
                searched.update({word})
                if self.findWord(board, n, m, word):
                    answer.append(word)
        return answer

###should use DFS!!!
solution = Solution()
board = [["a","b","c"],["a","e","d"],["a","f","g"]]
words = ["eaabcdgfa"]
print(solution.findWords(board, words))