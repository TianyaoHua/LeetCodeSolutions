class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return n
        answer = 1
        h = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                if h == -1 or h == 0:
                    h = 1
                    answer += 1
            elif nums[i] < nums[i-1]:
                if h == 1 or h == 0:
                    h = -1
                    answer += 1
        return answer


solution = Solution()
print(solution.wiggleMaxLength([1,2,3,4,5,6,7,8,9]))
