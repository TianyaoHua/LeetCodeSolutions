class Solution(object):
    def check(self, num, i, j, k, table):
        if j == i:
            return False
        if j - i == 1:
            return (num[j] + num[i]) % k == 0
        p = (i+j)//2
        if self.check(num, i, p, k, table):
            return True
        elif self.check(num, p+1, j, k, table):
            return True
        else:
            found = False
            t = p
            iteration = j - p
            right_sums = {table[m + 1] - table[p + 1] for m in range(p + 1, j + 1)}
            while not found and t >= i:
                UPPER = (table[j+1] - table[t])//k
                left_sum = table[p+1] - table[t]
                if UPPER < iteration:
                    n = 0
                    while n <= UPPER and found == False:
                        if n*k - left_sum in right_sums:
                            found = True
                        n += 1
                else:
                    x = p+1
                    while x <= j and not found:
                        if (left_sum + table[x+1] - table[p+1]) % k == 0:
                            found = True
                        x += 1
                t -= 1
            return found

    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 0:
            return True
        table = [0]
        for i in nums:
            table.append(table[-1] + i)
        return self.check(nums,0, len(nums)-1, k, table)

print(Solution().checkSubarraySum([1,2,3], 6))