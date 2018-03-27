class Solution(object):
    def r(self, board, i, ball):
        p = i-1
        q = i
        n = len(board)
        while p >= 0 and board[p] == ball:
            p -= 1
        while q < n and board[q] == ball:
            q += 1
        if q-p-1 >= 2:
            if q == n:
                return board[0:p+1]
            elif p == -1:
                return board[q:]
            else:
                return self.r(board[0:p+1]+board[q+1:], p+1,board[q])
        else:
            return board[0:i]+ball+board[i:]
    def get_position(self, board, ball):
        position_1 = []
        position_2 = []
        i = 1
        n = len(board)
        if board[0] == ball:
            position_2.append(0)
        while i < n:
            if board[i - 1] == board[i] == ball:
                position_1.append(i)
                position_2.pop()
                i += 1
            elif board[i] == ball:
                position_2.append(i)
            i += 1
        return position_1+position_2
    def dfs(self, board, hand, dict):
        if not board:
            return 0,[]
        elif not hand:
            return 10,[]
        elif board in dict and all(dict[board][i][0] in hand and dict[board][i][1] <= hand[dict[board][i][0]] for i in range(1, len(dict[board]))):
                return dict[board][0], dict[board][1:]
        else:
            answer = 10
            method = []
            for ball in hand:
                r_hand = hand.copy()
                r_hand[ball] -= 1
                if r_hand[ball] == 0:
                    r_hand.pop(ball)
                position = self.get_position(board, ball)
                for p in position:
                    r_board = self.r(board, p, ball)
                    n,m = self.dfs(r_board, r_hand, dict)
                    if answer > n+1:
                        answer = n+1
                        method = m
                        has_ball_in_m = 0
                        for i in range(len(method)):
                            if method[i][0] == ball:
                                method[i][1] += 1
                                has_ball_in_m = 1
                                break
                        if not has_ball_in_m:
                            method.append([ball, 1])
            dict.update({board: [answer] + method})
            return answer, method

    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """
        hand_dict = {}
        for ball in hand:
            if ball not in hand_dict:
                hand_dict[ball] = 0
            hand_dict[ball] += 1
        dict = {}
        answer = self.dfs(board,hand_dict,dict)
        print(dict)
        if answer == 10:
            return -1
        return answer

print(Solution().findMinStep("WWGWGW",'GWBW'))