class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        summation = sum(A)
        n = len(A)
        diff = 0
        max_diff = -float('inf')
        for i in range(n-1,0,-1):
            diff += summation - n*A[i]
            max_diff = max(max_diff, diff)
        return sum([i*A[i] for i in range(n)])+max_diff


solution = Solution()
print(solution.maxRotateFunction([4,3,2,6]))
