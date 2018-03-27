class Solution(object):
    def dynamic_core(self, n, table):
        if n in table:
            return table[n]
        elif n == 0:
            table.update({0:0})
            return 0
        else:
            i = 1
            least = float('inf')
            while i * i <= n:
                least = min(least, 1 + self.dynamic_core(n - i * i, table))
                i += 1
            table.update({n:least})
            return least

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # i = 1
        # least = float('inf')
        # table = {}
        # while i*i <= n:
        #     least = min(least, 1 + self.dynamic_core(n - i * i, table))
        #     i += 1
        # return least
        table = [0]
        for i in range(1, n+1):
            least = float('inf')
            j = 1
            while j*j <= i:
                least = min(least, 1 + table[i-j*j])
                j += 1
            table.append(least)
        return table[-1]



solution = Solution()
print(solution.numSquares(8825))