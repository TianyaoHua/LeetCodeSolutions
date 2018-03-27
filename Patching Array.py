class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        i = 0
        p = 0
        k = 1
        answer = 0
        while k <= n:
            if i >= len(nums):
                nums.append(k)
                k += 1
                answer += 1
            elif k - nums[i] < 0:
                answer += 1
                nums = nums[0:i] + [k] + nums[i:]
                k += 1
            else:
                k = p+nums[i]+1
                i += 1
                p = k-1
        return answer




solution = Solution()
print(solution.minPatches([1,2,31,33],2147483647))