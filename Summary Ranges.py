class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        nums.append(float('inf'))
        n = len(nums)
        answer= []
        p = 0
        for i in range(n):
            if nums[i]-nums[i-1] > 1:
                if i-1 > p:
                    answer.append(str(nums[p]) + '-' + '>' + str(nums[i-1]))
                else:
                    answer.append(str(nums[p]))
                p = i
        return answer


solution = Solution()
nums = [0,1,2,4,5,7]
print(solution.summaryRanges(nums))
