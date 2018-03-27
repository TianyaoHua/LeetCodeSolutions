class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        n = len(nums)
        if not n:
            return 0
        length = 1
        j = 1
        while j < n:
            if nums[j] == nums[j-1]:
                i += 1
            else:
                i = 1
            if i <= 2:
                length += 1
            else:
                nums.remove(nums[j])
                n -= 1
                j -= 1
            j += 1
        return length


nums = [1,1,1,1]
solution = Solution()
print(solution.removeDuplicates(nums))
