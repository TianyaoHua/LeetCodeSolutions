class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = -1
        j = -1
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                k = k+1
                j = j + 1
                temp = nums[i]
                nums[i] = nums[k]
                nums[k] = nums[j]
                nums[j] = temp
            elif nums[i] == 1:
                k += 1
                temp = nums[i]
                nums[i] = nums[k]
                nums[k] = temp
        return nums

if __name__ == "__main__":
    solution = Solution()
    matrix = [0]
    print(solution.sortColors(matrix))