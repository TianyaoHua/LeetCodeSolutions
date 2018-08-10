class Solution(object):
    def kInverse(self, n, k, table):
        if k == 0 and n > 0:
            return 1
        elif n == 1 and k > 0:
            return 0
        if (n,k) in table:
            return table[(n, k)]
        else:
            answer = 0
            for t in range(max(1, n - k), n+1):
                answer += self.kInverse(n - 1, k - n + t, table)
            answer %= int(1e9+7)
            table[(n, k)] = answer
            return answer

    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        table = [[0 for j in range(k + 1)] for i in range(n)]
        for i in range(n):
            table[i][0] = 1
        for i in range(1, n):
            for j in range(1, k + 1):
                self_s = max(j-i,0)
                pre_s = max(j-i-1,0)
                if self_s != pre_s:
                    table[i][j] = table[i][j-1] + table[i-1][j] - table[i-1][pre_s]
                else:
                    table[i][j] = table[i][j-1] + table[i-1][j]
                print(i, j)
                table[i][j] %= int(1e9+7)
        return table[n-1][k]


print(Solution().kInversePairs(4, 2))
