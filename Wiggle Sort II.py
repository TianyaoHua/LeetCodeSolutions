class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n = len(nums)
        a = []
        nums1 = nums[0:n//2+n%2]
        nums2 = nums[n//2+n%2:]
        i=0
        j=0
        for k in range(n):
            if k%2 == 0:
                a.append(nums1[i])
                i += 1
            else:
                a.append(nums2[j])
                j += 1
        for i in range(n-1):
            if a[i] == a[i+1]:
                a = a[i+1:] + a[0:i+1]
        nums[:]=a
        print(nums)

solution = Solution()
nums = [4,5,5,6]
solution.wiggleSort(nums)