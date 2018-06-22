class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        answer = 0
        for i in range(len(nums)):
            if i%2==0:
                answer += nums[i]
        return answer