class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        answer = []
        n = len(nums)
        for i in range(0, n-k+1):
            answer.append(max(nums[i:i+k]))
        return answer

solution = Solution()
nums = [1]
k = 1
print(solution.maxSlidingWindow(nums,k))