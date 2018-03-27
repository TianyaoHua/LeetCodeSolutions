class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] != i+1 and nums[nums[i]-1] != nums[i]:
                temp = nums[i]
                nums[i] = nums[nums[i]-1]
                nums[temp-1] = temp
        answer = []
        for i in range(n):
            if nums[i] != i+1:
                answer.append(i+1)
        return answer