class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        else:
            table = [0 for i in range(n+1)]
            table[1] = 1
            table[2] = 1
            for i in range(3, n+1):
                add1 = 2
                result = add1*table[i-add1]
                flag = 1
                while flag:
                    add1 += 1
                    new_result = max(add1*table[i-add1], add1*(i-add1))
                    if new_result > result:
                        result = new_result
                    else:
                        table[i] = result
                        flag = 0
            return table[-1]

solution = Solution()
print(solution.integerBreak(58))
