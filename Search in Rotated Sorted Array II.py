class Solution(object):
    def binary(self, nums, target):
        i = 0
        j = len(nums) - 1
        p = (i+j)//2
        while j - i > 1:
            if nums[p] > target:
                j = p
                p = (i+p)//2
            elif nums[p] < target:
                i = p
                p = (j+p)//2
            else:
                return True
        if nums[i] == target or nums[j] == target:
            return True
        else:
            return False

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        n = len(nums)
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                return self.binary(nums[i:] + nums[0:i], target)
        return self.binary(nums, target)

solution = Solution()
nums = [4, 5, 6, 7, 0, 1, 2]
print(solution.search(nums, 2))