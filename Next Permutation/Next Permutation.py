class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        increase = 0
        for i in range(l-1,0,-1):
            if nums[i]>nums[i-1]:
                increase = 1
                break
        if increase:
            nums_i_1 = nums[i-1]
            for j in range(l-1,i-1,-1):
                if nums[j] > nums_i_1:
                    break
            temp = nums_i_1
            nums[i-1] = nums[j]
            nums[j] = temp
            k = i
            limit_1 = i + (l-i)/2
            local_sum = i+l-1
            while k < limit_1:
                temp = nums[k]
                nums[k] = nums[local_sum-k]
                nums[local_sum-k]=temp
                k += 1
        else:
            j = 0
            while j < l/2:
                temp = nums[j]
                nums[j] = nums[l-1-j]
                nums[l-1-j] = temp
                j += 1

if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,3,4,1]
    solution.nextPermutation(nums)
    print(nums)