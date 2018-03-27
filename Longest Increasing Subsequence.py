class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        table = [0 for i in range(n)]
        table[0] = 1
        for i in range(n):
            max_ = 0
            for j in range(i+1):
                if nums[i] >= nums[j]:
                    max_ = max(table[j] + 1, max_)
            table[i] = max_
        return max(table)