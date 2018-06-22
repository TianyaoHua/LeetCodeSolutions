class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = 0
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] != n:
                next_ = nums[i]
                nums[i] = n
                length = 1
                while nums[next_] != n:
                    temp = next_
                    next_ = nums[next_]
                    nums[temp] = n
                    length += 1
                answer = max(answer, length)
        return answer

print(Solution().arrayNesting([5,4,0,3,1,6,2]))