class Solution(object):
    def arrange(self, N, positions):
        if N == 0:
            return 1
        else:
            answer = 0
            for p in positions:
                if p % N == 0 or N % p == 0:
                    r_positions = positions[:]
                    r_positions.remove(p)
                    answer += self.arrange(N-1, r_positions)
            return answer

    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        return self.arrange(N, [i+1 for i in range(N)])

print(Solution().countArrangement(15))