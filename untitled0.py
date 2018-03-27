# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 16:57:27 2018

@author: Hua Tianyao
"""

class Solution(object):
    def dfs(self, color, nums, i, n):
        next_index = (i + nums[i]) % n
        if color[next_index] == 1:
            color[i] = 2
            return True
        elif next_index != i and color[next_index] == 0:
            color[i] = 1
            answer = self.dfs(color, nums, next_index, n)
            color[i] = 2
            return answer
        else:
            color[i] = 2
            return False

    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        color = [0 for i in range(n)]
        i = 0
        while i < n:
            if color[i] == 0:
                if self.dfs(color,nums,i,n):
                    return True
            i += 1
        return False
print(Solution().circularArrayLoop([1,2,3,4,5]))