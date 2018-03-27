class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        a = []
        for i in range(0, numRows):
            a.append([1 for j in range(i+1)])
            for k in range(1, i):
                a[i][k] = a[i-1][k-1] + a[i-1][k]
        return a[numRows-1]

solution = Solution()
print(solution.generate(3))
