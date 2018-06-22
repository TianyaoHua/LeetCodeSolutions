class Solution(object):
    def f(self, nums, i, j, k):
        if i == j:
            return int(nums[i] == k)
        else:
            p = (i + j) // 2
            table = {}
            s = 0
            for q in range(p+1, j+1):
                s += nums[q]
                if s not in table:
                    table[s] = 0
                table[s] += 1
            answer = 0
            s = 0
            for q in range(p, i-1, -1):
                s += nums[q]
                if k-s in table:
                    answer += table[k-s]
            answer += self.f(nums, i, p, k) + self.f(nums, p+1, j, k)
            return answer


    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.f(nums, 0, len(nums)-1, k)
print(Solution().subarraySum([1,1,1],1))