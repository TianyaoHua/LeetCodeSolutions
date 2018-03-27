class Solution(object):
    def wfs(self,nums,v):
        for j in range(len(v)-1, -1, -1):
            if v[j][-1] + nums[v[j][-1]] < len(nums)-1:
                position = v[j][-1]
                v[j] = v[j][:-1] + [nums[position + 1], position + 1]
                for i in range(position + 2, position + nums[position] + 1):
                    v.append(v[j][:-2] + [(nums[i]), i])
            else:
                return v[j]
        return self.wfs(nums, v)

    def wfs_2(self,nums,v):
        for j in range(len(v)-1, -1, -1):
            if v[j][1] + nums[v[j][1]] < len(nums)-1:
                position = v[j][1]
                v[j] = [nums[position + 1], position + 1, v[j][2]+1]
                for i in range(position + 2, position + nums[position] + 1):
                    v.append([nums[i], i, v[j][2]])
            else:
                return v[j]
        return self.wfs_2(nums, v)

    def wfs_3(self,nums, start, end, n):
        if end >= len(nums)-1:
            return n
        max_p = 0
        for i in range(start, end+1):
            if i + nums[i] > max_p:
                max_p = i + nums[i]
        start = end + 1
        end = max_p
        n += 1
        a = self.wfs_3(nums, start, end, n)
        return a

    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        else:
            n = 0
            start = 0
            end = nums[0]
            while end < len(nums)-1:
                max_p = 0
                for i in range(start, end + 1):
                    if i + nums[i] > max_p:
                        max_p = i + nums[i]
                start = end + 1
                end = max_p
                n += 1
            return n


if __name__ == "__main__":
    array = [1,2]
    solution = Solution()
    answer = solution.jump(array)+1
    print(answer)