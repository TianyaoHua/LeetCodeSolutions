class Solution(object):
    def rob1(self, nums):
        n = len(nums)
        table = [0]*(n+1)
        table[1] = nums[0]
        for i in range(2, n+1):
            table[i] = max(table[i-1], table[i-2] + nums[i-1])
        return table[-1]

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_value = -float('inf')
        for i in range(1, len(nums)):
            nums_ = nums[0: i-1] + nums[i: ]
            max_value = max(self.rob1(nums_), max_value)
        max_value = max(self.rob1(nums[0:-1]), max_value)
        return max_value
