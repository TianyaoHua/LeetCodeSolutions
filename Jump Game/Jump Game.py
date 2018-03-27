class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        target = len(nums) - 1
        i = target - 1
        while target > 0:
            if i < 0:
                return False
            if i + nums[i] >= target:
                target = i
                i -= 1
            else:
                i -= 1
        return True




if __name__ == "__main__":
    solution = Solution()
    nums = [3,0,8,2,0,0,1]
    print(solution.canJump(nums))
