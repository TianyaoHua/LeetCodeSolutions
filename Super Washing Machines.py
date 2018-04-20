class Solution:
    def core(self, machines, i, target):
        n = len(machines)
        while i < n and machines[i] == target:
            i += 1
        if i == n:
            return 0
        diff1 = target - machines[i]
        machines[i] += diff1
        machines[i+1] -= diff1

        diff2 = target - machines[i+1]
        rest = self.core(machines, i+1, target)
        if (diff1 > 0 and diff2 > 0) or (diff1 <0 and diff2 < 0):
            diff1, diff2 = abs(diff1), abs(diff2)
            # if diff1 <= diff2:
            #     return rest
            # else:
            actual_diff = max(diff1 - diff2, 0)
            parallel = rest - diff2
            actual_steps = max(actual_diff - parallel, 0)
            return rest + actual_steps
        else:
            diff1, diff2 = abs(diff1), abs(diff2)
            parallel = rest - diff2
            actual_steps = max(diff1 - parallel, 0)
            return rest + actual_steps


    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        s = sum(machines)
        n = len(machines)
        if s%n != 0:
            return -1
        target = s//n
        diff = []
        for i in range(n-1):
            d = target - machines[i]
            machines[i] += d
            machines[i + 1] -= d
            diff.append(d)
        diff.append(0)
        table = [0 for _ in range(n)]
        for i in range(n-2, -1, -1):
            diff1, diff2 = abs(diff[i]), abs(diff[i+1])
            if (diff[i] > 0 and diff[i+1] > 0) or (diff[i] < 0):
                actual_diff = max(diff1 - diff2, 0)
                parallel = table[i+1] - diff2
                actual_steps = max(actual_diff - parallel, 0)
                table[i] = table[i+1] + actual_steps
            else:
                parallel = table[i+1] - diff2
                actual_steps = max(diff1 - parallel, 0)
                table[i] = table[i + 1] + actual_steps
        print(diff)
        return table[0]


print(Solution().findMinMoves([9,1,8,8,9]))