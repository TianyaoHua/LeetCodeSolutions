class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        # n = len(s)
        # table = [[[] for i in range(n)] for j in range(n)]
        # for i in range(n):
        #     table[i][i].append([s[i]])
        # for l in range(1, n):
        #     for i in range(n-l):
        #         j = i + l
        #         for k in range(i, j):
        #             for partition_1 in table[i][k]:
        #                 for partition_2 in table[k+1][j]:
        #                     d = partition_1 + partition_2
        #                     if d not in table[i][j]:
        #                         table[i][j].append(d)
        #         if s[i:j+1] == s[i:j+1][::-1]:
        #             table[i][j].append([s[i:j+1]])
        # return table[0][n-1]
        n = len(s)
        table = [[] for i in range(n+1)]
        table[0] = [[]]
        for i in range(0, n):
            for j in range(i, -1, -1):
                if s[j] == s[i] and s[j: i+1] == s[j: i+1][::-1]:
                    for partition in table[j]:
                        table[i+1].append(partition + [s[j : i+1]])
        return table

solution = Solution()
s = 'aab'
print(solution.partition(s))