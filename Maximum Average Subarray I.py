class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        s = sum(nums[0:k])
        average = s/k
        for i in range(k, len(nums)):
            s += nums[i]
            s -= nums[i-k]
            average = max(average, s/k)
        return average