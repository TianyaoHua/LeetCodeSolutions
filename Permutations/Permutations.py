class Solution(object):
    def wfs(self, nums, visited, n):
        if n > 0:
            n_v = len(visited)
            visited = visited * len(nums)
            for i in range(len(visited)):
                visited[i] = visited[i] + [nums[int(i/n_v)]]
            return self.wfs(nums, visited, n-1)
        else:
            return visited

    def dfs(self, nums, visited, n, answer):
        if n > 0:
            for element in nums:
                temp = visited[:]
                visited.append(element)
                next_nums = nums[:]
                next_nums.remove(element)
                self.dfs(next_nums, visited, n-1, answer)
                visited = temp[:]
        else:
            answer.append(visited)

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = []
        self.dfs(nums, [], len(nums),answer)
        return answer

if __name__ == "__main__":
    array = [1,2,3]
    solution = Solution()
    permutations = solution.permute(array)
    print(permutations)
