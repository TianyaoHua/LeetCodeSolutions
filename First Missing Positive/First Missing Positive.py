class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n:
            i = 0
            while i < n:
                if 0 < nums[i] <= n and nums[i] != i+1 and nums[i] != nums[nums[i]-1]:
                    temp = nums[i]
                    nums[i] = nums[nums[i]-1]
                    nums[temp - 1] = temp
                    i -= 1
                i += 1
            for i in range(n):
                if nums[i] != i + 1:
                    return i + 1
            return i+2
        else:
            return 1

if __name__ == "__main__":
    solution = Solution()
    answer = solution.firstMissingPositive([])
    print(answer)