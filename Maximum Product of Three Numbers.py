class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if nums[-3] >= 0:
            answer1 = nums[-3]*nums[-2]*nums[-1]
            answer2 = nums[0]*nums[1]*nums[-1]
            return max(answer1, answer2)
        else:
            answer1 = nums[-1]*nums[-2]*nums[-3]
            answer2 = nums[-3]*nums[-4]*nums[-5]
            return max(answer1, answer2)

