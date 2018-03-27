class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        table = [0]*(n+1)
        table[0] = 1
        for i in range(1, n+1):
            table[i] = table[i-1] + table[i-2]
        return table[n]

if __name__ == "__main__":
    solution = Solution()
    print(solution.climbStairs(5))
