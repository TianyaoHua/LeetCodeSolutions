class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        m = [0]*n
        m[n-1] = nums[n-1]
        max_ = m[n-1]
        for i in range(n-2,-1,-1):
            m[i] = max(nums[i], nums[i]+m[i+1])
            if max_ < m[i]:
                max_ = m[i]
        return max_

if __name__ == "__main__":
    solution = Solution()
    nums = [-1]
    print(solution.maxSubArray(nums))