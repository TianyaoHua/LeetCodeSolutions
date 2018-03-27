class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] != i+1 and nums[i] != nums[nums[i]-1]:
                temp = nums[i]
                nums[i] = nums[nums[i]-1]
                nums[temp-1] = temp
            else:
                i += 1
        answer = []
        for i in range(n):
            if nums[i] != i+1:
                answer.append(nums[i])
        return answer
nums = [4,3,2,7,8,2,3,1]
print(Solution().findDuplicates(nums))