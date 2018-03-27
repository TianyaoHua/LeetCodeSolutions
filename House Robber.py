class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        table = [0]*(n+1)
        table[1] = nums[0]
        for i in range(2, n+1):
            table[i] = max(table[i-1], table[i-2] + nums[i-1])
        return table[-1]

solution = Solution()
nums = [1]
print(solution.rob(nums))