class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        table_0 = ['u' for i in range(n)]
        table_1 = ['u' for i in range(n)]
        if nums[n-1] > 0:
            table_1[n-1] = nums[n-1]
        else:
            table_0[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            if nums[i] > 0:
                if table_1[i+1]!= 'u' and nums[i] * table_1[i+1] > nums[i]:
                    table_1[i] = nums[i] * table_1[i+1]
                else:
                    table_1[i] = nums[i]
                if table_0[i+1] != 'u':
                    table_0[i] = nums[i]*table_0[i+1]
            else:
                if table_0[i+1] != 'u':
                    table_1[i] = table_0[i+1] * nums[i]
                if table_1[i+1] != 'u' and nums[i] * table_1[i+1] < nums[i]:
                    table_0[i] = nums[i] * table_1[i+1]
                else:
                    table_0[i] = nums[i]
        while 'u' in table_1:
            table_1.remove('u')
        return max(table_1)


solution = Solution()
nums = [-4,-3,-2]
print(solution.maxProduct(nums))