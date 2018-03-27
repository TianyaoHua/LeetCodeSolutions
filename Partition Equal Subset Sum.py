class Solution(object):
    def hit(self, nums, i, target, dict):
        if (i,target) in dict:
            return dict[(i, target)]
        elif i >= len(nums) or target < 0:
            return False
        else:
            answer = self.hit(nums, i+1,target-nums[i], dict) or self.hit(nums, i+1, target, dict)
            dict.update({(i,target): answer})
            return answer
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        target = sum(nums)
        if target % 2:
            return False
        target = target//2
        nums.sort(reverse=1)
        n = len(nums)
        dict = {(i,0): True for i in range(n+1)}
        return self.hit(nums,0,target,dict)

solution = Solution()
print(solution.canPartition([1,2,3,5]))