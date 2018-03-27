class Solution(object):
    def s(self, nums, i, target, dict):
        if (i, target) in dict:
            return dict[(i, target)]
        elif i == len(nums)-1:
            if nums[i] == abs(target):
                if target == 0:
                    return 2
                else:
                    return 1
            else:
                return 0
        else:
            answer = self.s(nums,i+1,target-nums[i],dict) + self.s(nums, i+1, target+nums[i], dict)
            dict.update({(i,target): answer})
            return answer
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        return self.s(nums,0,S,{})

print(Solution().findTargetSumWays([1, 0],1))