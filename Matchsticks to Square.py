class Solution(object):
    def sumup(self, nums, s, i, target, visited, solution):
        if s + nums[i] == target:
            solution.append(visited + [i])
        elif s + nums[i] < target:
            for j in range(i+1, len(nums)):
                self.sumup(nums, s+nums[i], j, target, visited+[i], solution)
    def check(self, nums, target, k):
        if k == 0:
            return True
        solutions = []
        self.sumup(nums,0,0,target,[],solutions)
        for solution in solutions:
            i = 0
            nums_ = []
            for i in range(len(nums)):
                if i not in solution:
                    nums_.append(nums[i])
            if self.check(nums_, target, k-1):
                return True
        return False
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        if s%4 != 0:
            return False
        l = s // 4
        nums.sort(reverse=1)
        return self.check(nums,l,4)

import numpy as np
import time
a = time.time()
print(Solution().makesquare([np.random.randint(1, 10**9) for i in range(15)]))
print(time.time()-a)