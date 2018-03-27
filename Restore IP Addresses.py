class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        if n < 4 or n > 12:
            return []
        else:
            solution = []
            table = [[[] for i in range(n)] for j in range(4)]
            for i in range(3):
                table[0][i] = [[i+1]]
            for i in range(1, 4):
                for j in range(i, min(3*(i+1), n)):
                    for element in table[i-1][j-1]:
                        table[i][j].append([1] + element)
                    if j >= 2:
                        for element in table[i-1][j-2]:
                            table[i][j].append([2] + element)
                    if j >= 3:
                        for element in table[i-1][j-3]:
                            table[i][j].append([3] + element)
            print(table[3][n-1])
            for division in table[3][n-1]:
                s_ = s[:]
                answer = ''
                success = 0
                for length in division:
                    if int(s_[0:length]) < 256 and (length == 1 or (s_[0] != '0')):
                        answer = answer + '.' + s_[0:length]
                        s_ = s_[length:]
                        success = 1
                    else:
                        success = 0
                        break
                if success:
                    solution.append(answer[1:])
            return solution




solution = Solution()
s = '101023'
print(solution.restoreIpAddresses(s))

