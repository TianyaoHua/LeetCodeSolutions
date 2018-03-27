class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums[:] = nums[n-k:] + nums[0:n-k]
        print(nums)

solution = Solution()
nums = [1,2,3,4,5,6,7]
k = 3
solution.rotate(nums,k)
print(nums)