class Solution(object):

    def dfs(self, nums, visited, n, answer):
        if n > 0:
            n = len(nums)
            for i in range(n):
                if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                    temp = visited[:]
                    visited.append(nums[i])
                    next_nums = nums[:]
                    next_nums.remove(nums[i])
                    self.dfs(next_nums, visited, n-1, answer)
                    visited = temp[:]
        else:
            answer.append(visited)

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        answer =[]
        self.dfs(nums,[],len(nums),answer)
        return answer

if __name__ == "__main__":
    array = [1,1,1]
    solution = Solution()
    answer = solution.permuteUnique(array)
    print(answer)