#Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
class Solution(object):
    def find(self, nums, i, j, table):
        if i == j:
            return -1
        p = (i+j)//2
        record = {}
        max_length = -float('inf')
        for t in range(p+1, j+1):
            sum2 = table[t+1] - table[p+1]
            l2 = t - p
            record[l2-2*sum2] = l2
        for t in range(i, p+1):
            sum1 = table[p+1] - table[t]
            l1 = p-t+1
            if 2*sum1-l1 in record:
                max_length = max(max_length, l1+record[2*sum1-l1])
        if max_length < p-i+1:
            max_length = max(max_length, self.find(nums, i, p, table))
        if max_length < j-p:
            max_length = max(max_length, self.find(nums, p+1, j, table))
        return max_length

    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        table = [0]
        for i in nums:
            table.append(table[-1] + i)
        n = len(nums)
        if table[-1] == n or table[-1] == 0:
            return 0
        else:
            return self.find(nums, 0, n-1, table)

print(Solution().findMaxLength([0,1,1,1,0,1,0,1,0,1]))