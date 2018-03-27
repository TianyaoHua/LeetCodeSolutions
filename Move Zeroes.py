class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == 0:
                nums[i: n-1] = nums[i + 1: n]
                nums[n-1] = 0
                n -= 1
                i -= 1
            i += 1
        print(nums)

solution = Solution()
nums = [0, 1, 0 , 13, 2]
solution.moveZeroes(nums)
print(nums)