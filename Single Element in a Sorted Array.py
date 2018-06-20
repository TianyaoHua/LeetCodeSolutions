class Solution(object):
    def f(self, nums, i, j):
        p = (i+j)//2
        if ((i < p and nums[p] != nums[p-1]) or (p==i)) and ((p < j and nums[p] != nums[p+1]) or p==j):
            return nums[p]
        elif nums[p] == nums[p-1]:
            if (p-1-i) % 2 != 0:
                return self.f(nums, i, p-2)
            else:
                return self.f(nums,  p+1, j)
        else:
            if (p-i) % 2 != 0:
                return self.f(nums, i, p-1)
            else:
                return self.f(nums, p+2, j)
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = len(nums) - 1
        return self.f(nums, i, j)

print(Solution().singleNonDuplicate([3,3,7,7,10,11,11]))