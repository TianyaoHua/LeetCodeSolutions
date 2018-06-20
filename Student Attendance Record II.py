class Solution(object):
    def f(self, n, h):
        if n in h:
            return h[n]
        else:
            n1 = n // 2
            table1 = self.f(n1, h)
            table = [0]*27
            if n % 2 == 0:
                for i in range(3):
                    for j in range(3):
                        for t1 in range(3):
                            for t2 in range(2 - t1 + 1):
                                table[i * 6 + 2 * j] += (table1[i * 6 + 2 * t1] * table1[t2 * 6 + j * 2])%int(1e9 + 7)
                                table[i * 6 + 2 * j + 1] += (table1[i * 6 + t1 * 2] * table1[t2 * 6 + j * 2 + 1])%int(1e9 + 7)
                                table[i * 6 + 2 * j + 1] += (table1[i * 6 + t1 * 2 + 1] * table1[t2 * 6 + j * 2])%int(1e9 + 7)
            else:
                for i in range(3):
                    for j in range(3):
                        for t1 in range(3):
                            for t2 in range(3):
                                table[i * 6 + 2 * j + 1] += (table1[i * 6 + 2 * t1] * table1[t2 * 6 + j * 2])%int(1e9 + 7)
                                if t1 + t2 < 2:
                                    table[i * 6 + 2 * j] += (table1[i * 6 + 2 * t1] * table1[t2 * 6 + j * 2]*2)%int(1e9 + 7)
                                    table[i * 6 + 2 * j + 1] += (2*(table1[i * 6 + 2 * t1 + 1]*table1[t2 * 6 + j * 2] + \
                                                            table1[i * 6 + 2 * t1]*table1[t2 * 6 + j * 2 + 1]))%int(1e9 + 7)
                                else:
                                    table[i * 6 + 2 * j] += (table1[i * 6 + 2 * t1] * table1[t2 * 6 + j * 2])%int(1e9 + 7)
                                    table[i * 6 + 2 * j + 1] += (( table1[i * 6 + 2 * t1 + 1] * table1[t2 * 6 + j * 2] + \
                                    table1[i * 6 + 2 * t1] * table1[t2 * 6 + j * 2 + 1]))%int(1e9 + 7)
            h[n] = table
            return table
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        h = {}
        h[1] = [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        h[2] = [1, 2, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
        h[3] = [2, 5, 1, 2, 1, 1, 1, 2, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0]
        table = self.f(n, h)
        answer = sum(table)
        return answer % int(1e9 + 7)
print(Solution().checkRecord(100))
