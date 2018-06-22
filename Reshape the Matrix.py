class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        x = len(nums)
        y = len(nums[0])
        if x*y != r*c:
            return nums
        else:
            answer = [[] for i in range(r)]
            for i in range(x):
                for j in range(y):
                    line = ((i*y)+j)//c
                    answer[line].append(nums[i][j])
            return answer

print(Solution().matrixReshape(
[[1],[2],[3],[4]],2,2))