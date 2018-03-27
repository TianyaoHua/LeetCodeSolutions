class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        table = [0 for i in range(n + 1)]
        table[0] = -1
        for i in range(1, n+1):
            min_ = float('inf')
            for j in range(i):
                if 1 + table[j] < min_ and s[j: i] == s[j: i][::-1]:
                    min_ = table[j] + 1
            table[i] = min_
        return table


solution = Solution()
s = 'aab'
print(solution.minCut(s))