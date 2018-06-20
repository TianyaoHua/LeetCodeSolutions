class Solution:
    def f(self, nums, i, j, table, record_max, record_min):
        if (i, j) in table:
            return table[i, j]
        elif i == j:
            return (nums[i], nums[i])
        else:
            max_val = -float('inf')
            min_val = float('inf')
            for p in range(i, j):
                (max_left, min_left) = self.f(nums, i, p, table, record_max, record_min)
                (max_right, min_right) = self.f(nums, p+1, j, table, record_max, record_min)
                if max_left/min_right > max_val:
                    max_val = max_left/min_right
                    record_max[(i, j)] = p
                if min_left/max_right < min_val:
                    min_val = min_left/max_right
                    record_min[(i, j)] = p
            table[(i, j)] = (max_val, min_val)
            return (max_val, min_val)

    def reconstruct(self, nums, i, j, record_max, record_min, flag):
        if i == j:
            return str(nums[i])
        else:
            if flag:
                p = record_max[(i, j)]
                string1 = self.reconstruct(nums, i, p, record_max, record_min, True)
                string2 = self.reconstruct(nums, p+1, j, record_max, record_min, False)
            else:
                p = record_min[(i, j)]
                string1 = self.reconstruct(nums, i, p, record_max, record_min, False)
                string2 = self.reconstruct(nums, p+1, j, record_max, record_min, True)
            if '/' not in string2:
                return string1 + '/' + string2
            else:
                return string1 + '/' + '(' + string2 + ')'

    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        record_max = {}
        record_min = {}
        self.f(nums, 0, len(nums)-1, {}, record_max, record_min)
        return self.reconstruct(nums, 0, len(nums)-1, record_max, record_min, True)

print(Solution().optimalDivision([1000,100,10,2]))