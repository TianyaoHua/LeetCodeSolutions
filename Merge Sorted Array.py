class Solution(object):
    def insert(self, nums, n, target):
        nums.append(target)
        i = n
        while nums[i] < nums[i-1]:
            temp = nums[i]
            nums[i] = nums[i-1]
            nums[i-1] = temp
            i -= 1

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            self.insert(nums1, m+i, nums2[i])
        print(nums1)

nums1 = [1,5,8,9,34,123,543]
nums2 = [2,4,6,7]
solution = Solution()
solution.merge(nums1, len(nums1), nums2, len(nums2))
