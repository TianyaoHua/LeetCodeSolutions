class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        table = []
        width = 0
        answer = 0
        for i in nums:
            s = bin(i)[2:]
            width=max(width,len(s))
            table.append(list(s))
        for i in range(n):
            table[i] = ['0' for k in range(width-len(table[i]))] + table[i]
        for j in range(width):
            ones = 0
            zeros = 0
            for i in range(n):
                if table[i][j]=='0':
                    zeros += 1
                else:
                    ones += 1
            answer += zeros*ones
        return answer

print(Solution().totalHammingDistance([4,14,2]))