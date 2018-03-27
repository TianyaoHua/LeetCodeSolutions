class Solution(object):
    def dfs(self, color, nums, i, n, direction):
        if (nums[i]>0) != direction:
            return False
        if color[i] == 1:
            color[i] = 2
            return True
        next_index = (i + nums[i]) % n
        if next_index != i:
            color[i] = 1
            answer = self.dfs(color, nums, next_index, n, direction)
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
                if self.dfs(color,nums,i,n,nums[i] > 0):
                    return True
            i += 1
        return False

print(Solution().circularArrayLoop([2, -1, 1, 2, 2]))