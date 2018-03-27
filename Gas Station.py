class Solution(object):
    def check(self, nums, i, n):
        s = 0
        for j in range(i, n):
            s = s + nums[j]
            if s < 0:
                return 0
        for j in range(i):
            s = s + nums[j]
            if s < 0:
                return 0
        return 1

    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        nums = [(gas[i] - cost[i]) for i in range(n)]
        if sum(nums) < 0:
            return -1
        else:
            for i in range(n):
                success = self.check(nums, i, n)
                if success:
                    return i
            return -1

solution = Solution()
gas=[5]
cost=[4]
print(solution.canCompleteCircuit(gas, cost))