class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        n = len(dungeon[0])
        table = [[[] for i in range(n+1)] for j in range(m+1)]
        table[1][1] = [[dungeon[0][0], dungeon[0][0]]]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if table[i][j-1]:
                    health = table[i][j-1][0][0] + dungeon[i - 1][j - 1]
                    min_health = min(table[i][j-1][0][1], health)
                    record_for_i_j = [health, min_health]
                    table[i][j].append(record_for_i_j)
                    for record in table[i][j-1][1:]:
                        health = record[0] + dungeon[i-1][j-1]
                        min_health = min(record[1], health)
                        if min_health > table[i][j][-1][1]:
                            record_for_i_j = [health, min(record[1], health)]
                            table[i][j].append(record_for_i_j)
                if table[i-1][j]:
                    health = table[i-1][j][0][0] + dungeon[i - 1][j - 1]
                    min_health = min(table[i-1][j][0][1], health)
                    record_for_i_j = [health, min_health]
                    table[i][j].append(record_for_i_j)
                    for record in table[i-1][j][1:]:
                        health = record[0] + dungeon[i - 1][j - 1]
                        min_health = min(record[1], health)
                        if min_health > table[i][j][-1][1]:
                            record_for_i_j = [health, min(record[1], health)]
                            table[i][j].append(record_for_i_j)
                if i == m and j == n:
                    print(table[i][j])
                table[i][j].sort(key= lambda x: x[0], reverse=True)
                if i == m and j == n:
                    print(table[i][j])
        return table
        max_ = table[m][n][0][1]
        for i in table[m][n]:
            if max_ < i[1]:
                max_ = i[1]
        if max_ <= 0:
            return -max_+1
        else:
            return 1

solution = Solution()
dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
print(solution.calculateMinimumHP(dungeon))
